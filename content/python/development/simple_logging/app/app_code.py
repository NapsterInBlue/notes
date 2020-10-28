import logging

logger = logging.getLogger(__name__)
print(logging.root.handlers)
print("__name__", __name__.ljust(15), "printed from", "app/app_code.py")


def run_app():
    for i in range(10):
        logger.info(f"App ran for {i}")

        if i == 6:
            logger.warn("We saw the number 6!")
