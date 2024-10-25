import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from unittest import TestCase

from .base_page import BasePage


class HomePage(BasePage):
    """ The Home page after logging in successfully"""

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def validate_page(self):
        self.await_page_load(f"{os.getenv('BASE_URL')}/")
        WebDriverWait(self.browser, 10).until(EC.title_is("Home - Risevest"))

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
