from unittest import TestCase
from selenium.webdriver.remote.webdriver import WebDriver
from po.base_page import BasePage


class PlanBasePage(BasePage):
    """ Extends the BasePage and serves as a base for other plan pages """

    def __init__(self, browser: WebDriver, tester: TestCase, plan_data: dict):
        """
        Params
        ------
        browser: WebDriver
          The browser's driver manager instance
        tester: 
          unittest.TestCase instance. Provides assertion methods
        """
        super().__init__(browser, tester)

        self.plan_data = plan_data
