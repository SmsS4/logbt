from logiri import logger


def f():
    logger.info("INSIDE function")


logger.info("THIS IS INFO")
logger.error("THIS IS NOT INFO")
f()
