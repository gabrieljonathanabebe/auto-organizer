import logging
import time

from watchdog.observers import Observer

import config as cfg
from handlers import ScreenshotEventHandler

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=cfg.LOG_LEVEL, format="%(asctime)s | %(levelname)s | %(message)s"
    )
    event_handler = ScreenshotEventHandler()

    observer = Observer()
    observer.schedule(event_handler, path=cfg.DESKTOP_DIR, recursive=False)
    observer.start()

    logger.info("Watching: %s", cfg.DESKTOP_DIR)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
