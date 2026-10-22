# ============================================================
# FILE: 04_find-and-find-all.py
# TOPIC: Finding Elements
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Use find and find_all.
# 2. Handle absent elements before reading them.

def example_find_elements():
    from bs4 import BeautifulSoup

    html = """
    <main>
      <article class="album"><h2>Signals</h2><p class="artist">Rush</p></article>
      <article class="album"><h2>Blue</h2></article>
    </main>
    """
    soup = BeautifulSoup(html, "html.parser")
    first = soup.find("h2")
    print(first.get_text(strip=True))  # => Signals
    for album in soup.find_all("article", class_="album"):
        title = album.find("h2")
        artist = album.find("p", class_="artist")
        print(title.get_text(strip=True), artist is None)
    # => Signals False
    # => Blue True
    print(soup.find("footer") is None)  # => True
    print(soup.find_all("footer"))     # => []


# example_find_elements()
# class_ avoids the Python keyword class.
# find returns one match or None. find_all returns a list-like result.
# Searching inside each article keeps each artist paired with its title.
# Independently collecting titles/artists and zip-ing them can silently
# misalign records when one article is missing a field.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. What does find return when nothing matches?
# ANSWER / CODE: ______________________________________________
# 2. Extract an artist or the text 'Unknown' for each article.
# ANSWER / CODE: ______________________________________________
# 3. Add a third article and verify that titles stay paired with artists.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Search within each record and handle missing elements explicitly.

# ============================================================
# END OF LESSON
# ============================================================

