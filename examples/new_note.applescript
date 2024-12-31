on createNote(noteTitle, noteBody)
	tell application "Notes"
		activate
		
		tell account "iCloud"
			set newNote to make new note at folder "Notes" with properties {name:noteTitle, body:noteBody}
			return id of newNote
		end tell
	end tell
end createNote

createNote("Hello", "World")
