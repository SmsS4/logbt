import logging

from logbt import config
from logbt import inject_loguru_to_logging
from logbt import logger

config(level="INFO", show_function=False)


def f():
    logger.info("INSIDE function")


logger.debug("YOU SHOULD NOT SEE THIS")
logger.info("THIS IS INFO")
logger.error("THIS IS NOT INFO")
f()

inject_loguru_to_logging("test")
logging_logger = logging.getLogger("test")
logging_logger.setLevel(logging.INFO)
logging_logger.info("Inject logging %s", "test")
