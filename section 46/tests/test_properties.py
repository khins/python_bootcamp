from hypothesis import given, strategies as st
from bootcamp_catalog.core import validate_record

# Generate meaningful valid strings, then test a normalization invariant.
# This is additional evidence, not a proof for every possible input.
@given(title=st.text(alphabet="abcdefghijklmnopqrstuvwxyz ", min_size=1).filter(lambda s: bool(s.strip())),
       year=st.integers(min_value=1800, max_value=2100))
def test_normalization_is_idempotent(title, year):
    record = {"title": title, "artist": " Demo Band ", "year": year}
    normalized = validate_record(record)
    assert validate_record(normalized) == normalized
    assert normalized["title"] == title.strip()
    assert record["artist"] == " Demo Band "
