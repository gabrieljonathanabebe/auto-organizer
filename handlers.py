from datetime import datetime
from pathlib import Path

from watchdog.events import (
    FileCreatedEvent,
    FileMovedEvent,
    FileSystemEventHandler,
)

import config as cfg
from file_utils import get_available_dest_path, move_file, has_stable_size
from screenshot_utils import get_month_folder, is_screenshot


class ScreenshotEventHandler(FileSystemEventHandler):
    def on_created(self, event: FileCreatedEvent) -> None:
        if event.is_directory:
            return

        source_path = Path(event.src_path)

        if source_path.name.startswith("."):
            return

        self.handle_candidate_file(source_path)

    def on_moved(self, event: FileMovedEvent) -> None:
        if event.is_directory:
            return

        dest_path = Path(event.dest_path)
        self.handle_candidate_file(dest_path)

    def handle_candidate_file(self, path: Path) -> None:
        if path.is_relative_to(cfg.SCREENSHOT_ROOT):
            return
        if not path.exists():
            print("Skipped missing file:")
            print(path)
            return
        if not has_stable_size(path):
            print("Skipped unstable file:")
            print(path)
            return
        if not is_screenshot(path):
            return

        target_folder = get_month_folder()
        target_folder.mkdir(parents=True, exist_ok=True)

        dest_path = target_folder / path.name
        dest_path = get_available_dest_path(dest_path)
        print("Screenshot detected:")
        print(path)

        if cfg.DRY_RUN:
            print("Dry run: would move to:")
            print(dest_path)
            return
        move_file(path, dest_path)
        print("Moved to:")
        print(dest_path)
