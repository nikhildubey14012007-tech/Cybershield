
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from app.database.db import save_security_event


class FileMonitorHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            self.record_event("FILE_CREATED", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.record_event("FILE_MODIFIED", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.record_event("FILE_DELETED", event.src_path)

    def record_event(self, event_type, file_path):
        save_security_event(
            event_type,
            os.path.basename(file_path),
            f"{event_type}: {file_path}",
            "MEDIUM"
        )


def start_file_monitor(directory):
    if not os.path.isdir(directory):
        raise ValueError("Monitoring directory does not exist")

    observer = Observer()
    handler = FileMonitorHandler()

    observer.schedule(handler, directory, recursive=True)
    observer.start()

    return observer
