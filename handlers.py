from datetime import datetime
import logging
from pathlib import Path

from watchdog.events import (
    FileCreatedEvent,
    FileMovedEvent,
    FileSystemEventHandler,
)

import config as cfg
from file_utils import get_available_dest_path, move_file, has_stable_size
from screenshot_utils import get_month_folder, is_screenshot

logger = logging.getLogger(__name__)


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
            logger.warning("Skipping missing file: %s", path)
            return
        if not has_stable_size(path):
            logger.warning("Skipped unstable file: %s", path)
            return
        if not is_screenshot(path):
            return

        target_folder = get_month_folder()
        target_folder.mkdir(parents=True, exist_ok=True)

        dest_path = target_folder / path.name
        dest_path = get_available_dest_path(dest_path)
        logger.info("Screenshot detected %s", path)

        if cfg.DRY_RUN:
            logger.info("Dry run: would move to: %s", dest_path)
            return
        try:
            move_file(path, dest_path)
        except OSError:
            logger.exception("Could not move file: %s", path)
            return
        logger.info("Moved to: %s", dest_path)
