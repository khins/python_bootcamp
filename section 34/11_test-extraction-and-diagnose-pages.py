# ============================================================
# FILE: 11_test-extraction-and-diagnose-pages.py
# TOPIC: Testing Extraction Offline
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Test normal and missing-field cases.
# 2. Diagnose pages populated by JavaScript.

import unittest


def titles_from_html(html):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    return [node.get_text(" ", strip=True) for node in soup.select(".album h2")]


class TestTitles(unittest.TestCase):
    def test_nested_title_text(self):
        html = '<article class="album"><h2>Moving <em>Pictures</em></h2></article>'
        self.assertEqual(titles_from_html(html), ["Moving Pictures"])

    def test_no_album_cards(self):
        self.assertEqual(titles_from_html("<p>No results</p>"), [])

    def test_missing_title(self):
        self.assertEqual(titles_from_html('<article class="album"></article>'), [])


def example_run_tests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTitles)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # => Three passing tests when Beautiful Soup is installed.


# example_run_tests()
# Tests describe extraction behavior, not whether a remote site is available.
# In an application, unexpected zero records can also trigger an alert.
# If the browser shows albums but Requests does not:
# 1. Inspect response status, final URL, and downloaded HTML.
# 2. Check that selectors match that HTML.
# 3. Look for content loaded later by JavaScript.
# Beautiful Soup will not execute a <script> to fill an empty element.
# Investigate a documented API or browser automation when appropriate.
# Login pages, redirects, and changed markup can also explain missing data.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add a test with two album titles.
# ANSWER / CODE: ______________________________________________
# 2. Write a fixture where the selector has changed and observe the test.
# ANSWER / CODE: ______________________________________________
# 3. Why should extraction tests usually avoid the live website?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Use fixtures to make parser behavior reproducible.

# ============================================================
# END OF LESSON
# ============================================================

