
from selenium import webdriver

from ..repository.ajax_form import AjaxForm

from .base_action import BaseAction
class AjaxFormAction(BaseAction):

    def __init__(self, driver:webdriver,waitTime:float):
        super().__init__(driver,waitTime)   
        self._ajaxFormObj=AjaxForm(self._driver,waitTime)
    
    def submit_form(self, name:str,message:str):
        assert self._ajaxFormObj.form_header.is_displayed()==True
        self._screenshot.capture()
        self._ajaxFormObj.name_input.send_keys(name)
        self._ajaxFormObj.description_input.send_keys(message)
        self._screenshot.capture()
        self._ajaxFormObj.submit_button.click()    
        assert self._ajaxFormObj.form_submit_message.is_displayed() ==True
        assert self._ajaxFormObj.form_submit_message.text=='Ajax Request is Processing!' 
        self._screenshot.capture()
