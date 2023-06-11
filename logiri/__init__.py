import logging
import sys
import zlib
from pprint import pprint

import loguru

RESET = "\x1b[0m"
FORMATS = {
    logging.DEBUG: "\u001b[38;5;247m",
    logging.WARNING: "\u001b[38;5;11m",
    logging.ERROR: "\u001b[38;5;196m",
    logging.CRITICAL: "\u001b[38;5;52m",
    logging.INFO: "\u001b[38;5;46m",
}
COLORS = [
    46,
    27,
    44,
    93,
    118,
    128,
    123,
    131,
    134,
    30,
    47,
    64,
    68,
    138,
    141,
    147,
    151,
    155,
    165,
    175,
    183,
    192,
    201,
    210,
]


def random_color(text: str) -> str:
    color = (
        "\u001b[38;5;"
        + str(COLORS[zlib.adler32(text.encode()) % len(COLORS)])
        + "m"
    )
    return f"{color}{text}{RESET}"


def colorize(record):
    record["level"].name = f'[{record["level"].name}]'.ljust(10)
    record["module"] = random_color(f'[{record["module"]}]'.ljust(15))
    record["function"] = f'[{record["function"]}]'.ljust(10)


loguru.logger.remove()
logger = loguru.logger.patch(colorize)

splitter = " " * 3
logger.add(
    sys.stdout,
    colorize=True,
    format="SPLITTER[{time:YYYY-MM-DD HH:mm:ss}]"
    "SPLITTER<level>{level}</level>"
    "SPLITTER{module}"
    "SPLITTER{function}"
    "SPLITTER{message} :: ({file}:{line})".replace("SPLITTER", splitter),
)
