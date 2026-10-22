# ============================================================
# FILE: 06_extract-and-clean-records.py
# TOPIC: Extracting and Cleaning Records
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Normalize text and parse numeric fields.
# 2. Keep missing values distinct from real values.

def extract_records(html):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    records = []
    for card in soup.select("article.album"):
        title = card.select_one("h2")
        if title is None:
            continue  # Explicit policy: a record requires a title.
        title_text = title.get_text(" ", strip=True)
        if not title_text:
            continue
        artist = card.select_one(".artist")
        year = card.get("data-year")
        try:
            year = int(year) if year is not None else None
        except ValueError:
            year = None  # Malformed optional year stays missing.
        records.append({
            "title": title_text,
            "artist": artist.get_text(" ", strip=True) if artist else None,
            "year": year,
        })
    return records


def example_clean_records():
    html = """
    <article class="album" data-year="1981">
      <h2> Moving <em>Pictures</em> </h2><p class="artist"> Rush </p>
    </article>
    <article class="album" data-year="unknown"><h2>Blue</h2></article>
    <article class="album"><p>No title</p></article>
    """
    print(extract_records(html))
    # => [{'title': 'Moving Pictures', 'artist': 'Rush', 'year': 1981},
    #     {'title': 'Blue', 'artist': None, 'year': None}]


# example_clean_records()
# get_text(" ", strip=True) joins text fragments with a space and trims
# each fragment. It does not normalize every whitespace sequence inside
# every fragment. Use " ".join(text.split()) when that is your policy.
# None means missing; it is not the same as year 0 or an empty artist name.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Why is a missing year represented by None?
# ANSWER / CODE: ______________________________________________
# 2. Normalize repeated internal whitespace in extracted titles.
# ANSWER / CODE: ______________________________________________
# 3. Change the missing-title policy to report a rejected record count.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Define missing-data rules instead of silently inventing values.

# ============================================================
# END OF LESSON
# ============================================================

