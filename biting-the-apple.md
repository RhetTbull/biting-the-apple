---
theme: default
marp: true
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }

  section.small-text h2 {
    font-size: 0.75em !important;
  }

  section.small-text h3 {
    font-size: 0.75em !important;
  }

  section.small-text p, section.small-text li, section.small-text b {
    font-size: 0.75em; /* Shrink regular text */
  }
---

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

![bg right:40% 70%](images/presentation-qr.png)

This presentation:
[https://rhettbull.github.io/biting-the-apple/](https://rhettbull.github.io/biting-the-apple/)

Source:
[https://github.com/RhetTbull/biting-the-apple](https://github.com/RhetTbull/biting-the-apple)

---

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
import datetime
import PyXA

reminders_app = PyXA.Application("Reminders")
reminders_app.new_reminder(
    name="Finish HSV.py talk", due_date=datetime.datetime(2025, 2, 10)
)
```

---

# Beyond Scripting: Accessing the Power of Native APIs

![bg right contain](images/AVSpeechSynthesizer.png)

Apple provides useful APIs in Objective-C and Swift that enable features like extracting text from images, speech synthesis, accessing the Mac's camera, etc.

Can we use these from Python?

---

# Yes! Python to Objective-C Bridge

## [PyObjC](https://pyobjc.readthedocs.io/en/latest/)

Appears to have at least tacit blessing from Apple. Stable, offers support for most macOS APIs. Does not support iOS.

## [Rubicon](https://rubicon-objc.readthedocs.io/en/stable/)

Part of the [BeeWare](https://beeware.org) project. Supported by [Anaconda](https://www.anaconda.com). Supports both macOS and iOS.

---

<!-- _class: "invert small-text" -->
# Simple PyObjC Example

![bg right:40% contain](images/copyItemAtPath.png)

Use native [copy-on-write for APFS](https://eclecticlight.co/2020/04/14/copy-move-and-clone-files-in-apfs-a-primer/) file systems.

- Python's native [file copy functions](https://docs.python.org/3/library/shutil.html) cannot take advantage of copy-on-write; also do not copy all metadata.
- Apple's [NSFileManager](https://developer.apple.com/documentation/foundation/nsfilemanager) provides [copyItemAtPath:toPath:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1407903-copyitematpath) method that does use copy-on-write

Python implementation:

```python
import Foundation

def copyfile(src: str, dest: str):
    """Copy file from src to dest using NSFileManager"""
    filemgr = Foundation.NSFileManager.defaultManager()
    success, error = filemgr.copyItemAtPath_toPath_error_(src, dest, None)
    if not success:
        raise OSError(error)
```

---
<!-- _class: "invert small-text" -->
# Speech Synthesis Example

```python
import AVFoundation
from Foundation import NSObject
from PyObjCTools.AppHelper import runEventLoop, stopEventLoop

class SpeechSynthesizerDelegate(NSObject):
    def speechSynthesizer_didFinishSpeechUtterance_(self, synthesizer, utterance):
        stopEventLoop()

def speak_string(text: str) -> None:
    synthesizer = AVFoundation.AVSpeechSynthesizer.alloc().init()
    utterance = AVFoundation.AVSpeechUtterance.speechUtteranceWithString_(text)
    voice = AVFoundation.AVSpeechSynthesisVoice.voiceWithLanguage_("en-US")
    utterance.setVoice_(voice)
    delegate = SpeechSynthesizerDelegate.alloc().init()
    synthesizer.setDelegate_(delegate)
    synthesizer.speakUtterance_(utterance)
    runEventLoop()
```

---
<!-- _class: "invert small-text" -->
# Status Bar Apps

![bg vertical right:30% contain](images/rumps-menu.png)
![bg contain](images/rumps-alert.png)

[Rumps: Ridiculously Uncomplicated macOS Python Statusbar](https://github.com/jaredks/rumps)

```python
import rumps

class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("Check button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hello")
    def sayhello(self, _):
        rumps.alert("Hello", "Hello HSV.py!", "Goodbye")

if __name__ == "__main__":
    AwesomeStatusBarApp("Awesome App").run()
```

<!--
Good for:
- Notification-center-based app
- Controlling daemons / launching separate programs
- Updating simple info from web APIs on a timer

Not good for:
- Any app that is first and foremost a GUI application
-->

---
<!-- _class: "invert small-text" -->
# What about a GUI?

![bg contain left:40%](images/appkitgui.png)

## That's a whole other talk

- Most Python GUI frameworks work fine with macOS
- [Tkinter](https://docs.python.org/3/library/tkinter.html): Ships with Python standard library
- [Toga](https://beeware.org/project/projects/libraries/toga/): From BeeWare, native widgets, early development
- [AppKitGUI](https://github.com/RhetTbull/appkitgui): My own mini-framework, shows how to use [AppKit](https://developer.apple.com/documentation/appkit) from Python

---

# Creating a Standalone App

![bg vertical contain right:40%](images/applecrate.png)
![bg contain](images/textinator-installer.png)

- [PyInstaller](https://pyinstaller.org/en/stable/): Good for command line tools
- [Py2App](https://py2app.readthedocs.io/en/latest/): Standalone Mac apps (like [py2exe](https://pypi.org/project/py2exe/) but for macOS)
- [PyApp](https://github.com/ofek/pyapp): Self-bootstrapping apps with self-update, very fast, written in Rust
- [Briefcase](https://briefcase.readthedocs.io/en/stable/): From BeeWare, similar to Py2App
- [AppleCrate](https://github.com/RhetTbull/applecrate): Create installers for your app

---

# Permissions & Entitlements
<!-- _class: "invert small-text" -->

![bg vertical contain left:40%](images/ghostty-permission-reminders.png)
![bg contain](images/textinator_desktop_access.png)

## macOS has a ~~naggy~~ robust security model

- Certain features require user approval
- [Entitlements](https://developer.apple.com/documentation/bundleresources/entitlements): executable permission to use a technology / service
- Permissions: control run-time access to sensitive user data (e.g. location, files)

### Command line apps: the Terminal app is responsible for requesting permission.

### GUI apps: the application is responsible for requesting permission.

---
<!-- _class: "invert small-text" -->
# Resources

<div class="columns">
<div>

## Automation

- [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_fundamentals.html): Apple's scripting language
- [macnotesapp](https://github.com/RhetTbull/macnotesapp): Automate Apple Notes
- [PhotoScript](https://github.com/RhetTbull/PhotoScript): Automate Apple Photos
- [PyXA](https://github.com/SKaplanOfficial/PyXA): Python for automation

## Native APIs

- [PyObjC](https://pyobjc.readthedocs.io/en/latest/): Python to Objective-C bridge
- [Rubicon](https://rubicon-objc.readthedocs.io/en/stable/): Alternate Python to Objective-C bridge
- [Rumps](https://github.com/jaredks/rumps): macOS statusbar apps

</div>

<div>

## GUIs

- [Tkinter](https://docs.python.org/3/library/tkinter.html): Standard library
- [Toga](https://beeware.org/project/projects/libraries/toga/): Native widgets
- [AppKitGUI](https://github.com/RhetTbull/appkitgui): My own macOS native mini-framework

## Installers / App Packaging

- [PyInstaller](https://pyinstaller.org/en/stable/): Good for command line tools
- [Py2App](https://py2app.readthedocs.io/en/latest/): Standalone Mac apps
- [PyApp](https://github.com/ofek/pyapp): Self-bootstrapping apps
- [Briefcase](https://briefcase.readthedocs.io/en/stable/): Similar to Py2App
- [AppleCrate](https://github.com/RhetTbull/applecrate): Create installers

</div>
</div>

---

# Questions?
<!-- _class: "invert small-text" -->

![bg 60% right:40%](images/qrcode.png)

This talk: [https://github.com/RhetTbull/biting-the-apple](https://github.com/RhetTbull/biting-the-apple)
GitHub: [https://github.com/RhetTbull](https://github.com/RhetTbull)
LinkedIn: [https://www.linkedin.com/in/rhettbull/](https://www.linkedin.com/in/rhettbull/)
