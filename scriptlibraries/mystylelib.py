import logging

logging.basicConfig(
        level=logging.DEBUG,
        format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('mystylelib')
logger.level = logging.DEBUG

def test():
    print("Hello wrold from mystylelib!")
    logger.debug("Hello wrold from mystylelib!")
