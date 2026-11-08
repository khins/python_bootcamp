"""Offline API tests use a fake; the opt-in integration test uses a temp table."""
import asyncio
import os
import sys
import unittest
from contextlib import asynccontextmanager
from fastapi.testclient import TestClient
from postgres_catalog import create_app, DuplicateAlbum

class MemoryCatalog:
    def __init__(self):
        self.records = []
    async def create(self, album):
        if any(row["title"] == album.title and row["artist"] == album.artist for row in self.records):
            raise DuplicateAlbum()
        row = {"id": len(self.records) + 1, **album.model_dump()}
        self.records.append(row)
        return row.copy()
    async def list_all(self):
        return [row.copy() for row in self.records]
    async def get(self, album_id):
        return next((row.copy() for row in self.records if row["id"] == album_id), None)

@asynccontextmanager
async def fake_resource():
    yield MemoryCatalog()

class OfflineApiTests(unittest.TestCase):
    def setUp(self):
        self.client = self.enterContext(TestClient(create_app(fake_resource)))
    def test_create_get_and_list(self):
        response = self.client.post("/albums", json={"title": "Signals", "artist": "Rush"})
        self.assertEqual(response.status_code, 201)
        row = response.json()
        self.assertEqual(self.client.get(f"/albums/{row['id']}").json(), row)
        self.assertEqual(self.client.get("/albums").json(), [row])
    def test_duplicate_conflict(self):
        data = {"title": "Signals", "artist": "Rush"}
        self.assertEqual(self.client.post("/albums", json=data).status_code, 201)
        self.assertEqual(self.client.post("/albums", json=data).status_code, 409)
    def test_invalid_and_missing(self):
        self.assertEqual(self.client.post("/albums", json={"title": " ", "artist": "Rush"}).status_code, 422)
        self.assertEqual(self.client.get("/albums/99").status_code, 404)
    def test_isolation(self):
        self.assertEqual(self.client.get("/albums").json(), [])

@unittest.skipUnless(os.environ.get("STUDY_TEST_DATABASE_URL"), "No dedicated PostgreSQL test URL configured")
class PostgreSQLIntegrationTests(unittest.TestCase):
    def test_parameterization_constraint_and_rollback(self):
        async def check():
            import psycopg
            async with await psycopg.AsyncConnection.connect(
                os.environ["STUDY_TEST_DATABASE_URL"], autocommit=True, connect_timeout=5) as conn:
                await conn.execute("CREATE TEMP TABLE study_values (title TEXT UNIQUE NOT NULL)")
                async with conn.transaction(force_rollback=True):
                    await conn.execute("INSERT INTO study_values VALUES (%s)", ("O'Reilly",))
                    cursor = await conn.execute("SELECT title FROM study_values")
                    self.assertEqual(await cursor.fetchone(), ("O'Reilly",))
                    with self.assertRaises(psycopg.errors.UniqueViolation):
                        async with conn.transaction():  # Savepoint protects the outer transaction.
                            await conn.execute("INSERT INTO study_values VALUES (%s)", ("O'Reilly",))
                cursor = await conn.execute("SELECT count(*) FROM study_values")
                self.assertEqual(await cursor.fetchone(), (0,))
        # Psycopg async requires a selector loop on Windows.
        if sys.platform == "win32":
            with asyncio.Runner(loop_factory=asyncio.SelectorEventLoop) as runner:
                runner.run(check())
        else:
            asyncio.run(check())

if __name__ == "__main__":
    unittest.main(verbosity=2)
