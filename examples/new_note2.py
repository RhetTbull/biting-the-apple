"""Create a note in Notes.app

To use: python3 -m pip install macnotesapp
"""

import macnotesapp

new_note = macnotesapp.NotesApp().make_note("Hello World", "This is my note.")
print(f"New note created with ID {new_note}")
