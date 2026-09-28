# A Login Decorator from the Flask Tutorial — Study Summary
# Instructor summary:
# - A decorator can check a condition before allowing the original function to run.
# - A login-required wrapper checks whether a current user is available.
# - For an anonymous visitor, it returns a redirect instead of calling the view.
# - For a logged-in user, it calls the view and returns the view's result.
# - functools.wraps preserves the original view's name and documentation.
# - Keyword arguments are collected by the wrapper and forwarded to the view.
# - Reusing the decorator avoids repeating the same check in several views.
#
# Clarifications and connections:
# - This is application code from Flask's tutorial, not a built-in Flask decorator.
# - The tutorial's request setup assigns g.user before the protected view runs.
# - g is context-local storage, not a single shared user variable for all visitors.
# - A redirect is a response directing the browser elsewhere, not a direct call
#   to the login view. The early return prevents the protected view from running.
# - Being logged in does not establish ownership of a post. Update and delete
#   operations need separate permission checks.
# - A view returns a response or a value Flask can convert into a response;
#   it need not always render an HTML page.
# - The simulation below illustrates control flow only, not a real login system.
#
# Official references for the framework examples:
# https://flask.palletsprojects.com/en/stable/tutorial/views/
# https://flask.palletsprojects.com/en/stable/tutorial/blog/
# https://flask.palletsprojects.com/en/stable/patterns/viewdecorators/

from functools import wraps


# --- 1. Recognize the Flask pattern ---
# This commented example belongs in an application with Flask configured,
# an auth.login endpoint, and request setup that assigns g.user:
# from flask import g, redirect, url_for
#
# def login_required(view):
#     @wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for("auth.login"))
#         return view(**kwargs)
#     return wrapped_view
#
# The early return and the view call are alternative paths. Anonymous visitors
# do not proceed to view(**kwargs). The wrapper reads user state on each call.
# This version accepts keyword arguments, as used by the tutorial's routes.
# A general-purpose wrapper can accept and forward both *args and **kwargs.


# --- 2. Simulate the decision with ordinary Python ---
# In this teaching example, the caller explicitly supplies a user argument.
# In a real application, identity must come from trusted authentication handling.
# A dictionary returned below represents a simulated redirect, not an HTTP response.

def require_demo_user(view):
    @wraps(view)
    def wrapper(user, *args, **kwargs):
        if user is None:
            return {"redirect": "/login"}
        return view(user, *args, **kwargs)

    return wrapper


@require_demo_user
def create_post(user, title):
    """Return a simulated new post for the supplied user."""
    print("Creating post")
    return {"author": user["name"], "title": title}


print(create_post(None, title="My first post"))
# Expected: {'redirect': '/login'}
# "Creating post" does not print: the original function was never called.

print(create_post({"name": "Kevin"}, title="My first post"))
# Expected:
# Creating post
# {'author': 'Kevin', 'title': 'My first post'}
# The wrapper returns the original function's dictionary unchanged.


# --- 3. Reuse the same decision for another function ---
@require_demo_user
def show_draft(user, post_id):
    """Return a simulated draft description."""
    return f"Draft {post_id} for {user['name']}"


print(show_draft(None, post_id=7))  # {'redirect': '/login'}
print(show_draft({"name": "Kevin"}, post_id=7))  # Draft 7 for Kevin
# These demonstrations do not store, update, or delete actual posts.
# Real record access must also enforce any applicable ownership or permissions.


# --- 4. Preserve metadata and arguments ---
print(show_draft.__name__)  # show_draft
print(show_draft.__doc__)  # Return a simulated draft description.
print(show_draft({"name": "Alex"}, 8))  # Draft 8 for Alex
# wrapper receives user separately; the remaining positional values form args
# and the remaining keyword values form kwargs. It forwards all three parts.
# wraps does not perform the check or forwarding; the wrapper body does that.


# --- 5. Apply a check before route registration ---
# In a Flask application, the route decorator normally goes above the check:
# @bp.route("/create", methods=("GET", "POST"))
# @login_required
# def create():
#     ...
#
# Decorators apply bottom-up: login_required wraps create, then the route
# decorator registers that wrapped view. This ensures routed requests use the check.
# This snippet is illustrative and is not a complete application.


# --- 6. Understand both return levels ---
# return wrapper: the decorator supplies the replacement function during decoration.
# return {"redirect": "/login"}: the simulation stops an anonymous call early.
# return view(...): the allowed path preserves the original function's result.
#
# Simply constructing a redirect without returning it would not prevent later
# code from running. The early return is what stops execution of this wrapper.
# The wrapper does not need to call the original view on every path.


# --- 7. Practice: predict, explain, then run ---
# Use the plain-Python examples above; no Flask installation is needed.
# Write predictions in ANSWER comments before uncommenting each exercise.

# Exercise 1 — An anonymous visitor
# Predict the output. Does "Creating post" appear? Explain why.
# print(create_post(None, title="Album review"))
# ANSWER:


# Exercise 2 — An allowed call
# Predict every output line in order.
# print(create_post({"name": "Alex"}, title="Album review"))
# Which return statement in the wrapper supplies the caller's value?
# ANSWER:


# Exercise 3 — Forward the arguments
# Predict both outputs and explain where post_id is collected in each call.
# print(show_draft({"name": "Kevin"}, 12))
# print(show_draft({"name": "Kevin"}, post_id=12))
# ANSWER:


# Exercise 4 — Preserve documentation
# Predict the output. Does inspecting this attribute call show_draft's body?
# print(show_draft.__name__)
# Which decorator makes the name show_draft rather than wrapper?
# ANSWER:


# Exercise 5 — Login versus permission
# A user is logged in, but a post belongs to somebody else.
# Does passing the login check alone establish permission to delete it?
# Explain the separate question an ownership check must answer.
# ANSWER:


# Exercise 6 — Write another protected simulation
# 1. Define view_profile(user) to return "Profile for Kevin" for a matching user.
# 2. Apply @require_demo_user to it and give it a docstring.
# 3. Call it with None and then {"name": "Kevin"}; print both results.
# 4. Predict both outputs and explain why the anonymous path skips the body.
# 5. Print view_profile.__doc__ to check its preserved documentation.
# Write your code below:


# Optional challenge — Add an ownership check to a simulated edit
# Work through this one together when you are ready.
# Define edit_post(user, post, new_title), decorated with @require_demo_user.
# user contains "id" and "name"; post contains "author_id" and "title".
# Inside the original function, compare user["id"] with post["author_id"].
# If they differ, return "Permission denied".
# If they match, make a COPY of post, replace the copy's title, and return it.
# Test three cases: anonymous user, logged-in non-owner, and logged-in owner.
# Print each returned value and verify the original post dictionary is unchanged.
# Explain which check belongs to the decorator, which belongs to the function,
# and which paths actually execute edit_post's original body.
# This is a data-only exercise, not a production authorization implementation.
# Write your code below:
