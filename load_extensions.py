# ---------------------
# load_extensions.py
# Description: Loads the approved file extensions
# http://shayConcepts.com
# Andrew Shay
# ---------------------

import json
import base64


def load_default_extensions():
    """
    Loads the default file extensions
    """

    extensions = {
        "extensions": [
            ".mp4",
            ".avi",
            ".mkv",
            ".mpeg",
            ".wmv",
            ".wma",
            ".mov",
            ".3gp",
            ".flv"
        ]
    }

    extensions = json.dumps(extensions)
    return extensions


def load_file_extensions():
    """
    Loads file extensions from file_extensions.json

    Returns:
    extensions_data -- String. File extensions base64 encoded
    """

    try:
        file_extensions = open("file_extensions.json", "r").read()
    except:
        file_extensions = load_default_extensions()

    file_extensions = file_extensions.splitlines()
    extensions_data = ""
    for line in file_extensions:
        extensions_data += line

    extensions_data = base64.b64encode(extensions_data)

    return extensions_data

if __name__ == "__main__":
    extensions = load_file_extensions()
    print(extensions)
