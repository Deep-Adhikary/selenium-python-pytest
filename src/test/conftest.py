import sys
import os

sys.path.append(os.path.abspath('./'))

from src.utils.webdriver_builder.driver_builder import DriverBuilder
from src.utils.enums import Browsers
from src.utils.types import WebDriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from pytest import fixture
import pytest
from typing import Any, Generator



@fixture(scope='session')
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


@fixture(scope="class")
def driver():
    _drivers = []

    def _driver(browserName: str = Browsers.CHROME) -> WebDriver:
        driver = DriverBuilder().build_for(browserName).set_implicit_wait(5).build()
        driver.implicitly_wait(5)
        _drivers.append(driver)
        return driver

    yield _driver

    for driver in _drivers:
        driver.quit()


@fixture(scope='class')
def browser(driver) -> WebDriver:
    _browser: WebDriver = driver(Browsers.FIREFOX)
    return _browser


@fixture(scope="class")
def wait(browser):
    webdriverWait = WebDriverWait(driver=browser, timeout=10)
    yield webdriverWait
