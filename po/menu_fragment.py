import os
from selenium.webdriver.common.by import By
from unittest import TestCase

from .base_page import BasePage


class SideMenu(BasePage):
    """ The Side menu of the page after logging in successfully"""

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.LOGO = (By.CSS_SELECTOR, "main + div > svg")
        self.HOME_MENU = (By.CSS_SELECTOR, "main + div > a[href='/']")
        self.HOME_MENU_ICON = (By.CSS_SELECTOR, "main + div > a[href='/'] svg")
        self.PLANS_MENU = (By.CSS_SELECTOR, "main + div > a[href='/plans']")
        self.WALLET_MENU = (By.CSS_SELECTOR, "main + div > a[href='/wallet']")
        self.FEED_MENU = (By.CSS_SELECTOR, "main + div > a[href='/feed']")
        self.MORE_MENU = (By.CSS_SELECTOR, "main + div > a[href='/account']")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def navigate_to_wallet(self):
        """
        Click the Wallet link to open the wallet page
        """
        wallet_link = self.get_element(self.WALLET_MENU)
        wallet_link.click()

        self.tester.assertIsNotNone(wallet_link.get_attribute("aria-current"))
        self.tester.assertEqual(
            wallet_link.get_attribute("aria-current"), "page")

        self.logger.info(f"{__class__}: Navigated to wallet page")

    def validate_page(self):
        menu_logo = self.get_element(self.LOGO)
        self.tester.assertIsNotNone(menu_logo, "Logo not detected.")

        home_menu = self.get_element(self.HOME_MENU)
        self.tester.assertEqual(home_menu.text, "Home")

        plans_menu = self.get_element(self.PLANS_MENU)
        self.tester.assertEqual(plans_menu.text, "Plans")

        wallet_menu = self.get_element(self.WALLET_MENU)
        self.tester.assertEqual(wallet_menu.text, "Wallet")

        feed_menu = self.get_element(self.FEED_MENU)
        self.tester.assertEqual(feed_menu.text, "Feed")

        account_menu = self.get_element(self.MORE_MENU)
        self.tester.assertEqual(account_menu.text, "More")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
