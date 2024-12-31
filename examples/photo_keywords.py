"""Add a keyword to currently selected photos in Photos.app

To use: python3 -m pip install photoscript
"""

import photoscript

for photo in photoscript.PhotosLibrary().selection:
    photo.keywords += ["Travel"]
