import pytest
from bootcamp_catalog.core import add_record, labels, validate_catalog

def test_labels(album):
    assert labels([album]) == ["Signals by Rush (1982)"]

def test_empty():
    assert labels([]) == []

@pytest.mark.parametrize("year", [True, "1982", 1799, 2101, None])
def test_invalid_year(year):
    with pytest.raises(ValueError, match="year"):
        add_record([], "Signals", "Rush", year)

def test_add_does_not_mutate_input(album):
    rows = [album]
    result = add_record(rows, "Blue", "Joni Mitchell", 1971)
    assert rows == [album]
    assert len(result) == 2
    result[0]["title"] = "Changed"
    assert album["title"] == "Signals"

def test_duplicate_is_case_insensitive(album):
    with pytest.raises(ValueError, match="duplicate"):
        add_record([album], " signals ", "RUSH", 1982)

@pytest.mark.parametrize("value", [None, {}, [None], [{"title": "", "artist": "Rush", "year": 1982}]])
def test_bad_shape(value):
    with pytest.raises(ValueError):
        validate_catalog(value)
