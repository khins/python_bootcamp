# ============================================================
# FILE: 11_what-patch-patches.py
# TOPIC: Patch Where the Name Is Looked Up
# ============================================================
# STUDY GUIDE
# Predict before running, then run this file directly with Python.
# Complete the exercises and challenges. No live services are used.

import unittest
from unittest.mock import Mock, MagicMock, call, create_autospec, patch


# LESSON OBJECTIVES
# 1. Distinguish an object's definition from references to it.
# 2. Explain why patching the original provider can have no effect.
# 3. Patch the namespace used by the code under test.

from types import SimpleNamespace


def original_fetch():
    return "original"


# These namespaces simulate two import styles without requiring extra
# package files. The objects and references are real Python objects.
provider = SimpleNamespace(fetch=original_fetch)

# Similar to: from provider import fetch
imported_fetch = provider.fetch


def use_imported_name():
    return imported_fetch()


# Similar to: import provider; provider.fetch()
def use_provider_attribute():
    return provider.fetch()


# ============================================================
# SECTION 1 — PATCHING THE PROVIDER DOES NOT REBIND A COPIED NAME
# ============================================================
class TestLookupLocation(unittest.TestCase):
    def test_provider_patch_only_affects_provider_lookup(self):
        with patch.object(provider, "fetch", return_value="replacement") as mocked:
            self.assertEqual(use_imported_name(), "original")
            mocked.assert_not_called()
            self.assertEqual(use_provider_attribute(), "replacement")
            mocked.assert_called_once_with()

    def test_patch_the_name_used_by_importing_code(self):
        with patch(f"{__name__}.imported_fetch", return_value="replacement") as mocked:
            self.assertEqual(use_imported_name(), "replacement")
            self.assertEqual(use_provider_attribute(), "original")
            mocked.assert_called_once_with()

    def test_direct_alias_is_not_rewritten(self):
        saved_reference = provider.fetch
        with patch.object(provider, "fetch", return_value="replacement"):
            self.assertEqual(saved_reference(), "original")
            self.assertEqual(provider.fetch(), "replacement")


# ============================================================
# SECTION 2 — APPLY THE RULE TO REAL MODULES
# ============================================================
# Suppose app/reports.py contains:
#     from app.gateway import fetch
#     def report():
#         return fetch()
# Patch "app.reports.fetch", because report looks up fetch there.
#
# If reports.py instead contains:
#     import app.gateway
#     def report():
#         return app.gateway.fetch()
# Patch "app.gateway.fetch", the attribute looked up at call time.
# patch.object(existing_object, "attribute") applies the same principle
# using an object reference instead of a dotted target string.


# ============================================================
# SECTION 3 — SAVED REFERENCES AND DEFAULT ARGUMENTS
# ============================================================
# patch replaces a name/attribute; it does not rewrite function bodies,
# previously saved aliases, closure references, or bound default values.
# For def run(fetch=provider.fetch), the default is captured when the
# function is defined. Patching provider.fetch later does not change it.
# Prefer explicit dependency injection when a captured dependency would
# otherwise make testing awkward. Do not use create=True to conceal a
# misspelled target: a newly created attribute may never be used.
# Patching shared objects can affect other code using the same attribute
# while the patch is active. Keep scopes narrow and restore reliably.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: A module has 'from library import send as deliver'.
# Its function calls deliver(). Which name must you patch?
# ANSWER: ____________________________________________________
# CHALLENGE: Add a function with imported_fetch as a default argument.
# Demonstrate that patching the module name does not replace the saved
# default. Then explicitly pass a Mock and verify that it is used.
# Write your code here:
#
# 1. Does patch change every reference to the same object? ______
# 2. Why did the provider patch miss use_imported_name()? _______
# 3. What question identifies the correct target? ______________
# KEY TAKEAWAY: Patch the name your code actually resolves when it
# runs, not automatically the place where the object was defined.

if __name__ == "__main__":
    unittest.main(verbosity=2)

# ============================================================
# END OF LESSON
# ============================================================

