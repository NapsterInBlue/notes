import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import app.app_code
import logging

from app.config import logging_config

logger = logging.getLogger(__name__)
print("__name__", __name__.ljust(15), "printed from", "app/__init__.py")
logger.setLevel(logging.DEBUG)

logger.addHandler(logging_config.get_console_handler())
logger.addHandler(logging_config.get_file_handler())
