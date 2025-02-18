import logging
import scriptlibraries.mylogiclib as logiclib
import re

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('Mainlogic')
logger.setLevel(logging.DEBUG)

def start_driver(username,password,mode,platform,short_sleep=1,timeout=10):
    '''Starts up Chrome browser, logins to Amigo and returns driver
        
        Inputs:
        string username, the credential for the Boom account
        string subfolder, the credential for the Boom account
        string mode, determines if the maintenance or asset Boom is acessed
        string platform, determines if the training or the actual enviornment is acessed
        
        Output:
        driver, the Selenium library object
        action_chains, Selenium object
        '''
    return logiclib.start_driver(username,password,mode,platform,short_sleep=short_sleep,timeout=timeout)

def read_pdf(file_name,subfolder='inputs',echo=False):
    '''Takes in the name of the file and its subfolder within the script, and returns all text contained in the pdf.
    Optionally echoes the pdf contents to the console.'''
    return logiclib.read_pdf(file_name=file_name,subfolder=subfolder,echo=echo)

def read_all_pdfs(subfolder='inputs',echo=False):
    '''Takes in the name of the subfolder, and returns all the text from all the files in a list,
    each member of a list being complete text of a file.'''
    return logiclib.read_all_pdfs(subfolder=subfolder,echo=echo)

def find_train_num(text,fleet)->str:
    '''Returns a list of train numbers belonging to a given fleet from a given text.
    Supported fleets: Desiro, Mireo, ABY, FLIRT'''
    return logiclib.find_train_num(text=text,fleet=fleet)

def extract_between_strings(text,string1,string2):
    '''Extracts text that is contained between string1 and string2 (ordered)'''
    return logiclib.extract_between_strings(text=text,string1=string1,string2=string2)

def export_to_csv(data: list[list[str]],column_names: list[str]=[""],file_name:str='output.csv',subfolder:str='outputs',mode:str='a'):
    '''Takes in the column names and data to write to the csv file.
    Each individual list within data input is a row, and its elements are individual elements
    Mode options: 'a' for append, or add to the end of already existing .csv, 'w' for write to overwrite existing contents '''

    return logiclib.export_to_csv(column_names=column_names,data=data,file_name=file_name,subfolder=subfolder,mode=mode)

def resolve_file_name(file_name:str,subfolder:str)->str:
    '''This function joins file_name and subfolder strings with character '\' ,
    and returns just the file_name if empty or no subfolder is provided'''
    return resolve_file_name(file_name,subfolder)

def test():
    print('Hello, world from mainlogic!')
    logger.debug('Hello, world from mainlogic!')
    logiclib.test()