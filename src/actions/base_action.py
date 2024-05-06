
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from utils.screenshot import Screenshot

class BaseAction:
    _driver=None
    _webDriverWait=None
    
    def __init__(self, driver:webdriver,waitTime:float):
        self._driver=driver
        self._webDriverWait: WebDriverWait = WebDriverWait(driver,timeout=waitTime)
        self._screenshot=Screenshot(self._driver, './reports/screenshots')