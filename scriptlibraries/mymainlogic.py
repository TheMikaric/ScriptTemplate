import logging
import scriptlibraries.mylogiclib as logiclib
import sys
import re

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('Mainlogic')
logger.setLevel(logging.DEBUG)

def start_driver(username:str,password:str,mode:str,platform:str,timeout=10,delay=1,override_link:str=None):
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
    return logiclib.start_driver(username,password,mode,platform,timeout=timeout,delay=delay,override_link=override_link)

def click(driver,xpath:str,double_click:bool=False,max_tries=15,timeout=10,delay=1):
    '''This function clicks on the XPATH of specified element with
    given persistance. Useful due to Amigo/Boom instability'''
    return logiclib.click(driver=driver,xpath=xpath,double_click=double_click,max_tries=max_tries,timeout=timeout,delay=delay)

def read_value(driver,xpath:str,max_tries=15,timeout=10,delay=1)->str:
    '''Reads value attribute from the element of specified XPath and returns it as a string'''
    return logiclib.read_value(driver=driver,xpath=xpath,max_tries=max_tries,timeout=timeout,delay=delay)

def extract_code(text:str)->str:
    '''Extracts a code from a given text, anything between [ and ]'''
    logger.debug(f'Entered extract_code function with text={text}')
    return re.findall(r'\[(.*?)\]', text)

def find_train_num(text:str,fleet:str)->str:
    '''Returns a frist appearance of a train number belonging to a given fleet from a given text.
    Supported fleets: Desiro, Mireo, ABY, FLIRT'''
    return logiclib.find_train_num(text=text,fleet=fleet)

def extract_between_strings(text,string1,string2):
    '''Extracts text that is contained between string1 and string2 (ordered)'''
    return logiclib.extract_between_strings(text=text,string1=string1,string2=string2)

def setup_logging(logging_level,log_to_console):
    '''Makes log messages appear in the console, in addition to standard file output.'''
    if log_to_console:
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    if logging_level == 'ERROR':
        logger.setLevel(logging.ERROR)
    logiclib.setup_logging(logging_level,log_to_console)