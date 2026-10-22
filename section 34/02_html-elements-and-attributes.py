# ============================================================
# FILE: 02_html-elements-and-attributes.py
# TOPIC: HTML Elements and Attributes
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Recognize nested elements and attributes.
# 2. Parse an HTML string.

# SECTION 1 — HTML IS STRUCTURE
# <a class="album-link" href="/albums/1">Moving Pictures</a>
# a is the tag; class and href are attributes; the title is text.
# Elements can contain other elements. Indentation is not the structure.
# An id usually identifies one element; classes may describe many.
# Use an HTML parser for structure instead of regular expressions.

def example_parse_html():
    from bs4 import BeautifulSoup

    html = '<article class="album"><h2>Moving <em>Pictures</em></h2></article>'
    soup = BeautifulSoup(html, "html.parser")
    print(soup.article.name)          # => article
    print(soup.article.get("class"))  # => ['album']
    print(soup.h2.get_text(" ", strip=True))  # => Moving Pictures


# example_parse_html()
# html.parser is included with Python; Beautiful Soup is installed separately.
# Specifying the parser avoids relying on whichever parser happens to exist.

# SECTION 2 — INSPECT A FIXTURE
def example_read_fixture():
    from pathlib import Path
    from bs4 import BeautifulSoup

    path = Path(__file__).resolve().parent / "fixtures" / "catalog-page-1.html"
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    print(soup.title.get_text())  # => Practice Album Catalog
    print(len(soup.find_all("article")))  # => 2


# example_read_fixture()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Identify the tag, attributes, and text in the anchor example.
# ANSWER / CODE: ______________________________________________
# 2. Add a nested strong element to a copied HTML string and extract its text.
# ANSWER / CODE: ______________________________________________
# 3. Why is an explicit parser name useful?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Read the element structure before choosing extraction rules.

# ============================================================
# END OF LESSON
# ============================================================

