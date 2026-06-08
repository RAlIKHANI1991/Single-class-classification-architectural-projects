# src/utils/logger.py

import logging


def get_logger(name: str):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        )

        stream_handler = logging.StreamHandler()

        stream_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            stream_handler
        )

    return logger