"""Local music-catalog API with an isolated SQLite database per app lifespan."""
from contextlib import asynccontextmanager
import sqlite3
import threading
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel, Field, field_validator

class AlbumInput(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    artist: str = Field(min_length=1, max_length=200)
    @field_validator("title", "artist")
    @classmethod
    def clean_text(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("text cannot be blank")
        return value

class AlbumOutput(AlbumInput):
    id: int

class SQLiteCatalog:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.lock = threading.RLock()
        self.connection.execute("CREATE TABLE albums(id INTEGER PRIMARY KEY, title TEXT NOT NULL, artist TEXT NOT NULL)")
    def create(self, album):
        with self.lock, self.connection:
            cursor = self.connection.execute("INSERT INTO albums(title, artist) VALUES (?, ?)",
                                             (album.title, album.artist))
            return {"id": cursor.lastrowid, **album.model_dump()}
    def list_all(self):
        with self.lock:
            return [dict(row) for row in self.connection.execute("SELECT * FROM albums ORDER BY id")]
    def get(self, album_id):
        with self.lock:
            row = self.connection.execute("SELECT * FROM albums WHERE id=?", (album_id,)).fetchone()
            return None if row is None else dict(row)
    def close(self):
        self.connection.close()

def get_store(request: Request):
    return request.app.state.store

def create_app(store_factory=SQLiteCatalog):
    @asynccontextmanager
    async def lifespan(app):
        app.state.store = store_factory()
        try:
            yield
        finally:
            app.state.store.close()
    app = FastAPI(title="Study Music Catalog", lifespan=lifespan)
    @app.get("/health")
    def health():
        return {"status": "ok"}
    @app.get("/albums", response_model=list[AlbumOutput])
    def albums(store=Depends(get_store)):
        return store.list_all()
    @app.post("/albums", response_model=AlbumOutput, status_code=201)
    def create(album: AlbumInput, store=Depends(get_store)):
        return store.create(album)
    @app.get("/albums/{album_id}", response_model=AlbumOutput)
    def get(album_id: int, store=Depends(get_store)):
        album = store.get(album_id)
        if album is None:
            raise HTTPException(status_code=404, detail="Album not found")
        return album
    return app

app = create_app()
