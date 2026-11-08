"""Async PostgreSQL catalog. Importing does not connect or migrate a database."""
import os
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel, Field, field_validator

class DuplicateAlbum(Exception):
    pass

class AlbumInput(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    artist: str = Field(min_length=1, max_length=200)
    @field_validator("title", "artist")
    @classmethod
    def strip_text(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("text cannot be blank")
        return value

class AlbumOutput(AlbumInput):
    id: int

class PostgresCatalog:
    def __init__(self, pool):
        self.pool = pool
    async def list_all(self):
        async with self.pool.connection() as connection:
            cursor = await connection.execute(
                "SELECT a.id, a.title, r.name AS artist FROM albums a "
                "JOIN artists r ON a.artist_id=r.id ORDER BY a.id")
            return await cursor.fetchall()
    async def get(self, album_id):
        async with self.pool.connection() as connection:
            cursor = await connection.execute(
                "SELECT a.id, a.title, r.name AS artist FROM albums a "
                "JOIN artists r ON a.artist_id=r.id WHERE a.id=%s", (album_id,))
            return await cursor.fetchone()
    async def create(self, album):
        from psycopg.errors import UniqueViolation
        try:
            async with self.pool.connection() as connection:
                # Both statements belong to the same transaction.
                cursor = await connection.execute(
                    "INSERT INTO artists(name) VALUES (%s) "
                    "ON CONFLICT(name) DO UPDATE SET name=excluded.name RETURNING id",
                    (album.artist,))
                artist = await cursor.fetchone()
                cursor = await connection.execute(
                    "INSERT INTO albums(title, artist_id) VALUES (%s, %s) RETURNING id",
                    (album.title, artist["id"]))
                row = await cursor.fetchone()
                return {"id": row["id"], **album.model_dump()}
        except UniqueViolation as cause:
            # The connection context has rolled back before translating the error.
            raise DuplicateAlbum("album already exists for this artist") from cause

@asynccontextmanager
async def postgres_resource():
    from psycopg.rows import dict_row
    from psycopg_pool import AsyncConnectionPool
    dsn = os.environ.get("STUDY_DATABASE_URL")
    if not dsn:
        raise RuntimeError("Set STUDY_DATABASE_URL to your migrated study database")
    pool = AsyncConnectionPool(dsn, min_size=1, max_size=4, open=False,
                               kwargs={"row_factory": dict_row, "connect_timeout": 5})
    try:
        await pool.open()
        await pool.wait(timeout=10)
        yield PostgresCatalog(pool)
    finally:
        await pool.close()

def get_store(request: Request):
    return request.app.state.store

def create_app(resource=postgres_resource):
    @asynccontextmanager
    async def lifespan(app):
        async with resource() as store:
            app.state.store = store
            yield
    app = FastAPI(title="Async study catalog", lifespan=lifespan)
    @app.get("/health")
    async def health():
        return {"status": "ok"}
    @app.get("/albums", response_model=list[AlbumOutput])
    async def albums(store=Depends(get_store)):
        return await store.list_all()
    @app.post("/albums", response_model=AlbumOutput, status_code=201)
    async def create(album: AlbumInput, store=Depends(get_store)):
        try:
            return await store.create(album)
        except DuplicateAlbum:
            raise HTTPException(status_code=409, detail="Album already exists") from None
    @app.get("/albums/{album_id}", response_model=AlbumOutput)
    async def get(album_id: int, store=Depends(get_store)):
        record = await store.get(album_id)
        if record is None:
            raise HTTPException(status_code=404, detail="Album not found")
        return record
    return app

app = create_app()
