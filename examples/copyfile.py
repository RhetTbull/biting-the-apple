"""Copy a file on macOS using native API.
This allows copied files to use copy-on-write when used on a volume formatted with APFS.

When used on an APFS volume, a file copied with this function will be copied almost instantly
and will not use any additional disk space until the file is modified.

To use, you will need to install pyobjc-core and pyobjc-framework-Cocoa:

    `python3 -m pip install pyobjc-core pyobjc-framework-Cocoa`

This function uses the native [NSFileManager](https://developer.apple.com/documentation/foundation/nsfilemanager) API to perform the copy.
The Objective-C function is called via [pyobjc](https://pyobjc.readthedocs.io/en/latest/).

For full implementation with error checking, etc. see https://gist.github.com/RhetTbull/e418f8090f1eea39f0d653e43bf8222b
"""

import Foundation


def copyfile(src: str, dest: str):
    """Copy file from src to dest using NSFileManager"""
    filemgr = Foundation.NSFileManager.defaultManager()
    success, error = filemgr.copyItemAtPath_toPath_error_(src, dest, None)
    if not success:
        raise OSError(error)


if __name__ == "__main__":
    import sys

    copyfile(sys.argv[1], sys.argv[2])
