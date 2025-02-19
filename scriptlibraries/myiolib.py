import logging
import yaml
import os
from pypdf import PdfReader
import csv

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
        config['boom_settings']['mode'],config['boom_settings']['platform'],\
        config['credentials']['username'], config['credentials']['password'],\
        config['persistance']['max_tries'], config['persistance']['timeout'], config['persistance']['boom_delay'],\
        config['logging']['level'], config['logging']['to_console']\
        
def resolve_file_name(file_name:str,subfolder:str)->str:
    '''This function joins file_name and subfolder strings with character '\' ,
    and returns just the file_name if empty or no subfolder is provided'''
    if not file_name: raise NameError('No file_name provided!')
    if not subfolder:
        logger.warning(f'No subfolder (None object) for the resolve_file_name with file_name={file_name} provided!')
        return file_name
    elif subfolder=='':
        logger.warning(f'No subfolder (string "") for the resolve_file_name with file_name={file_name} provided!')
        return file_name
    else:
        return f'{subfolder}\{file_name}'

def read_pdf(file_name,subfolder='inputs',echo=False):
    '''Takes in the name of the file and its subfolder within the script, and returns all text contained in the pdf.
    Returns None in the event that a file isn't a pdf file.'''

    if not 'pdf' in file_name:
        logger.warning(f'File {file_name} is not a PDF file, skipping it from read_pdf function!')
        return
    
    destination = resolve_file_name(file_name,subfolder)
    logger.info(f'Attempting to read pdf from read_pdf function with a destination {destination}')
    to_return = ''
    try:
        reader = PdfReader(destination)
    except FileNotFoundError:
        raise FileNotFoundError('File not found in read_pdf function, even after resolving file name {destination}.')
    if echo: print(f'Attempting to read pdf from read_pdf function with a destionation {destination}')
    for page in reader.pages:
        if echo: print(page.extract_text())
        to_return+=page.extract_text() # Pages usually have '\n' and ' ' characters between them
    return to_return

def read_all_pdfs(subfolder:str='inputs',echo=False):
    '''Takes in the name of the subfolder, and returns all the text from all the files in a list,
    each member of a list being complete text of a file.'''
    logger.debug(f'Entered read_all_pdfs function with parameter subfolder={subfolder}! Will call the read_pdf function for each individual file soon...')

    for_return = [read_pdf(f,subfolder=subfolder,echo=echo) for f in os.listdir(subfolder) if os.path.isfile(os.path.join(subfolder,f))]
    return for_return

def export_to_csv(data: list[list[str]],column_names: list[str]=[""],file_name:str='output.csv',subfolder:str='outputs',mode:str='a'):
    '''Takes in the column names and data to write to the csv file.
    Each individual list within data input is a row, and its elements are individual elements
    Mode options: 'a' for append, or add to the end of already existing .csv, 'w' for write to overwrite existing contents '''
    logger.debug(f'Entered function export_to_csv with parameters data={data}, column_names={column_names}, file_name ={file_name}, subfolder={subfolder}, mode={mode}')

    with open(resolve_file_name(file_name,subfolder), mode=mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if mode == 'w': 
            writer.writerow(column_names) # Only write column names if we are making a new file
        writer.writerows(data)
