import logging
import scriptlibraries.mylogiclib as logiclib

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('Mainlogic')
logger.level = logging.DEBUG

def test():
    print('Hello, world from mainlogic!')
    logger.debug('Hello, world from mainlogic!')
    logiclib.test()