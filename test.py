from dotenv import load_dotenv
import os
import time
import unittest

from utilities.driver_types import DriverTypes
from utilities.driver_factory import DriverFactory


class RiseVestTester(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load environment variables for the test runner
        load_dotenv()
        cls.base_url = os.getenv("BASE_URL")
        cls.browser = DriverFactory.get_driver(
            browser_type=DriverTypes.EDGE)

    def setUp(self):
        self.browser.get(self.base_url)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    @classmethod
    def tearDownClass(cls):
        cls.browser = None

    def test_login(self):
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
