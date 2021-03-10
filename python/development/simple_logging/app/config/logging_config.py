import logging
import sys
import os

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s"
)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(logging.WARNING)
    return console_handler


def get_file_handler():
    cwd = os.getcwd()
    if cwd.split("\\")[-1] == "development":
        path = "simple_logging/logs/app.log"
    else:
        path = "logs/app.log"

    file_handler = logging.FileHandler(path)
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.INFO)
    return file_handler
