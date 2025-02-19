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
        
def resolve_file_name(file_name:str,subfolder:str)->str:
    '''This function joins file_name and subfolder strings with character '\' ,
    and returns just the file_name if empty or no subfolder is provided'''
    return resolve_file_name(file_name,subfolder)

def read_pdf(file_name,subfolder='inputs',echo=False):
    '''Takes in the name of the file and its subfolder within the script, and returns all text contained in the pdf.
    Optionally echoes the pdf contents to the console.'''
    return iolib.read_pdf(file_name=file_name,subfolder=subfolder,echo=echo)

def read_all_pdfs(subfolder='inputs',echo=False):
    '''Takes in the name of the subfolder, and returns all the text from all the files in a list,
    each member of a list being complete text of a file.'''
    return iolib.read_all_pdfs(subfolder=subfolder,echo=echo)

def find_train_num(text,fleet)->str:
    '''Returns a list of train numbers belonging to a given fleet from a given text.
    Supported fleets: Desiro, Mireo, ABY, FLIRT'''
    return iolib.find_train_num(text=text,fleet=fleet)