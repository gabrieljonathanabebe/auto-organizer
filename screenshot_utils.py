from datetime import datetime
from pathlib import Path

import config as cfg


def is_screenshot(path: Path) -> bool:
    filename = path.name
    extension = path.suffix.lower()
    has_screenshot_prefix = filename.startswith(cfg.SCREENSHOT_PREFIXES)
    has_image_extension = extension in cfg.IMAGE_EXTENSIONS
    return has_screenshot_prefix and has_image_extension


def get_month_folder() -> Path:
    current_month = datetime.now().strftime("%Y-%m")
    return cfg.SCREENSHOT_ROOT / current_month
