from random import choice
from selenium.webdriver import (
    Chrome, Firefox, Edge,
    ChromeOptions, FirefoxOptions, EdgeOptions
)
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.remote.webdriver import WebDriver

from .driver_types import DriverTypes
from .proxies import proxy_list


class DriverFactory():

    @classmethod
    def get_driver(cls, browser_type: DriverTypes) -> WebDriver:
        """
        Get the Browser driver given a browser name

        Params
        ------
        browser_type: DriverTypes
            An option from Chrome | Edge | Firefox

        Returns
        -------
        WebDriver
        """

        proxy_options = cls.__set_proxy_options(browser_type)

        return {
            DriverTypes.CHROME: Chrome,
            DriverTypes.FIREFOX: Firefox,
            DriverTypes.EDGE: Edge,
        }[browser_type](options=proxy_options)

    def __set_proxy_options(self, browser_type: DriverTypes) -> ArgOptions:
        """
        Fetch a random proxy and add to a browser Options object

        Params
        ------
        browser_type: DriverTypes
            An option from Chrome | Edge | Firefox

        Returns
        -------
        ArgOptions
            A browser Options instance
        """
        proxy = choice(proxy_list)

        options: ArgOptions = {
            DriverTypes.CHROME: ChromeOptions,
            DriverTypes.FIREFOX: FirefoxOptions,
            DriverTypes.EDGE: EdgeOptions,
        }[browser_type]()

        options.add_argument(f"--proxy-server={proxy}")
        return options
