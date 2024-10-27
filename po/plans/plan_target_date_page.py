from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from po.plans.plan_base_page import PlanBasePage


class PlanTargetDatePage(PlanBasePage):
    """ The Target Date page """

    def __init__(self, browser, tester: TestCase, plan_data: dict):
        super().__init__(browser, tester, plan_data)

        self.HEADING = (By.CSS_SELECTOR, "form div.relative h2")
        self.BACK_BUTTON = (By.CSS_SELECTOR, "form div.relative button")
        self.QUESTION_TEXT = (By.CSS_SELECTOR, "form p:nth-child(1)")
        self.DATE_INPUT = (By.ID, "mui-2")
        self.INPUT_TEXT = (By.CSS_SELECTOR, "form p:nth-child(3)")
        self.CONTINUE_BUTTON = (By.CSS_SELECTOR, "form button:nth-child(5)")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def fill_target_date(self, target_date: str):
        """ 
        Enter a target date

        Params
        ------
        target_date: str
            The target date
        """
        name_input = self.get_element(self.DATE_INPUT)
        name_input.send_keys(Keys.CONTROL)
        name_input.send_keys("a")
        name_input.send_keys(
            target_date if target_date else self.plan_data["maturity_date"])

        self.logger.info(f"{__class__}: Entered a date")

    def __check_default_target_date(self):
        """
        Check if the default date is 3 months minimum
        """
        from datetime import date
        from dateutil.relativedelta import relativedelta

        maturity_date = date.today() + relativedelta(months=3)
        maturity_text = maturity_date.strftime("%d-%m-%Y")

        input_text = self.get_element(self.INPUT_TEXT)
        self.tester.assertEqual(input_text.text, maturity_text)

        self.logger.info(f"{__class__}: Checked validity of date")

    def click_continue(self):
        """ Click the continue button """
        continue_button = self.get_element(self.CONTINUE_BUTTON)
        continue_button.click()

        self.logger.info(f"{__class__}: Clicked the continue button")

    def validate_page(self):
        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(
            heading.text, "Target Date", "Heading text is not matched.")

        self.tester.assertIsNotNone(self.get_element(
            self.BACK_BUTTON), "Back button not detected.")

        question_text = self.get_element(self.QUESTION_TEXT)
        self.tester.assertEqual(question_text.text,
                                "Question 3 of 3",
                                "Question text is not matched.")

        input_text = self.get_element(self.INPUT_TEXT)
        self.tester.assertEqual(input_text.text,
                                f"When do you want to start your {self.plan_data['type'].lower()}?",
                                "Input text is not matched.")

        self.tester.assertIsNotNone(self.get_element(self.DATE_INPUT),
                                    "Date input field not detected")

        self.__check_default_target_date()

        continue_button = self.get_element(self.CONTINUE_BUTTON)
        self.tester.assertEqual(
            continue_button.text, "Continue", "Continue button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
