tell application "Notes"
	activate
	
	set noteTitle to "Hello World"
	set noteBody to "This is my note."
	
	tell account "iCloud"
		set newNote to make new note at folder "Notes" with properties {name:noteTitle, body:noteBody}
	end tell
end tell
