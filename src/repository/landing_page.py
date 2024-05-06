from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class LandingPage(BasePage) :
    def __init__(self, driver: webdriver, waitTime: float) -> None:
        super().__init__(driver,waitTime)

    @property
    def page_header(self) -> WebElement:
        return self._driver.find_element(
            by=By.XPATH, value="(//*[.='Selenium Playground'])[1]")

    def get_nav_link(self, link_text: str) -> WebElement:
        return self._wait.until(
            EC.visibility_of_element_located(
                (By.LINK_TEXT, link_text)))
