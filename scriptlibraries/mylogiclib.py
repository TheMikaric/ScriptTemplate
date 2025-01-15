import logging

logging.basicConfig(
        level=logging.DEBUG,
        format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('logiclib')
logger.level = logging.DEBUG

def test():
    print("Hello, world from mylogiclib!")
    logger.debug("Hello, world from mylogiclib!")
