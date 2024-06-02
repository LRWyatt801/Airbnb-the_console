#!/usr/bin/python3
"""init module for models"""


from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
