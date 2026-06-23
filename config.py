from pathlib import Path


DESKTOP_DIR = Path.home() / "Desktop"
SCREENSHOT_ROOT = DESKTOP_DIR / "screenshots"

SCREENSHOT_PREFIXES = ("Bildschirmfoto", "Screenshot")
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}

DRY_RUN = False