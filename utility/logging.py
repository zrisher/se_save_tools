"""
utility/logging.py
"""

import os
import logging


def logger(name, path, level_str=None):
    dir_path = os.path.dirname(path)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    logger = logging.getLogger(name)

    level = getattr(logging, level_str.upper()) if level_str else logging.INFO
    logger.setLevel(level)

    format = "%(asctime)s %(levelname)s: %(message)s"
    date_format = "%Y/%m/%d %H:%M:%S"
    formatter = logging.Formatter(fmt=format, datefmt=date_format)

    file_handler = logging.FileHandler(path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
