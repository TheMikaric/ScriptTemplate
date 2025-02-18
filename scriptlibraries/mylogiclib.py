import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.common.exceptions as sce
import csv
import time
from pypdf import PdfReader
import re
import os

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('logiclib')
logger.setLevel(logging.DEBUG)

def start_driver(username,password,mode:str,platform:str,short_sleep=1,timeout=10): 
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
    logger.debug("Entered start_driver function")

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options) # Opens chrome window
    extension = '-training' if mode=="training" else ''
    driver.get(f'https://amigo{extension}.eucorail.com/{platform}') #Open the web page
    action_chains = ActionChains(driver)
    logger.debug("Driver made action chains")

    #Log in
    try:
        WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.ID,"un"))).send_keys(username)
        time.sleep(short_sleep)
        WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.NAME,"Password"))).send_keys(password)
        driver.find_element(By.CLASS_NAME, "login-button").click() #Click login button to actually login
        logger.info("Logged in")
    except sce.TimeoutException:
        logger.error(f'Timeout exception!')
    except Exception as e:
        logger.error(f'Failed to log in, error: {e}')

    logger.debug("Exiting start_driver function")
    return driver,action_chains

def resolve_file_name(file_name:str,subfolder:str)->str:
    '''This function joins file_name and subfolder strings with character '\' ,
    and returns just the file_name if empty or no subfolder is provided'''
    if not file_name: raise NameError('No file_name provided!')
    if not subfolder:
        return file_name
    elif subfolder=='':
        logger.warning(f'No subfolder for the resolve_file_name with file_name={file_name} provided!')
        return file_name
    else:
        return f'{subfolder}\{file_name}'

def read_pdf(file_name,subfolder='inputs',echo=False):
    '''Takes in the name of the file and its subfolder within the script, and returns all text contained in the pdf.'''
    destination = resolve_file_name(file_name,subfolder)
    logger.info(f'Attempting to read pdf from read_pdf function with a destionation {destination}')
    to_return = ''
    try:
        reader = PdfReader(destination)
    except FileNotFoundError:
        raise FileNotFoundError('File not found in read_pdf function, even after resolving file name {destination}.')
    if echo: print(f'Attempting to read pdf from read_pdf function with a destionation {destination}')
    for page in reader.pages:
        if echo: print(page.extract_text())
        to_return+=page.extract_text()
    return to_return

def read_all_pdfs(subfolder:str='inputs',echo=False):
    '''Takes in the name of the subfolder, and returns all the text from all the files in a list,
    each member of a list being complete text of a file.'''
    return [read_pdf(f,subfolder=subfolder,echo=True) for f in os.listdir(subfolder) if os.path.isfile(os.path.join(subfolder,f))]
    
def find_train_num(text:str,fleet:str)->str:
    '''Returns a frist appearance of a train number belonging to a given fleet from a given text.
    Supported fleets: Desiro, Mireo, ABY, FLIRT'''

    fleet = fleet.lower()
    if fleet=='desiro' or fleet=='mireo': pattern="(?<!\d)\d{4}\.\d{3}(?!\d)" 
    elif fleet=='aby' or fleet=='flirt': pattern="ET\d\.\d{2}(?!\d)"
    else:
        raise NameError('Unknown fleet! Options: Desiro, Mireo, ABY, FLIRT')
    results = re.findall(pattern,text)
    
    try:
        to_return = results[0]
    except IndexError:
        logger.error(f'In function find_train_num Index error on to_return={results},returning empty string.')
        return ""
        
    return results[0]

def extract_between_strings(text,string1,string2):
    '''Extracts text that is contained between string1 and string2 (ordered)'''
    logger.debug(f'Etntered extract_between_strings function with text and string1={string1} string2={string2}')
    if string2!="": 
        pattern = re.escape(string1)+r'\s*(.*?)\s*'+re.escape(string2)
    else: 
        pattern = re.escape(string1)+r'\s*(.*?) ' # NEEDS TO INCLUDE A SINGLE SPACE AFTER STRING IN THIS CASE
        logger.debug("String2 was empty, so the alternative RegEx statement is being used.")
    return re.findall(pattern, text, re.DOTALL)

def export_to_csv(data: list[list[str]],column_names: list[str]=[""],file_name:str='output.csv',subfolder:str='outputs',mode:str='a'):
    '''Takes in the column names and data to write to the csv file.
    Each individual list within data input is a row, and its elements are individual elements
    Mode options: 'a' for append, or add to the end of already existing .csv, 'w' for write to overwrite existing contents '''

    with open(resolve_file_name(file_name,subfolder), mode=mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if mode == 'w': writer.writerow(column_names) # Only write column names if we are making a new file
        writer.writerows(data)
    pass

def test():
    print("Hello, world from mylogiclib!")
    logger.debug("Hello, world from mylogiclib!")
