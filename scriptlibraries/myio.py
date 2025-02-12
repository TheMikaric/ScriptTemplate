import logging
import yaml
import os
import scriptlibraries.myiolib as iolib 

def load_config(file_name='config.yaml', subfolder=''):
    return iolib.load_config(file_name, subfolder)
        

def test():
    print('Hello, world from io!') 
    logger.error('Hello, world from io!')