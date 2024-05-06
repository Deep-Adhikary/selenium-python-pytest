from typing import Callable, List,TypeAlias
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

WebDriver: TypeAlias= ChromeDriver | FirefoxDriver
WebDriverOptions:TypeAlias= ChromeOptions | FirefoxOptions