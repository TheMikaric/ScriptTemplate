import logging
import scriptlibraries.mystylelib as stylelib

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('UI')
logger.level = logging.ERROR

def test():
    print("Hello, world from ui!")
    logger.debug("Hello, world from ui!")
    stylelib.test()
