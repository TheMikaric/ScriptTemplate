import scriptlibraries.myui as ui
import scriptlibraries.myio as io 
import scriptlibraries.mymainlogic as logic
import logging
import sys

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('Main')
logger.setLevel(logging.DEBUG)

def setup():
    '''Returns all the values from the config file, and sets up the logging
    in each module properly'''

    boom_mode,boom_platform,\
    username,password,\
    max_tries, timeout, delay,\
    logging_level,log_to_console = io.load_config()

    if log_to_console:
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    if logging_level == 'ERROR':
        logging.getLogger().setLevel(logging.ERROR)
    
    ui.setup_logging(logging_level,log_to_console)
    io.setup_logging(logging_level,log_to_console)
    logic.setup_logging(logging_level,log_to_console)

    return boom_mode,boom_platform,\
    username,password,\
    max_tries, timeout, delay,\
    logging_level,log_to_console


def main():
    boom_mode,boom_platform,\
    username,password,\
    max_tries, timeout, delay,\
    logging_level,log_to_console = setup()

if __name__ == '__main__':
    main()