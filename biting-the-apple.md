---
theme: default
marp: true
---

<style>
/* Adjust text size on slide */
section.small-text h2 {
  font-size: 0.85em !important;
}

section.small-text h3 {
  font-size: 0.85em !important;
}

section.small-text p, section.small-text li, section.small-text b {
  font-size: 0.85em; /* Shrink regular text */
}

/* To use this, add <!-- _class: "invert small-text" --> before the slide you want to use it on*/
</style>

<!--
_backgroundColor: black
_color: white
-->

<!-- class: invert -->

# Biting the Apple

## Unlocking macOS with Python

![bg](images/cover.jpg)

---

<!--
paginate: true
footer: "Biting the Apple: Unlocking macOS with Python"
-->

# About Me

![bg right:50%](images/TRS80-Model-III.png)

- Hobbyist programmer
- First code in Tandy BASIC on a TRS-80 Model III
- Reformed Perl hacker
- Pythonista since 2018
- [github.com/RhetTbull](https://github.com/RhetTbull)

---

# Installing Python on macOS

- [Homebrew](https://brew.sh): [Homebrew Python is Not For You](https://justinmayer.com/posts/homebrew-python-is-not-for-you/)

- [Conda](https://docs.conda.io/projects/conda/en/latest/index.html)

- [Python.org](https://www.python.org/downloads/)

- [uv](https://docs.astral.sh/uv/): `uv python install 3.13`

## <span style="text-align: center; display: block;">Just use uv or python.org</span>

---

# Automating Mac Apps

![bg vertical right:33% 90%](images/new-note-scripteditor.png)
![bg 100%](images/new-note-screenshot.png)

Many Mac apps are scriptable using [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_fundamentals.html)

```applescript
tell application "Notes"
	activate

	set noteTitle to "Hello World"
	set noteBody to "This is my note."

	tell account "iCloud"
		set newNote to make new note at folder "Notes" with properties
		          {name:noteTitle, body:noteBody}
	end tell
end tell
```

---

# Isn't This Talk Supposed To Be About Python?

`pip install py-applescript`

```python
import applescript

def create_note(title: str, body: str) -> str:
    """Create a new note in Notes.app"""
    script = """
    on createNote(noteTitle, noteBody)
        tell application "Notes"
            activate

            tell account "iCloud"
                set newNote to make new note at folder "Notes" with properties {name:noteTitle, body:noteBody}
                return id of newNote
            end tell
        end tell
    end createNote
    """
    ascript = applescript.AppleScript(script)
    return str(ascript.call("createNote", title, body))

note_id = create_note("Hello World", "This is my note.")
print(f"New note created with id {note_id}")
```

---

# There's a Package For That!

`pip install macnotesapp`

```python
import macnotesapp

new_note = macnotesapp.NotesApp().make_note("Hello World", "This is my note.")
print(f"New note created with ID {new_note}")
```

`pip install photoscript`

```python
import photoscript

for photo in photoscript.PhotosLibrary().selection:
    photo.keywords += ["Travel"]
```
---

# PyXA: Python for Automation

`pip install mac-pyxa` (Doesn't work yet with Python 3.13)

<!-- Supports most Apple Mac apps and some 3rd party apps. -->

```python
from datetime import datetime
import PyXA

def create_reminder(name, due_date=None):
    """Creates a new reminder in the Mac Reminders app's default list."""
    try:
        reminders_app = PyXA.Application("Reminders")
        due_date = datetime.fromisoformat(due_date) if due_date else None
        reminder = reminders_app.new_reminder(name=name, due_date=due_date)
        print(f"Reminder '{name}' created successfully.")
    except Exception as e:
        print(f"Failed to create reminder: {e}")

create_reminder("Finish HSV.py talk", due_date="2025-02-01T17:00:00")
```

---

# Accessing Native APIs

- PyObjC
- Rubicon

---

# PyObjc Overview

---

# PyObjc Examples

- Speech, vision, camera, convert heic to jpeg
- use ChatGPT Objc -> Python

---

# Add a GUI

- Rumps
- others

---

# Creating a Standalone App

- PyInstaller
- Py2App
- PyApp
- Briefcase

---

# Permissions & Entitlements

- disclaim.py
- Locationator example

---

# Questions?

- Link to slides
