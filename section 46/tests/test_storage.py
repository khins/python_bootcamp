import pytest
from bootcamp_catalog.storage import load, save

def test_round_trip(tmp_path, album):
    path = tmp_path / "catalog.json"
    save(path, [album])
    assert load(path) == [album]
    assert list(tmp_path.glob(".catalog-*.tmp")) == []

def test_missing_is_empty_without_creating_file(tmp_path):
    path = tmp_path / "missing.json"
    assert load(path) == []
    assert not path.exists()

def test_bad_save_preserves_existing_file(tmp_path, album):
    path = tmp_path / "catalog.json"
    save(path, [album])
    before = path.read_bytes()
    with pytest.raises(ValueError):
        save(path, [{"title": "Bad"}])
    assert path.read_bytes() == before

def test_replace_failure_cleans_temporary_file(tmp_path, monkeypatch, album):
    path = tmp_path / "catalog.json"
    save(path, [album])
    before = path.read_bytes()
    def fail_replace(*args):
        raise OSError("simulated replace failure")
    monkeypatch.setattr("bootcamp_catalog.storage.os.replace", fail_replace)
    with pytest.raises(OSError, match="simulated"):
        save(path, [album])
    assert path.read_bytes() == before
    assert list(tmp_path.glob(".catalog-*.tmp")) == []
