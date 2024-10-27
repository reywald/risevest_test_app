from dotenv import load_dotenv
import json
import os
import time
import unittest

from utilities.driver_types import DriverTypes
from utilities.driver_factory import DriverFactory
from utilities.logs_handler import LogHandler

from data.data_generator import DataTypes, get_credential_data

# Page Objects
from po.base_page import BasePage
from po.login_page import LoginPage
from po.home_page import HomePage
from po.side_menu import SideMenu


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load environment variables for the test runner
        load_dotenv()
        cls.base_url = os.getenv("BASE_URL")
        cls.browser = DriverFactory.get_driver(browser_type=DriverTypes.CHROME)

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

    def test_valid_login(self):
        login_page = LoginPage(self.browser, self)
        login_page.validate_page()
        username = os.getenv("ACCOUNT_USERNAME")
        password = os.getenv("ACCOUNT_PASSWORD")
        login_page.login(username=username, password=password)

        home_page = HomePage(self.browser, self)
        home_page.validate_page()

        side_menu = SideMenu(self.browser, self)
        side_menu.validate_page()

        time.sleep(4)

    def test_incorrect_email_login(self):
        login_page = LoginPage(self.browser, self)
        login_page.validate_page()
        password = os.getenv("ACCOUNT_PASSWORD")

        invalid_emails = get_credential_data(DataTypes.INVALID_EMAIL)
        for entry in invalid_emails:
            with self.subTest("Incorrect email"):
                login_page.login(username=entry["email"], password=password)
                login_page.check_form_error(
                    message="Invalid email or password.")

    def test_incorrect_password_login(self):
        login_page = LoginPage(self.browser, self)
        login_page.validate_page()
        username = os.getenv("ACCOUNT_USERNAME")

        invalid_passwords = get_credential_data(DataTypes.INVALID_PASSWORD)
        for entry in invalid_passwords:
            with self.subTest("Incorrect password"):
                login_page.login(username=username, password=entry["password"])
                login_page.check_form_error(
                    message="Invalid email or password.")

    def test_blank_email_login(self):
        login_page = LoginPage(self.browser, self)
        login_page.validate_page()
        username = ""
        password = os.getenv("ACCOUNT_PASSWORD")

        login_page.login(username=username, password=password)
        login_page.check_email_error(message="Enter your email address")

    def test_blank_password_login(self):
        login_page = LoginPage(self.browser, self)
        login_page.validate_page()
        username = os.getenv("ACCOUNT_USERNAME")
        password = ""

        login_page.login(username=username, password=password)
        login_page.check_password_error(message="Enter your password")


if __name__ == "__main__":
    unittest.main(verbosity=2)
