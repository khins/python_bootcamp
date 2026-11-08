"""Two adapters with the same contract; SQLite stays in memory."""
import sqlite3
from typing import Protocol

class Store(Protocol):
    def save(self, key: str, title: str) -> None: ...
    def load(self, key: str) -> str | None: ...

class MemoryStore:
    def __init__(self):
        self.data = {}
    def save(self, key, title):
        self.data[key] = title
    def load(self, key):
        return self.data.get(key)

class SQLiteStore:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute("CREATE TABLE albums (id TEXT PRIMARY KEY, title TEXT NOT NULL)")
    def save(self, key, title):
        with self.connection:
            self.connection.execute(
                "INSERT INTO albums VALUES (?, ?) ON CONFLICT(id) DO UPDATE SET title=excluded.title",
                (key, title))
    def load(self, key):
        row = self.connection.execute("SELECT title FROM albums WHERE id=?", (key,)).fetchone()
        return None if row is None else row[0]
    def close(self):
        self.connection.close()

def contract(store: Store):
    assert store.load("missing") is None
    store.save("1", "Blue")
    assert store.load("1") == "Blue"
    store.save("1", "Signals")
    assert store.load("1") == "Signals"

if __name__ == "__main__":
    contract(MemoryStore())
    database = SQLiteStore()
    try:
        contract(database)
    finally:
        database.close()
    print("Both adapters satisfy the exercised contract")
