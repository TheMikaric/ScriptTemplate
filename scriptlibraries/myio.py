import logging
import yaml
import os
import scriptlibraries.myiolib as iolib 

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('IO')
logger.level = logging.DEBUG

def load_config(file_name='config.yaml', subfolder=''):
    '''Loads a config file into memory and returns its values.
        
        Inputs:
        string file_name, the name of the config file including the extension
        string subfolder, the subfolder in which the config file is in,
        counting from the folder of main.py
        
        Output:
        list of strings containing config file's contents
    '''
    return iolib.load_config(file_name, subfolder)
        

def test():
    print('Hello, world from io!') 
    logger.error('Hello, world from io!')