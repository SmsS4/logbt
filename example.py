from logbt import config
from logbt import logger

config(level="INFO")


def f():
    logger.info("INSIDE function")


logger.debug("YOU SHOULD NOT SEE THIS")
logger.info("THIS IS INFO")
logger.error("THIS IS NOT INFO")
f()
