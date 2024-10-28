from dotenv import load_dotenv
import os
import unittest

from po.base_page import BasePage
from po.side_menu import SideMenu
from po.wallet_page import WalletPage

from utilities.driver_factory import DriverFactory
from utilities.driver_types import DriverTypes
from utilities.logs_handler import LogHandler
from utilities.commands import app_login


class TestWallet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load environment variables for the test runner
        load_dotenv()
        cls.base_url = os.getenv("BASE_URL")
        cls.browser = DriverFactory.get_random_driver()

        cls.username = os.getenv("ACCOUNT_USERNAME")
        cls.password = os.getenv("ACCOUNT_PASSWORD")

        cls.logger = LogHandler.create_logger()
        BasePage.set_logger(cls.logger)

        cls.logger.info("Initialized Web Browser")

    def setUp(self):
        self.browser.get(self.base_url)
        self.browser.maximize_window()
        app_login({"username": self.username,
                  "password": self.password}, self.browser, self)

        self.logger.info(f"{__class__}: Opened browser")

    def tearDown(self):
        self.browser.close()
        self.logger.info(f"{__class__}: Closed browser window")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        cls.browser = None
        cls.logger.info(f"{__class__}: Closed browser and session")

    def test_wallet_page_balance(self):
        """User should be able to view the wallet section"""
        side_menu = SideMenu(self.browser, self)
        side_menu.validate_page()
        side_menu.navigate_to_wallet()

        wallet_page = WalletPage(self.browser, self)
        wallet_page.validate_page()
        wallet_page.check_wallet_balance("$0.00")

    def test_wallet_page_toggle_balance(self):
        """User should be able to hide/show their wallet balance"""
        side_menu = SideMenu(self.browser, self)
        side_menu.validate_page()
        side_menu.navigate_to_wallet()

        wallet_page = WalletPage(self.browser, self)
        wallet_page.validate_page()
        wallet_page.toggle_wallet_balance_visibility()
        wallet_page.check_wallet_balance("******")

        wallet_page.toggle_wallet_balance_visibility()
        wallet_page.check_wallet_balance("$0.00")


if __name__ == "__main__":
    unittest.main(verbosity=2)
