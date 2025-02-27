import logging
import sys

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('mystylelib')
logger.level = logging.ERROR

def setup_logging(logging_level,log_to_console):
    '''Makes log messages appear in the console, in addition to standard file output.'''
    if log_to_console:
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    if logging_level == 'ERROR':
        logger.setLevel(logging.ERROR)