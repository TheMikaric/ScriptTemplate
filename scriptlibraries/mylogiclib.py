import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.common.exceptions as sce
import sys
import time
import re


logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('logiclib')
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
    logger.debug("Entered start_driver function")

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options) # Opens chrome window

    extension = '-training' if platform=="training" else ''
    if override_link: 
        logger.debug(f'Overriding the link with {override_link}')
        driver.get(override_link)
    else: driver.get(f'https://amigo{extension}.eucorail.com/{mode}') #Open the web page
    action_chains = ActionChains(driver)
    logger.debug("Driver made action chains")

    #Log in
    try:
        WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.ID,"un"))).send_keys(username)
        time.sleep(delay)
        WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.NAME,"Password"))).send_keys(password)
        driver.find_element(By.CLASS_NAME, "login-button").click() #Click login button to actually login
        logger.info("Logged in")
    except sce.TimeoutException:
        logger.error(f'Timeout exception!')
    except Exception as e:
        logger.error(f'Failed to log in, error: {e}')

    logger.debug("Exiting start_driver function")
    return driver,action_chains

def click(driver,xpath:str,double_click:bool=False,max_tries=15,timeout=10,delay=1):
    '''This function clicks on the XPATH of specified element once or twice with
    given persistance. Useful due to Amigo/Boom instability. 
    Raises TimeoutError if it time outs.'''
    logger.debug(f'Entered click function with xpath={xpath}, max_tries={max_tries}, double_click={double_click}, timeout={timeout}, delay={delay}')

    for i in range(max_tries):
        try:
            if double_click:
                time.sleep(delay)
                actionChains = ActionChains(driver)
                actionChains.double_click(driver.find_element(By.XPATH, xpath)).perform()
            else:
                WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
            return
        except sce.TimeoutException:
            logger.info(f'Timeout exception on click function! Try number {i}')
        time.sleep(delay)

    raise TimeoutError(f'Failed to click on the element with xpath={xpath} after {max_tries} tries.')

def read_value(driver,xpath:str,max_tries=15,timeout=10,delay=1)->str:
    '''Reads value attribute from the element of specified XPath and returns it as a string'''
    logger.debug(f'Entered read_value function with xpath={xpath}, max_tries={max_tries}, timeout={timeout}, delay={delay}')
    
    for i in range(max_tries):
        try:
            WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = driver.find_element(By.XPATH, xpath)
            logger.debug(f'Element found with xpath={xpath}')
            return element.text
        except sce.TimeoutException:
            logger.info(f'Timeout exception on read_value function! Try number {i}')
        time.sleep(delay)
            
        raise TimeoutError(f'Failed to read value of the element with xpath={xpath} after {max_tries} tries.')
    
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
        raise IndexError(f'In function find_train_num Index error on to_return={results},returning empty string.')
        
    return to_return

def extract_between_strings(text:str,string1,string2)->list[str]:
    '''Extracts text that is contained between string1 and string2 (ordered)'''
    logger.debug(f'Etntered extract_between_strings function with text and string1={string1} string2={string2}')
    if string2!="": 
        pattern = re.escape(string1)+r'\s*(.*?)\s*'+re.escape(string2)
    else: 
        pattern = re.escape(string1)+r'\s*(.*?) ' # NEEDS TO INCLUDE A SINGLE SPACE AFTER STRING IN THIS CASE
        logger.debug("String2 was empty, so the alternative RegEx statement is being used.")
    return re.findall(pattern, text, re.DOTALL)

def setup_logging(logging_level,log_to_console):
    '''Makes log messages appear in the console, in addition to standard file output.'''
    if log_to_console:
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    if logging_level == 'ERROR':
        logger.setLevel(logging.ERROR)