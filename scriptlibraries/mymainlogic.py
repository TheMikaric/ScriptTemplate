import logging
import scriptlibraries.mylogiclib as logiclib

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('Mainlogic')
logger.setLevel(logging.ERROR)

def test():
    print('Hello, world from mainlogic!')
    logger.debug('Hello, world from mainlogic!')
    logiclib.test()

def start_driver(username,password,mode,platform,short_sleep=1,timeout=10):
    return logiclib.start_driver(username,password,mode,platform,short_sleep=short_sleep,timeout=timeout)
