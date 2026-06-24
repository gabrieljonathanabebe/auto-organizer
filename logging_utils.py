import logging
from logging.handlers import RotatingFileHandler

import config as cfg


def configure_logging() -> None:
    cfg.LOG_DIR.mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(
        cfg.LOG_FILE,
        maxBytes=cfg.LOG_MAX_BYTES,
        backupCount=cfg.LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    file_handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.setLevel(cfg.LOG_LEVEL)
    root_logger.addHandler(file_handler)
