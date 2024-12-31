"""Create a new note in Notes.app using applescript via py-applescript

To use: python3 -m pip install py-applescript
"""

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
