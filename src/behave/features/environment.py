import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath('./'))

from behave import fixture, use_fixture
from src.actions.input_form_action import InputFormAction
from selenium.webdriver.support.ui import WebDriverWait
from src.utils.types import WebDriver
from src.utils.enums import Browsers
from src.utils.webdriver_builder.driver_builder import DriverBuilder



@fixture
def browser_chrome(context):
    try:
        driver = DriverBuilder().build_for(Browsers.CHROME).set_implicit_wait(5).build()
        driver.implicitly_wait(5)
        context.driver = driver
        context.wait = WebDriverWait(driver, timeout=10)
        yield driver
    finally:
        driver.quit


@fixture
def initialize_actions(context):
    context.input_form_action = InputFormAction(context.driver, 10)


def before_scenario(context, scenario):
    use_fixture(browser_chrome, context)
    use_fixture(initialize_actions, context)
