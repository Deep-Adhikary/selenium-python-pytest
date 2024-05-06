from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from utils.enums import Browsers
from utils.types import WebDriver, WebDriverOptions


# from enum import Enum
# class Browsers(Enum):
#     CHROME='chrome'
#     FIREFOX='firefox'

# from typing import Callable, List,TypeAlias
# from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
# from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver

# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.chrome.options import Options as ChromeOptions

# WebDriver: TypeAlias= ChromeDriver | FirefoxDriver
# WebDriverOptions:TypeAlias= ChromeOptions | FirefoxOptions


class DriverBuilder():
    def __init__(self) -> None:
        self._option = None
        self._browser_name = Browsers.CHROME.value
        print(self._browser_name)
        self._browser_dict = {
            Browsers.CHROME.value: self._get_chrome_driver,
            Browsers.FIREFOX.value: self._get_geko_driver,
            }
        self._implicit_wait = 10

    def build_for(self, browser_name: Browsers):
        self._browser_name = browser_name.value
        return self

    def set_option(self, option: WebDriverOptions):
        self._option = option
        return self

    def set_implicit_wait(self, implicit_wait: int):
        self._implicit_wait = implicit_wait
        return self

    def build(self) -> WebDriver:
        print(self._browser_name)
        return self._browser_dict[self._browser_name]()

    def _get_chrome_driver(self) -> WebDriver:
        return webdriver.Chrome(options=self._option, service=ChromeService(
            ChromeDriverManager().install()))

    def _get_geko_driver(self) -> WebDriver:
        return webdriver.Firefox(options=self._option, service=FirefoxService(GeckoDriverManager().install()))

# if __name__ == "__main__":
#      driver = DriverBuilder().build_for(Browsers.FIREFOX).set_implicit_wait(5).build()
#      driver.quit()