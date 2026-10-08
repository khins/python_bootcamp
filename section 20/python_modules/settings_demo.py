# Exercise 2 — Default public names
# Suppose settings_demo.py defines these names and does not define __all__:
volume = 9
subtitles = True
_debug = False
#
# Which names become available after from settings_demo import * in a fresh
# script? Explain why _debug is treated differently.
# ANSWER:
# What if we define __all__?
# Remember the lesson we just covered about __all__?
__all__ = ["volume", "subtitles", "_debug"]

volume = 9
subtitles = True
_debug = False