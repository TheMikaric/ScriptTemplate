import logging

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('logiclib')
logger.level = logging.DEBUG

def test():
    print("Hello, world from mylogiclib!")
    logger.debug("Hello, world from mylogiclib!")
