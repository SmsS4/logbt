Configuration for Loguru

# Install

```shell
poetry add logbt
```

# Usage

```python
from logbt import config
from logbt import logger

config(level="DEBUG")


def f():
    logger.info("INSIDE function")


logger.debug("YOU SHOULD NOT SEE THIS")
logger.info("THIS IS INFO")
logger.error("THIS IS NOT INFO")
f()
```
