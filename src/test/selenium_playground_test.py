import sys
import os

sys.path.append(os.path.abspath('./'))

import pytest
from selenium import webdriver

from src.actions.ajax_form_action import AjaxFormAction
from src.repository.landing_page import LandingPage
from src.utils.screenshot import Screenshot

from src.utils.types import WebDriver
from src.utils.enums import Browsers
class TestForm: 
    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_home(self,browser:WebDriver,base_url):
        browser.get(base_url)

    def test_ajax_form(self, browser):
        landingPage=LandingPage(browser, 10)
        ajaxFormAction=AjaxFormAction(browser, 10)

        assert landingPage.page_header.is_displayed()==True
        landingPage.get_nav_link('Ajax Form Submit').click()
        ajaxFormAction.submit_form("Test","Test")
    
    def test_ajax_form2(self, browser):
        landingPage=LandingPage(browser, 10)
        ajaxFormAction=AjaxFormAction(browser, 10)

        assert landingPage.page_header.is_displayed()==True
        landingPage.get_nav_link('Ajax Form Submit').click()
        ajaxFormAction.submit_form("Test","Test")

    
    
