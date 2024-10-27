from selenium.webdriver.common.by import By
from unittest import TestCase

from po.base_page import BasePage


class AssetsPanel(BasePage):
    """ The Asset classes on the Plans page"""

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.ASSET_CONTAINER = (
            By.CSS_SELECTOR, "[data-test-id='asset-classes']")
        self.NEW_STOCKS_LINK = (By.CSS_SELECTOR, "a[href='/plans/new/stocks']")
        self.NEW_FIXED_INCOME_LINK = (
            By.CSS_SELECTOR, "a[href='/plans/new/fixed-income']")
        self.NEW_REAL_ESTATE_LINK = (
            By.CSS_SELECTOR, "a[href='/plans/new/real-estate']")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def create_stocks_plan(self):
        """ Click the Stocks link """
        stocks_link = self.get_element(self.NEW_STOCKS_LINK)
        stocks_link.click()

        self.logger.info(f"{__class__}: Clicked Stocks link")

    def create_fixed_income_plan(self):
        """ Click the Fixed Income link """
        fixed_income_link = self.get_element(self.NEW_FIXED_INCOME_LINK)
        fixed_income_link.click()

        self.logger.info(f"{__class__}: Clicked Fixed Income link")

    def create_real_estate_plan(self):
        """ Click the Real Estate link """
        real_estate_link = self.get_element(self.NEW_REAL_ESTATE_LINK)
        real_estate_link.click()

        self.logger.info(f"{__class__}: Clicked Real Estate link")

    def validate_page(self):
        self.tester.assertIsNotNone(self.get_element(
            self.ASSET_CONTAINER), "Asset classes not detected")

        stocks_link = self.get_element(self.NEW_STOCKS_LINK)
        self.tester.assertIn("Stocks", stocks_link.text,
                             "Stocks link text not matched.")

        fixed_income_link = self.get_element(self.NEW_FIXED_INCOME_LINK)
        self.tester.assertIn(
            "Fixed Income", fixed_income_link.text, "Fixed income link text not matched.")

        real_estate_link = self.get_element(self.NEW_REAL_ESTATE_LINK)
        self.tester.assertIn("Real Estate", real_estate_link.text,
                             "Real estate link text not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
