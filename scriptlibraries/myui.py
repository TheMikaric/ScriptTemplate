import logging
import scriptlibraries.mystylelib as stylelib

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('UI')
logger.level = logging.DEBUG

def test():
    print("Hello, world from ui!")
    logger.debug("Hello, world from ui!")
    stylelib.test()
