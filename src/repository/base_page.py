from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    _driver = None
    _wait=None
    def __init__(self,driver:webdriver,waitTime:float) -> None:
        self._driver = driver
        self._wait: WebDriverWait = WebDriverWait(driver, waitTime)