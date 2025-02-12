import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('logiclib')
logger.setLevel(logging.DEBUG)

# Opens chrome and BOOM/AMIGO, logs in with the given parameters and returns driver and action_chains
def start_driver(username,password,mode,platform,short_sleep=1,timeout=10): 
    logger.debug("Entered start_driver function")

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options) # Opens chrome window
    extension = '-training' if mode=="training" else ''
    driver.get(f'https://amigo{extension}.eucorail.com/{platform}') # 
    logging.debug("Driver got Amigo login page URL")
    action_chains = ActionChains(driver)
    logger.debug("Driver made action chains")

    #Log in
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.ID,"un"))).send_keys(username)
    logger.debug("Entered username")
    time.sleep(short_sleep)
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.NAME,"Password"))).send_keys(password)
    logger.debug("Entered password")
    driver.find_element(By.CLASS_NAME, "login-button").click() #Click login button to actually login
    logger.info("Logged in")

    logger.debug("Exiting start_driver function")
    return driver,action_chains

def test():
    print("Hello, world from mylogiclib!")
    logger.debug("Hello, world from mylogiclib!")
