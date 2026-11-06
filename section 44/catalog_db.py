"""Small SQLite catalog. Explicit transaction examples use legacy isolation mode."""
import sqlite3

def connect(path=":memory:"):
    connection = sqlite3.connect(path, isolation_level="DEFERRED")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def create_schema(connection):
    connection.executescript("""
        CREATE TABLE artists (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
        CREATE TABLE albums (
            id INTEGER PRIMARY KEY,
            artist_id INTEGER NOT NULL REFERENCES artists(id),
            title TEXT NOT NULL,
            year INTEGER NOT NULL CHECK(year BETWEEN 1800 AND 2100),
            UNIQUE(artist_id, title)
        );
        CREATE INDEX albums_year_idx ON albums(year);
    """)

def add_album(connection, artist, title, year):
    if not isinstance(artist, str) or not artist.strip() or not isinstance(title, str) or not title.strip():
        raise ValueError("artist and title are required")
    if type(year) is not int or not 1800 <= year <= 2100:
        raise ValueError("invalid year")
    artist, title = artist.strip(), title.strip()
    connection.execute("INSERT INTO artists(name) VALUES (?) ON CONFLICT(name) DO NOTHING", (artist,))
    artist_id = connection.execute("SELECT id FROM artists WHERE name = ?", (artist,)).fetchone()[0]
    cursor = connection.execute("INSERT INTO albums(artist_id, title, year) VALUES (?, ?, ?)",
                                (artist_id, title, year))
    return cursor.lastrowid

def list_albums(connection):
    return connection.execute("""
        SELECT artists.name, albums.title, albums.year
        FROM albums JOIN artists ON albums.artist_id = artists.id
        ORDER BY albums.year, albums.title
    """).fetchall()
