from selenium import webdriver

from ..repository.input_form import InputForm

from .base_action import BaseAction


class InputFormAction(BaseAction):
    def __init__(self, driver: webdriver, waitTime: float):
        super().__init__(driver, waitTime)
        self._inputFormObj = InputForm(self._driver, waitTime)

    def enter_personal_info(self, name: str, email: str, password: str, company: str, website: str) -> None:
        self._inputFormObj.name.send_keys(name)
        self._inputFormObj.email.send_keys(email)
        self._inputFormObj.password.send_keys(password)
        self._inputFormObj.company_name.send_keys(company)
        self._inputFormObj.website.send_keys(website)

    def enter_address_info(self, country: str, city: str, addr_1: str, addr_2: str, state: str, zip: str) -> None:
        self._inputFormObj.country.select_by_visible_text(country)
        self._inputFormObj.city.send_keys(city)
        self._inputFormObj.address_line_1.send_keys(addr_1)
        self._inputFormObj.address_line_2.send_keys(addr_2)
        self._inputFormObj.state.send_keys(state)
        self._inputFormObj.zip_code.send_keys(zip)
