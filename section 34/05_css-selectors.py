# ============================================================
# FILE: 05_css-selectors.py
# TOPIC: Selecting Elements with CSS
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Use select and select_one.
# 2. Choose selectors based on meaningful structure.

def example_css_selectors():
    from bs4 import BeautifulSoup

    html = """
    <main id="catalog">
      <article class="album featured"><h2><a href="/one">Signals</a></h2></article>
      <article class="album"><h2><a href="/two">Blue</a></h2></article>
    </main>
    """
    soup = BeautifulSoup(html, "html.parser")
    print(len(soup.select("#catalog .album")))  # => 2
    print(soup.select_one(".featured h2").get_text())  # => Signals
    for link in soup.select("article.album > h2 > a[href]"):
        print(link["href"])
    # => /one
    # => /two
    print(soup.select_one(".price") is None)  # => True


# example_css_selectors()
# .album means a class; #catalog means an id; [href] requires an attribute.
# A space selects descendants; > selects direct children.
# select returns a list; select_one returns a tag or None.
# Prefer meaningful selectors over long chains of nth-child positions.
# Selectors describe the current HTML; redesigns can invalidate them.
# REFERENCE: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Explain the difference between '.album h2' and '.album > h2'.
# ANSWER / CODE: ______________________________________________
# 2. Select only the featured album's link.
# ANSWER / CODE: ______________________________________________
# 3. What should your code do if select_one returns None?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Choose understandable selectors and check their results.

# ============================================================
# END OF LESSON
# ============================================================

