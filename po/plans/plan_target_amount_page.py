from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from po.plans.plan_base_page import PlanBasePage


class PlanTargetAmountPage(PlanBasePage):
    """ The Target Amount page """

    def __init__(self, browser, tester: TestCase, plan_data: dict):
        super().__init__(browser, tester, plan_data)

        self.HEADING = (By.CSS_SELECTOR, "form div.relative h2")
        self.BACK_BUTTON = (By.CSS_SELECTOR, "form div.relative button")
        self.QUESTION_TEXT = (By.CSS_SELECTOR, "form p:nth-child(1)")
        self.NAME_INPUT = (By.ID, "name")
        self.INPUT_TEXT = (By.CSS_SELECTOR, "form p:nth-child(3)")
        self.PROMPT_TEXT = (By.CSS_SELECTOR, "form p:nth-child(2)")
        self.CONVERT_TEXT = (By.CSS_SELECTOR, "form p:nth-child(5)")
        self.CONTINUE_BUTTON = (By.CSS_SELECTOR, "form button:nth-child(6)")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def fill_target_amount(self, amount: str):
        """ 
        Enter a target amount

        Params
        ------
        amount: str
            The target amount
        """
        name_input = self.get_element(self.NAME_INPUT)
        name_input.send_keys(Keys.CONTROL)
        name_input.send_keys("a")
        name_input.send_keys(amount if amount else self.plan_data["amount"])

        self.logger.info(f"{__class__}: Entered an amount")

    def click_continue(self):
        """ Click the continue button """
        continue_button = self.get_element(self.CONTINUE_BUTTON)
        continue_button.click()

        self.logger.info(f"{__class__}: Clicked the continue button")

    def check_currency_conversion(self, amount: float):
        """
        Convert the amount to new currency using provided rate

        Params
        ------
        amount: float
            The amount to convert to
        """
        convert_text = self.get_element(self.CONVERT_TEXT)
        self.tester.assertEqual(f"${amount if amount else self.plan_data['investment_amount']}",
                                convert_text.text,
                                "Currency conversion figure is not matched.")

        self.logger.info(f"{__class__}: Checked currency conversion accuracy")

    def validate_page(self):
        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(
            heading.text, "Target Amount", "Heading text is not matched.")

        self.tester.assertIsNotNone(self.get_element(
            self.BACK_BUTTON), "Back button not detected.")

        question_text = self.get_element(self.QUESTION_TEXT)
        self.tester.assertEqual(question_text.text,
                                "Question 2 of 3",
                                "Question text is not matched.")

        input_text = self.get_element(self.INPUT_TEXT)
        self.tester.assertEqual(input_text.text,
                                f"How much do you need for your {self.plan_data['type'].lower()}?",
                                "Input text is not matched.")

        self.tester.assertIsNotNone(self.get_element(self.NAME_INPUT),
                                    "Amount input field not detected")

        prompt_text = self.get_element(self.PROMPT_TEXT)
        self.tester.assertEqual(prompt_text.text,
                                "Enter a target amount to continue",
                                "Prompt text is not matched.")

        convert_text = self.get_element(self.CONVERT_TEXT)
        self.tester.assertIn("0.00", convert_text.text,
                             "Input text is not matched.")

        continue_button = self.get_element(self.CONTINUE_BUTTON)
        self.tester.assertEqual(
            continue_button.text, "Continue", "Continue button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
