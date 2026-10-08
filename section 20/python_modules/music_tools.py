# Optional challenge — Design a small module's public exports
# Work through this one together when you are ready.
# 1. Create music_tools.py with creator = "Kevin", _year = 2026, and a function
#    album_label(title, artist) that returns a string like "Hemispheres by Rush".
creator = "Kevin"
_year = 2026

def album_label(title, artist) -> str:
    return  f'{artist} by {title} '

# 2. Define __all__ so a star import exports only creator and album_label.
__all__ = ["creator", "album_label"]

# 3. In a separate script, use a star import for this experiment and print creator
#    and the result of calling album_label with a title and artist of your choice.


# 4. Explain why the star import does not bind _year in that script.
# 5. Replace the star import with explicit imports of the same two names.
# 6. Explain whether __all__ would prevent someone explicitly importing _year.
# Keep intentional-error demonstrations commented out.
# Write your code in the two files described above: