import logging
import yaml
import os

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('IO')
logger.level = logging.DEBUG

def load_config(file_name='config.yaml', subfolder=''):
        logger.debug(f'Entered the function load_config with parameters file_name={file_name} and subfolder={subfolder}')
        
        script_location = os.path.dirname(os.path.abspath(__file__)) # Folder in which this file is.
        scr = os.path.dirname(script_location) # Folder in which the script is.
        with open(os.path.join(scr, subfolder, file_name)) as config_file:
            config = yaml.safe_load(config_file)
            logger.debug('Config file loaded successfully')
        logger.debug('Exiting the load_config function')
        logger.level = config['logging']['level']
        # Return data in the order that the calling script
        # which should only ever be main.py expects,
        # this return should be updated if the structure
        # of config.yaml updates
        return \
        config['mode'],\
        config['credentials']['username'], config['credentials']['password'],\
        config['persistance']['max_tries'], config['persistance']['timeout'], config['persistance']['boom_delay'],\
        config['logging']['level'], config['logging']['to_console']\
        

def test():
    print('Hello, world from io!') 
    logger.error('Hello, world from io!')