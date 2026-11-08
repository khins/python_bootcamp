"""Worked descriptor project: independent, validated mutable albums."""
class NonemptyText:
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, instance, owner=None):
        return self if instance is None else getattr(instance, self.name)
    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("expected nonempty text")
        setattr(instance, self.name, value.strip())

class Album:
    title = NonemptyText()
    artist = NonemptyText()
    __hash__ = None
    def __init__(self, title, artist):
        self.title, self.artist = title, artist
    def __eq__(self, other):
        if not isinstance(other, Album):
            return NotImplemented
        return (self.title, self.artist) == (other.title, other.artist)

if __name__ == "__main__":
    first = Album(" Signals ", "Rush")
    second = Album("Blue", "Joni Mitchell")
    assert first.title == "Signals" and second.title == "Blue"
    try:
        first.title = " "
    except ValueError:
        pass
    else:
        raise AssertionError("invalid assignment was accepted")
    assert first.title == "Signals"
    print("Validation preserved the original value")
