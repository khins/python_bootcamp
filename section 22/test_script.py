from functools import wraps

def decorator(fn):
    @wraps(fn) #wraps(fn) tells Python to copy identifying metadata from fn onto wrapper.
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


@decorator
def favorite_album():
    """Return my favorite Rush album."""
    return "Hemispheres"


print(favorite_album())
print(favorite_album.__name__)
print(favorite_album.__doc__)

# @decorator is applied to favorite_album.
# @wraps(fn) is applied to the nested wrapper function.

# from functools import wraps

# def announce(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print("Starting")
#         return fn(*args, **kwargs)

#     return wrapper


# @announce
# def show_album():
#     return "Moving Pictures"


# print(show_album.__name__)
# print(show_album.__doc__)

from functools import wraps

def announce(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Starting")
        return fn(*args, **kwargs)

    return wrapper


@announce
def favorite_artist():
    """Return my favorite artist."""
    return "Rush"


print(favorite_artist.__name__)
print(favorite_artist())