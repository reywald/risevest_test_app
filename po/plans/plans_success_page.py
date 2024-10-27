from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from po.base_page import BasePage


class PlanSuccessPage(BasePage):
    """ The success page after completing plan creation """

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.HEADING = (By.CSS_SELECTOR, "main h2")
        self.ICON = (By.CSS_SELECTOR, "main svg")
        self.MESSAGE = (By.CSS_SELECTOR, "main p")
        self.VIEW_PLAN_BUTTON = (By.CSS_SELECTOR, "main button")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def click_view_plan_button(self):
        """
        Click the View Plan button to navigate back to the Plans page
        """
        ok_button = self.get_element(self.VIEW_PLAN_BUTTON)
        ok_button.click()

        self.logger.info(f"{__class__}: Closed success page")

    def validate_page(self):
        self.get_element(self.NOTIFICATION_MODAL)
        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(heading.text,
                                "You just created your Business plan.",
                                "Heading not detected.")

        self.tester.assertIsNotNone(self.get_element(self.ICON),
                                    "No icon detected.")

        message = self.get_element(self.MESSAGE)
        self.tester.assertIn("Well done, IKECHUKWU", message.text,
                             "Message text is not matched.")

        ok_button = self.get_element(self.VIEW_PLAN_BUTTON)
        self.tester.assertEqual(
            ok_button.text, "View Plan", "View plan button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
