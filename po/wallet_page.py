from unittest import TestCase
from selenium.webdriver.common.by import By
from po.base_page import BasePage


class WalletPage(BasePage):
    """ The wallet page of the user """

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.WALLET_ICON = (By.CSS_SELECTOR, "div.h-full-page > header > svg")
        self.NOTIFICATION_BUTTON = (
            By.CSS_SELECTOR, "div.h-full-page > header button")
        self.WALLET_HEADING = (
            By.CSS_SELECTOR, "#wallet-tab-panel > p:first-child > span")
        self.WALLET_TOGGLE = (
            By.CSS_SELECTOR, "#wallet-tab-panel > p:first-child > button")
        self.WALLET_BALANCE = (
            By.CSS_SELECTOR, "#wallet-tab-panel > p:nth-child(2)")

    def check_wallet_balance(self, wallet_amount: str):
        """
        Checks that the wallet balance is correct

        Params
        ------
        wallet_amount: str - The string to compare to
        """
        wallet_balance = self.get_element(self.WALLET_BALANCE)
        self.tester.assertEqual(wallet_balance.text, wallet_amount,
                                "Wallet balance is not matched.")

    def toggle_wallet_balance_visibility(self):
        """
        Click the wallet toggle button to show/hide the wallet balance
        """
        wallet_toggle = self.get_element(self.WALLET_TOGGLE)
        wallet_toggle.click()

    def is_wallet_balance_hidden(self) -> bool:
        """
        Verifies if the wallet balance is shown or hidden.
        If 'asterisks' characters are present, then it is hidden
        """
        wallet_balance = self.get_element(self.WALLET_BALANCE)
        return "*" in wallet_balance.text

    def validate_page(self):
        self.tester.assertIsNotNone(self.get_element(
            self.WALLET_ICON), "Wallet icon not detected.")
        self.tester.assertIsNotNone(self.get_element(
            self.NOTIFICATION_BUTTON), "Notification button not detected.")

        wallet_heading = self.get_element(self.WALLET_HEADING)
        self.tester.assertEqual(
            wallet_heading.text, "Wallet Balance", "Heading text is not matched.")

        self.tester.assertIsNotNone(self.get_element(
            self.WALLET_TOGGLE), "Show/Hide button not detected.")

        self.tester.assertIsNotNone(self.get_element(
            self.WALLET_BALANCE), "Wallet balance not detected.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
