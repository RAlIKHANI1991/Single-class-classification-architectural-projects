# config/logging_config.py

import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler
from config.settings import settings

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True,exist_ok=True)

LOG_FILE = LOG_DIR / "api.log"

def setup_logger(logger_name: str = "project_logger"):

    logger = logging.getLogger(logger_name)
    logger.setLevel(settings.LOG_LEVEL)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        (
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ))

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger