# ============================================================
# FILE: 09_uv-and-your-first-project.py
# TOPIC: uv — From an Empty Folder to a Working Python Project
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Terminal commands are comments: run them in PowerShell, not Python.
# Follow the numbered sections in order. Do not run this entire lesson
# expecting it to install software or create the project automatically.

# LESSON OBJECTIVES
# 1. Explain what uv manages and why developers adopt it.
# 2. Compare pip-style installation with uv's project workflow.
# 3. Build a small album-summary application from an empty folder.
# 4. Explain pyproject.toml, uv.lock, .python-version, and .venv.
# 5. Run, inspect, and reproduce a project's environment.


# ============================================================
# SECTION 1 — WHAT IS uv?
# ============================================================
# uv is a Python package and project manager from Astral, written in Rust.
# It can install Python versions, create virtual environments, resolve
# dependencies, maintain a lockfile, and run commands in an environment.
# Your application still runs on Python. uv does not replace the language.
# It also does not replace packages such as Requests or Beautiful Soup.
#
# Previously: Python + venv + pip + a requirements file.
# With uv projects: uv coordinates Python, .venv, dependencies, and runs.
# The underlying idea from lessons 01–08 remains: projects need suitable
# interpreters and isolated dependencies. uv automates much of that work.


# ============================================================
# SECTION 2 — WHY ARE PEOPLE ADOPTING IT INSTEAD OF pip?
# ============================================================
# 1. SPEED: uv emphasizes fast dependency resolution and installation,
#    using a shared cache and efficient implementation. Actual improvement
#    depends on network access, package builds, and whether caches are warm.
#    Faster installation does not make your Python application's loops faster.
# 2. ONE WORKFLOW: interpreter management, environments, dependencies, and
#    execution are available through related commands.
# 3. DEPENDENCY RECORDS: uv add records a requirement, resolves versions,
#    updates uv.lock, and synchronizes the project environment.
# 4. REPEATABLE SETUP: colleagues can use the committed lockfile to select
#    the same resolved dependency versions appropriate to their platform.
# 5. LESS ACTIVATION CONFUSION: uv run selects the project environment.
#
# pip is still a valid, widely used installer. Nobody needs to abandon a
# working pip workflow. Comparing uv projects with pip alone is not quite
# like-for-like: uv projects include work that venv and other tools perform.
# Existing team tooling or compatibility requirements may favor pip.
# uv has a pip-compatible interface, but not every pip behavior is identical.


# ============================================================
# SECTION 3 — TWO DIFFERENT uv WORKFLOWS
# ============================================================
# LOW-LEVEL, pip-LIKE WORKFLOW (for understanding; not our project steps):
# uv venv
# uv pip install requests
# uv pip install -r requirements.txt
#
# These commands manage an environment directly. uv pip install does NOT
# record project dependencies in pyproject.toml or maintain uv.lock.
# The uv pip interface does not need the pip package installed in the venv.
#
# PROJECT WORKFLOW (used below):
# uv init
# uv add rich
# uv run python main.py
#
# Use uv add for lasting project dependencies. An ad hoc uv pip install
# may be removed by a later exact uv sync if absent from project records.


# ============================================================
# SECTION 4 — INSTALL uv ON WINDOWS
# ============================================================
# First check in PowerShell:
# uv --version
#
# If uv is not installed, Astral documents this standalone installer:
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
#
# That command downloads and executes Astral's installer. The policy flag
# applies to that PowerShell process; it is not a permanent policy change.
# You can inspect the script first using:
# powershell -c "irm https://astral.sh/uv/install.ps1 | more"
#
# Follow the installer's PATH instructions, or open a new terminal, then:
# uv --version
#
# The standalone installation does not require Python to be installed first.
# Do not run every installation method you find: choose one.
# Official alternatives: https://docs.astral.sh/uv/getting-started/installation/


# ============================================================
# SECTION 5 — START FROM AN EMPTY FOLDER
# ============================================================
# Start PowerShell in your python_bootcamp repository root.
# Use a new folder name if uv-album-demo already contains work.
# These commands create a separate project with its OWN .venv; it does
# not use the shared root environment from the earlier lessons.
#
# New-Item -ItemType Directory -Path "section 33/uv-album-demo"
# Set-Location "section 33/uv-album-demo"
# uv init --app --python 3.13 --vcs none
# uv add rich
#
# 3.13 is an explicit teaching choice, not a claim about the newest Python.
# uv can download a suitable interpreter if one is unavailable, subject to
# its download settings and network access. Exact patch versions can vary.
# --app selects an application project; --vcs none avoids initializing a
# nested Git repository inside this bootcamp repository.
# rich is a third-party library for formatted terminal output.
# uv add installs it and its required dependencies into this project's venv.
#
# AFTER INITIALIZATION AND ADDING rich, inspect these files:
# main.py           application source; replace its starter code below
# pyproject.toml    project metadata, supported Python range, dependencies
# uv.lock           resolved versions and package/source information
# .python-version   local interpreter preference created by initialization
# .venv/            generated project environment
# README.md         project documentation
#
# .python-version and requires-python have different jobs. The first selects
# a local interpreter preference; the second declares supported Python.
# A minor-version preference does not pin the exact interpreter patch.


# ============================================================
# SECTION 6 — WRITE THE SMALL APPLICATION
# ============================================================
# Open main.py INSIDE uv-album-demo. Replace its starter contents with
# the Python code below, beginning at 'from rich.console import Console'
# and ending after the indented 'main()'. Do not copy the quote delimiters.
# This string keeps the project code readable without importing rich when
# you run this lesson file outside the new project's environment.

PROJECT_CODE = '''from rich.console import Console
from rich.table import Table


def summarize(albums):
    count = len(albums)
    total_minutes = sum(album["minutes"] for album in albums)
    return count, total_minutes


def main():
    # Synthetic durations for practice, not factual album running times.
    albums = [
        {"title": "Signals", "artist": "Rush", "minutes": 42},
        {"title": "Blue", "artist": "Joni Mitchell", "minutes": 36},
        {"title": "Kind of Blue", "artist": "Miles Davis", "minutes": 46},
    ]
    table = Table(title="My Album Library")
    table.add_column("Album")
    table.add_column("Artist")
    table.add_column("Minutes", justify="right")
    for album in albums:
        table.add_row(album["title"], album["artist"], str(album["minutes"]))
    count, total_minutes = summarize(albums)
    console = Console()
    console.print(table)
    console.print(f"Albums: {count} | Total minutes: {total_minutes}")


if __name__ == "__main__":
    main()
'''


def example_show_project_code():
    print(PROJECT_CODE)
    # Prints the complete main.py source. It does not run or save it.


# example_show_project_code()


# ============================================================
# SECTION 7 — RUN AND VERIFY
# ============================================================
# Still inside uv-album-demo:
# uv run python main.py
#
# EXPECTED RESULT:
# A table titled My Album Library with three rows, followed by:
# Albums: 3 | Total minutes: 124
# Border characters, color, and width can vary with your terminal.
# The application uses local data; it makes no web requests.
# Setup/package downloads can require internet access.
#
# Inspect the interpreter and dependencies:
# uv run python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
# Expected: this project's .venv interpreter path, then True.
# uv tree
# Expected: rich and its dependency tree; exact versions can vary initially.
#
# Check the calculation independently of terminal formatting:
# uv run python -c "from main import summarize; assert summarize([]) == (0, 0); assert summarize([{'minutes': 42}, {'minutes': 36}, {'minutes': 46}]) == (3, 124); print('Checks passed')"
# Expected: Checks passed
# Importing main does not print the table because of its __name__ guard.
#
# uv run checks project/lockfile/environment consistency before execution.
# It can update the lockfile when requirements change. No manual activation
# is necessary. In your IDE, select uv-album-demo/.venv/Scripts/python.exe
# if you want the IDE Run button to use this same environment.


# ============================================================
# SECTION 8 — SHARE AND RECREATE THE PROJECT
# ============================================================
# Keep main.py, pyproject.toml, uv.lock, .python-version, and README.md.
# Add .venv/ and __pycache__/ to the project's .gitignore if needed.
# --vcs none did not set up Git ignore rules for you.
# Do not commit the generated .venv directory. Do not hand-edit uv.lock.
#
# On another machine or in a new folder containing the project files:
# uv sync --locked
# uv run --locked python main.py
#
# sync creates/updates .venv from the project's dependency records.
# --locked fails if uv.lock is missing or needs updating; it prevents an
# unnoticed re-resolution. Keep pyproject.toml and uv.lock together.
# uv sync normally removes packages not selected by the project records.
# uv run normally retains extra packages; do not equate its default sync
# behavior with an exact uv sync.
# A lockfile does not supply your OS or guarantee availability of every
# external system library. Python/platform requirements still matter.


# ============================================================
# SECTION 9 — EVERYDAY COMMANDS AND COMMON CONFUSION
# ============================================================
# uv add requests                 record/install another project dependency
# uv remove requests              remove that requirement and synchronize
# uv add --dev pytest             record a development-only dependency
# uv lock --upgrade-package rich  deliberately refresh rich's resolution
# uv sync                        install the selected locked dependencies
# uv run python main.py          run in the project's environment
#
# These are optional examples, not additional steps required for this demo.
# Locking updates resolution; syncing installs the selected result.
# Adding pytest does not create tests automatically.
#
# 'uv is not recognized': check installation/PATH and open a new terminal.
# 'No module named rich': verify you are in the new project directory and
# using uv run, or that your IDE points to the new project's interpreter.
# --locked reports a stale lock: review your intended dependency changes,
# run uv lock to update resolution, then uv sync to update the environment.
# Do not blindly discard the lockfile whenever an installation fails.


# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Explain why uv is more than a faster spelling of pip install.
# ANSWER: ____________________________________________________
# 2. What does uv add record that uv pip install does not?
# ANSWER: ____________________________________________________
# 3. Add a fourth album, predict the new total, and run the program.
# YOUR CODE: __________________________________________________
# 4. Extend summarize to return the longest album, handling empty input.
# YOUR CODE: __________________________________________________
# 5. Copy only the source/configuration files into a new empty directory,
#    run uv sync --locked, and verify that the same application runs.
# NOTES: ______________________________________________________
# 6. Why is .venv excluded from Git while uv.lock is included?
# ANSWER: ____________________________________________________
# 7. Does faster package installation speed up summarize itself? Why?
# ANSWER: ____________________________________________________
# KEY TAKEAWAY: uv coordinates Python, dependencies, environments, and runs;
# the project records let you recreate the setup instead of copying .venv.

# REFERENCES — official documentation checked for this lesson:
# https://docs.astral.sh/uv/
# https://docs.astral.sh/uv/getting-started/installation/
# https://docs.astral.sh/uv/guides/projects/
# https://docs.astral.sh/uv/concepts/projects/sync/
# https://docs.astral.sh/uv/reference/cli/

# ============================================================
# END OF LESSON
# ============================================================
