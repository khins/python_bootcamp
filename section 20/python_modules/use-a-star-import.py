# 3. In a separate script, use a star import for this experiment and print creator
#    and the result of calling album_label with a title and artist of your choice.
from music_tools import *

print(creator)

print(album_label("Hemispheres", "Rush"))
print(album_label("Yes", "Subway Walls"))

import music_tools
print(music_tools._year)

from music_tools import _year
print(_year)