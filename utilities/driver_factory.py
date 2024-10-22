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

from .driver_types import DriverTypes


class DriverFactory():

    @classmethod
    def get_driver(cls, browser_type: DriverTypes):
        """
        Get the Browser driver given a browser name

        Params
        ------
        browser_name: DriverTypes

        Returns
        -------
        [Chrome | Firefox | Edge]
        """
        return {
            DriverTypes.CHROME: cls._get_chrome_manager,
            DriverTypes.FIREFOX: cls._get_firefox_manager,
            DriverTypes.EDGE: cls._get_edge_manager,
        }[browser_type]()

    @staticmethod
    def _get_chrome_manager() -> Chrome:
        """
        Get the Chrome driver

        Returns
        -------
        Chrome
        """

        return Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    @staticmethod
    def _get_firefox_manager() -> Firefox:
        """
        Get the Firefox driver

        Returns
        -------
        Firefox
        """

        return Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))

    @staticmethod
    def _get_edge_manager() -> Edge:
        """
        Get the Edge driver

        Returns
        -------
        Edge
        """

        return Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))
