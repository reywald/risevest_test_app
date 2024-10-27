from unittest import TestCase
from selenium.webdriver.common.by import By
from po.plans.plan_base_page import PlanBasePage


class PlanIntroPage(PlanBasePage):
    """ The Introductory plan page """

    def __init__(self, browser, tester: TestCase, plan_data: dict):
        super().__init__(browser, tester, plan_data)

        self.HEADING = (By.CSS_SELECTOR, "header h2")
        self.BACK_BUTTON = (By.CSS_SELECTOR, "header button")
        self.ICON = (By.CSS_SELECTOR, "header.relative ~ img")
        self.SUB_HEADING = (By.CSS_SELECTOR, "header.relative ~ p")
        self.CONTINUE_BUTTON = (
            By.XPATH, "//header/following-sibling::button")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def click_continue(self):
        """ Click the Continue button """
        continue_button = self.get_element(self.CONTINUE_BUTTON)
        continue_button.click()

        self.logger.info(f"{__class__}: Clicked the continue button")

    def validate_page(self):
        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(
            heading.text, self.plan_data["title"], "Heading text is not matched.")

        sub_heading = self.get_element(self.SUB_HEADING)
        self.tester.assertEqual(
            sub_heading.text, self.plan_data["subtitle"], "Sub-heading text is not matched.")

        self.tester.assertIsNotNone(self.get_element(
            self.BACK_BUTTON), "Back button not detected.")

        self.tester.assertIsNotNone(self.get_element(
            self.ICON), "Plan icon is not detected.")

        continue_button = self.get_element(self.CONTINUE_BUTTON)
        self.tester.assertEqual(
            continue_button.text, "Continue", "Continue button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
