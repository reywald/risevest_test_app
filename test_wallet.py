from dotenv import load_dotenv
import os
import unittest

from po.base_page import BasePage
from po.login_page import LoginPage
from po.home_page import HomePage
from po.notifications_fragment import NotificationsModal
from po.confirm_notifications_fragment import ConfirmNotificationsModal
from po.menu_fragment import SideMenu
from po.wallet_page import WalletPage

from utilities.driver_factory import DriverFactory
from utilities.driver_types import DriverTypes
from utilities.logs_handler import LogHandler


class TestWallet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load environment variables for the test runner
        load_dotenv()
        cls.base_url = os.getenv("BASE_URL")
        cls.browser = DriverFactory.get_driver(
            browser_type=DriverTypes.FIREFOX)

        cls.username = os.getenv("ACCOUNT_USERNAME")
        cls.password = os.getenv("ACCOUNT_PASSWORD")

        cls.logger = LogHandler.create_logger()
        BasePage.set_logger(cls.logger)

        cls.logger.info("Initialized Web Browser")

    def setUp(self):
        self.browser.get(self.base_url)
        self.browser.maximize_window()

        self.logger.info(f"{__class__}: Opened browser")

    def tearDown(self):
        self.browser.close()
        self.logger.info(f"{__class__}: Closed browser window")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        cls.browser = None
        cls.logger.info(f"{__class__}: Closed browser and session")

    def access_wallet_page(self):
        login_page = LoginPage(self.browser, self)
        login_page.validate_page()
        login_page.login(username=self.username, password=self.password)

        home_page = HomePage(self.browser, self)
        home_page.validate_page()

        notifications_modal = NotificationsModal(self.browser, self)
        notifications_modal.validate_page()
        notifications_modal.cancel_modal()
        notifications_modal.confirm_modal_changed()

        confirm_modal = ConfirmNotificationsModal(self.browser, self)
        confirm_modal.validate_page()
        confirm_modal.close_modal()
        confirm_modal.confirm_modal_closed()

        side_menu = SideMenu(self.browser, self)
        side_menu.validate_page()
        side_menu.navigate_to_wallet()

    def test_wallet_page_balance(self):
        self.access_wallet_page()

        wallet_page = WalletPage(self.browser, self)
        wallet_page.validate_page()
        wallet_page.check_wallet_balance("$0.00")

    def test_wallet_page_toggle_balance(self):
        self.access_wallet_page()

        wallet_page = WalletPage(self.browser, self)
        wallet_page.validate_page()
        wallet_page.toggle_wallet_balance_visibility()
        wallet_page.check_wallet_balance("******")

        wallet_page.toggle_wallet_balance_visibility()
        wallet_page.check_wallet_balance("$0.00")


if __name__ == "__main__":
    unittest.main(verbosity=2)
