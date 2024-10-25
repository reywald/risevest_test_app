from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from po.base_page import BasePage


class PlanPage(BasePage):
    """ The Plans page of the user """

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.PLANS_HEADING = (
            By.CSS_SELECTOR, "header > h1")
        self.PLANS_BUTTON = (By.ID, "plans-tab-control")
        self.PORTFOLIO_BUTTON = (By.ID, "portfolio-tab-control")
        self.PLANS_PANEL = (
            By.CSS_SELECTOR, "[role='tabpanel']:not([class='hidden'])")
        self.SUB_HEADINGS = (
            By.CSS_SELECTOR, "[role='tabpanel']:not([class='hidden']) h2")
        self.NO_PLANS_TEXT = (
            By.XPATH, "//div[@role='tabpanel'][1]/div/div/div[2]/p")

    # def check_wallet_balance(self, wallet_amount: str):
    #     """
    #     Checks that the wallet balance is correct

    #     Params
    #     ------
    #     wallet_amount: str - The string to compare to
    #     """
    #     wallet_balance = self.get_element(self.WALLET_BALANCE)
    #     self.tester.assertEqual(wallet_balance.text, wallet_amount,
    #                             "Wallet balance is not matched.")

    # def toggle_wallet_balance_visibility(self):
    #     """
    #     Click the wallet toggle button to show/hide the wallet balance
    #     """
    #     wallet_toggle = self.get_element(self.WALLET_TOGGLE)
    #     wallet_toggle.click()

    # def is_wallet_balance_hidden(self) -> bool:
    #     """
    #     Verifies if the wallet balance is shown or hidden.
    #     If 'asterisks' characters are present, then it is hidden
    #     """
    #     wallet_balance = self.get_element(self.WALLET_BALANCE)
    #     return "*" in wallet_balance.text

    def validate_page(self):
        plans_heading = self.get_element(self.PLANS_HEADING)
        self.tester.assertEqual(
            plans_heading.text, "Plans", "Heading text is not matched.")

        plans_tab_button = self.get_element(self.PLANS_BUTTON)
        self.tester.assertEqual(
            plans_tab_button.text, "Plans", "Tab button text is not matched.")

        portfolio_tab_button = self.get_element(self.PORTFOLIO_BUTTON)
        self.tester.assertEqual(
            portfolio_tab_button.text, "Portfolio", "Tab button text is not matched.")

        self.tester.assertIsNotNone(self.get_element(
            self.PLANS_PANEL), "Plans panel not detected.")

        no_plans_text = self.get_element(self.NO_PLANS_TEXT)
        self.tester.assertIn(
            "You have not created any plans.", no_plans_text.text)

        sub_headings: list[WebElement] = self.get_elements(self.SUB_HEADINGS)
        self.tester.assertIsNotNone(sub_headings, "Sub-headings not detected.")
        self.tester.assertEqual(len(sub_headings), 4,
                                "Count of Sub-headings inaccurate.")

        for sub_heading in sub_headings:
            self.tester.assertIn(sub_heading.text, [
                                 "Your plans", "Asset classes", "Goals", "Your matured plans"])

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
