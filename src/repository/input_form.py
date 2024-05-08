
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC, select

from .base_page import BasePage


class InputForm(BasePage):
    def __init__(self, driver: webdriver, waitTime: int):
        super().__init__(driver, waitTime)

    @property
    def input_form_nav(self):
        return self._wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, 'Input Form Submit')))

    @property
    def name(self):
        return self._wait.until(EC.presence_of_element_located((By.ID, 'name')))

    @property
    def email(self):
        return self._wait.until(EC.presence_of_element_located(
            (By.ID, 'inputEmail4')))

    @property
    def password(self):
        return self._wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '* [name="password"]')))

    @property
    def company_name(self):
        return self._wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@name="company"]')))

    @property
    def website(self):
        return self._wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@for="inputWebsite"]/following-sibling::input')))

    @property
    def country(self):
        return select.Select(self._wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[.="Country*"]/following-sibling::select'))))

    @property
    def city(self):
        return self._wait.until(EC.visibility_of_element_located(
            (By.NAME, 'city')))

    @property
    def address_line_1(self):
        return self._wait.until(EC.visibility_of_element_located(
            (By.NAME, 'address_line1')))

    @property
    def address_line_2(self):
        return self._wait.until(EC.visibility_of_element_located(
            (By.NAME, 'address_line2')))

    @property
    def state(self):
        return self._wait.until(EC.visibility_of_element_located(
            (By.ID, 'inputState')))

    @property
    def zip_code(self):
        return self._wait.until(EC.visibility_of_element_located(
            (By.ID, 'inputZip')))

    @property
    def submit_button(self):
        return self._wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.loginform button')))

    def get_success_msg(self, success_msg):
        return self._wait.until(EC.presence_of_element_located(
            (By.XPATH, f'//*[.="{success_msg}"]')))
