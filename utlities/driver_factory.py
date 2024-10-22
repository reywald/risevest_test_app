from selenium import webdriver
from selenium.webdriver import Chrome, Firefox, Edge

# Web Driver services for different browsers
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# Driver managers for different browsers
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from typing import Tuple


class DriverFactory():

    @classmethod
    def get_driver(cls, browser_name: str) -> Tuple[Chrome | Firefox | Edge]:
        """
        Get the Browser driver given a browser name

        Params
        ------
        browser_name: str

        Returns
        -------
        [Chrome | Firefox | Edge]
        """

        drivers_dict = {
            "CHROME": Chrome,
            "FIREFOX": Firefox,
            "EDGE": Edge,
        }

        service = cls._get_service(browser_name.upper())

        return drivers_dict[browser_name.upper()](service=service)

    @staticmethod
    def _get_service(browser_name: str) -> Tuple[ChromeService | FirefoxService | EdgeService]:
        """
        Get the Browser service to manage the driver for a given browser name

        Params
        ------
        browser_name: str

        Returns
        -------
        [ChromeService | FirefoxService | EdgeService]
        """

        if browser_name == "CHROME":
            return ChromeService(executable_path=ChromeDriverManager().install())
        elif browser_name == "FIREFOX":
            return FirefoxService(executable_path=GeckoDriverManager().install())
        elif browser_name == "EDGE":
            return EdgeService(executable_path=EdgeChromiumDriverManager().install()),
