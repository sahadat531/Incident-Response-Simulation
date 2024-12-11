
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileMonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            with open("incident_logs.txt", "a") as log_file:
                log_file.write(f"File modified: {event.src_path} at {time.ctime()}\n")
                print(f"[ALERT] File modified: {event.src_path} at {time.ctime()}")

    def on_created(self, event):
        if not event.is_directory:
            with open("incident_logs.txt", "a") as log_file:
                log_file.write(f"File created: {event.src_path} at {time.ctime()}\n")
                print(f"[ALERT] File created: {event.src_path} at {time.ctime()}")

def monitor_folder(folder_path):
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    try:
        print(f"Monitoring folder: {folder_path}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_to_monitor = "./monitor_folder"
    os.makedirs(folder_to_monitor, exist_ok=True)
    monitor_folder(folder_to_monitor)
