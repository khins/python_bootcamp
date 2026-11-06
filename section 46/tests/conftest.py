import pytest

@pytest.fixture
def album():
    return {"title": "Signals", "artist": "Rush", "year": 1982}
