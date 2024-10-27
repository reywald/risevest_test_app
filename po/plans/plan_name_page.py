from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from po.plans.plan_base_page import PlanBasePage


class PlanNamePage(PlanBasePage):
    """ The Plane name page """

    def __init__(self, browser, tester: TestCase, plan_data: dict):
        super().__init__(browser, tester, plan_data)

        self.HEADING = (By.CSS_SELECTOR, "form div.relative h2")
        self.BACK_BUTTON = (By.CSS_SELECTOR, "form div.relative button")
        self.QUESTION_TEXT = (By.CSS_SELECTOR, "form p:nth-child(1)")
        self.NAME_INPUT = (By.ID, "name")
        self.INPUT_TEXT = (By.CSS_SELECTOR, "form p:nth-child(3)")
        self.CONTINUE_BUTTON = (By.CSS_SELECTOR, "form button:nth-child(5)")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def fill_plan_name(self, plan_name: str):
        """ 
        Enter a plan name

        Params
        ------
        plan_name: str
            The name of the plan
        """
        name_input = self.get_element(self.NAME_INPUT)
        name_input.send_keys(Keys.CONTROL)
        name_input.send_keys("a")
        name_input.send_keys(
            plan_name if plan_name else self.plan_data["name"])

        self.logger.info(f"{__class__}: Entered a plan name")

    def click_continue(self):
        """ Click the continue button """
        continue_button = self.get_element(self.CONTINUE_BUTTON)
        continue_button.click()

    def validate_page(self):
        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(
            heading.text, "Plan name", "Heading text is not matched.")

        self.tester.assertIsNotNone(self.get_element(
            self.BACK_BUTTON), "Back button not detected.")

        question_text = self.get_element(self.QUESTION_TEXT)
        self.tester.assertEqual(
            question_text.text, "Question 1 of 3", "Question text is not matched.")

        input_prompt = self.get_element(self.INPUT_TEXT)
        self.tester.assertEqual(
            input_prompt.text, f"Give your {self.plan_data['type'].title()} plan a name", "Input text is not matched.")

        continue_button = self.get_element(self.CONTINUE_BUTTON)
        self.tester.assertEqual(
            continue_button.text, "Continue", "Continue button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
