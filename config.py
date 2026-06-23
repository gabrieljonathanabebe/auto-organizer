from enum import StrEnum
from pathlib import Path

DESKTOP_DIR = Path.home() / "Desktop"
SCREENSHOT_ROOT = DESKTOP_DIR / "screenshots"

SCREENSHOT_PREFIXES = ("Bildschirmfoto", "Screenshot")
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}

DRY_RUN = False


class LogLevel(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


LOG_LEVEL = LogLevel.INFO
