from abc import ABC, abstractmethod
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from unittest import TestCase


class BasePage(ABC):
    """ The base page from which other page objects inherit """

    def __init__(self, browser: Chrome | Edge | Firefox, tester: TestCase):
        """
        Params
        ------
        browser: The browser's driver manager instance
        tester: unittest.TestCase instance. Provides assertion methods
        """
        self.browser = browser
        self.tester = tester

    def await_page_load(self, expected_url: str):
        """
        Checks if after a page loads, the browser URL matches the expected web location
        """
        try:
            WebDriverWait(self.browser, 20).until(
                EC.url_to_be(expected_url))
        except TimeoutException as toe:
            toe.msg = f"Not in the right url: {expected_url}"
            self.logger.error(toe)
            raise toe

    def get_element(self, web_locator: tuple):
        """
        Checks if a web element exists on the page's DOM

        Params
        ------
        web_locator: a tuple of the form (By.*, "locator")

        Returns
        -------
        web_element: WebElement
        """
        web_element = None

        try:
            web_element = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(web_locator)
            )
        except TimeoutException as toe:
            toe.msg = f"Could not find element {web_locator} on time"
            self.logger.error(toe)
            raise toe

        return web_element

    def get_elements(self, web_locator: tuple) -> list:
        """
        Checks if multiple web elements exist on the page's DOM

        Params
        ------
        web_locator: a tuple of the form (By.*, "locator")

        Returns
        -------
        web_elements: List[WebElement]
        """
        web_elements = None

        try:
            web_elements = WebDriverWait(self.browser, 100).until(
                EC.presence_of_all_elements_located(web_locator)
            )
        except TimeoutException as toe:
            toe.msg = f"Could not find element {web_locator} on time"
            self.logger.error(toe)
            raise toe

        return web_elements

    @abstractmethod
    def validate_page(self):
        """
        Checks that all elements of the page are in place with the right text content
        """

    @classmethod
    def set_logger(cls, logger):
        """
        Add a logger for every page object to use

        Params
        ------
        logger: Logger
        """
        cls.logger = logger
