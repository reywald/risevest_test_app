from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from po.base_page import BasePage


class PlanCurrencyPage(BasePage):
    """ The Select Currency page """

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.HEADING = (By.XPATH, '//h2[text()="Select Currency"]')
        self.BACK_BUTTON = (By.CSS_SELECTOR, "form div.relative button")
        self.DESCRIPTION = (By.CSS_SELECTOR, "form p")
        self.NGN_BUTTON = (By.CSS_SELECTOR, "form ul > li:nth-child(1)")
        self.USD_BUTTON = (By.CSS_SELECTOR, "form ul > li:nth-child(2)")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def choose_naira(self):
        """ Click the Naira button """
        ngn_button = self.get_element(self.NGN_BUTTON)
        ngn_button.click()

        self.logger.info(f"{__class__}: Clicked the Naira button")

    def choose_usd(self):
        """ Click the Dollar button """
        usd_button = self.get_element(self.USD_BUTTON)
        usd_button.click()

        self.logger.info(f"{__class__}: Clicked the Dollar button")

    def validate_page(self):
        WebDriverWait(self.browser, 20).until(
            EC.url_contains("stage=currency"))

        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(
            heading.text, "Select Currency", "Heading text is not matched.")

        self.tester.assertIsNotNone(self.get_element(
            self.BACK_BUTTON), "Back button not detected.")

        # page_description = self.get_element(self.DESCRIPTION)
        # self.tester.assertIn(
        #     "In which currency", page_description.text, "Description text is not matched.")

        ngn_button = self.get_element(self.NGN_BUTTON)
        self.tester.assertIn("Nigerian Naira", ngn_button.text,
                             "Naira button text is not matched.")

        usd_button = self.get_element(self.USD_BUTTON)
        self.tester.assertIn("US Dollar", usd_button.text,
                             "Dollar button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
