import unittest
from fastapi.testclient import TestClient
from catalog_api import create_app, get_store

class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.client = self.enterContext(TestClient(create_app()))
    def test_create_and_retrieve(self):
        response = self.client.post("/albums", json={"title": " Signals ", "artist": "Rush"})
        self.assertEqual(response.status_code, 201)
        record = response.json()
        self.assertEqual(record["title"], "Signals")
        self.assertEqual(self.client.get(f"/albums/{record['id']}").json(), record)
        self.assertEqual(self.client.get("/albums").json(), [record])
    def test_invalid_payload(self):
        self.assertEqual(self.client.post("/albums", json={"title": " ", "artist": "Rush"}).status_code, 422)
        self.assertEqual(self.client.post("/albums", json={"title": "Blue"}).status_code, 422)
    def test_missing_and_invalid_id(self):
        self.assertEqual(self.client.get("/albums/999").status_code, 404)
        self.assertEqual(self.client.get("/albums/not-an-int").status_code, 422)
    def test_fresh_database(self):
        self.assertEqual(self.client.get("/albums").json(), [])
    def test_dependency_override(self):
        class EmptyStore:
            def list_all(self):
                return []
        self.client.app.dependency_overrides[get_store] = lambda: EmptyStore()
        self.addCleanup(self.client.app.dependency_overrides.clear)
        self.assertEqual(self.client.get("/albums").json(), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)
