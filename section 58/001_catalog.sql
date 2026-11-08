-- Apply once, explicitly, to your own study database using psql -v ON_ERROR_STOP=1.
-- This is a versioned migration, not startup code or a request handler.
BEGIN;
CREATE TABLE artists (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE CHECK (length(trim(name)) > 0)
);
CREATE TABLE albums (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL CHECK (length(trim(title)) > 0),
    artist_id BIGINT NOT NULL REFERENCES artists(id),
    UNIQUE (artist_id, title)
);
CREATE INDEX albums_artist_id_idx ON albums(artist_id);
CREATE TABLE study_schema_versions (
    version INTEGER PRIMARY KEY,
    applied_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO study_schema_versions(version) VALUES (1);
COMMIT;
