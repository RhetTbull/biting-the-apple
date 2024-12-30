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

- py-applescript
- macnotesapp
- photoscript

---

# Examples with code snippets

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
