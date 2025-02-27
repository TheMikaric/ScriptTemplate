import logging
import sys
import scriptlibraries.myiolib as iolib 

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('IO')
logger.level = logging.DEBUG

def load_config(file_name:str='config.yaml', subfolder:str=''):
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
    return iolib.resolve_file_name(file_name,subfolder)

def read_pdf(file_name:str,subfolder:str='inputs',echo=False):
    '''Takes in the name of the file and its subfolder within the script, and returns all text contained in the pdf.
    Optionally echoes the pdf contents to the console.'''
    return iolib.read_pdf(file_name=file_name,subfolder=subfolder,echo=echo)

def read_all_pdfs(subfolder:str='inputs',echo=False):
    '''Takes in the name of the subfolder, and returns all the text from all the files in a list,
    each member of a list being complete text of a file.'''
    return iolib.read_all_pdfs(subfolder=subfolder,echo=echo)

def export_to_csv(data: list[list[str]],column_names: list[str]=[""],file_name:str='output.csv',subfolder:str='outputs',mode:str='a'):
    '''Takes in the column names and data to write to the csv file.
    Each individual list within data input is a row, and its elements are individual elements
    Mode options: 'a' for append, or add to the end of already existing .csv, 'w' for write to overwrite existing contents '''
    return iolib.export_to_csv(data=data,column_names=column_names,file_name=file_name,subfolder=subfolder,mode=mode)

def setup_logging(logging_level,log_to_console):
    '''Makes log messages appear in the console, in addition to standard file output.'''
    if log_to_console:
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    if logging_level == 'ERROR':
        logger.level = logging.ERROR
    iolib.setup_logging(logging_level,log_to_console)