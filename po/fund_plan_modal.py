from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from po.base_page import BasePage


class FundPlanModal(BasePage):
    """ The Fund plan notifications modal after creating a plan """

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.NOTIFICATION_MODAL = (By.CSS_SELECTOR,
                                   'div[data-test-id="fund-plan-modal"]')
        self.CLOSE_BUTTON = (By.CSS_SELECTOR,
                             'div[data-test-id="fund-plan-modal"]'
                             ' div.relative button')
        self.HEADING = (By.CSS_SELECTOR,
                        "//h2[contains(text(), 'add money')]")
        self.MESSAGE = (By.XPATH,
                        "//p[contains(text(), 'fund your plan?')]")
        self.ADD_MONEY_BUTTON = (By.XPATH,
                                 "//button[text()='Yes, add money now.']")
        self.NO_BUTTON = (By.XPATH, "//button[text()='No, later']")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def close_modal(self):
        """
        Close the notifications modal
        """
        no_button = self.get_element(self.NO_BUTTON)
        no_button.click()

        self.logger.info(f"{__class__}: Closed the notifications modal")

    def confirm_modal_closed(self):
        """
        Confirm the modal is closed
        """
        WebDriverWait(self.browser, 20).until(
            EC.invisibility_of_element(self.HEADING))

        self.logger.info(
            f"{__class__}: Checked that the notifications modal is closed")

    def validate_page(self):
        self.get_element(self.NOTIFICATION_MODAL)
        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(heading.text,
                                "Would you like to add money now?",
                                "Heading not detected.")

        self.tester.assertIsNotNone(self.get_element(self.ICON),
                                    "No icon detected.")

        fund_prompt = self.get_element(self.MESSAGE)
        self.tester.assertEqual(fund_prompt.text,
                                "You currently are low on Plan funds."
                                " Would you like to fund your plan?",
                                "Fund prompt is not matched.")

        yes_button = self.get_element(self.ADD_MONEY_BUTTON)
        self.tester.assertEqual(yes_button.text, "Yes, add money now.",
                                "Yes button text is not matched.")

        no_button = self.get_element(self.NO_BUTTON)
        self.tester.assertEqual(no_button.text, "No, later",
                                "No button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
