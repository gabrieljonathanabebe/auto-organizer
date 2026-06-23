import time

from watchdog.observers import Observer

import config as cfg
from handlers import ScreenshotEventHandler


def main() -> None:
    event_handler = ScreenshotEventHandler()

    observer = Observer()
    observer.schedule(event_handler, path=cfg.DESKTOP_DIR, recursive=False)
    observer.start()

    print(f"Watching: {cfg.DESKTOP_DIR}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
