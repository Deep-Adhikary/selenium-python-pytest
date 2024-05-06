
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class AjaxForm(BasePage):

    def __init__(self, driver:webdriver,waitTime:int):
        super().__init__(driver,waitTime)

    @property
    def form_header(self)->WebElement:
       return self._wait.until(EC.presence_of_element_located((By.XPATH,'(//*[.="Form Submit Demo"])[1]')))
    @property
    def name_input(self)->WebElement:
        return self._wait.until(EC.visibility_of_element_located((By.ID,'title')))
    @property
    def description_input(self)->WebElement:
        return self._wait.until(EC.presence_of_element_located((By.ID,'description')))
    @property
    def submit_button(self)->WebElement:
        return self._wait.until(EC.presence_of_element_located((By.ID,'btn-submit')))
    @property
    def form_submit_message(self)->WebElement:
        return self._wait.until(EC.presence_of_element_located((By.ID,'submit-control')))
        
