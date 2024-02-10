#!/usr/bin/env python3
# Models Module Documentation
# The storage module serves as a singleton for FileStorage,
# responsible for reloading objects to file.json.

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
