from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from po.plans.plan_base_page import PlanBasePage


class PlanReviewPage(PlanBasePage):
    """ The Plan review page """

    def __init__(self, browser, tester: TestCase, plan_data: dict):
        super().__init__(browser, tester, plan_data)

        self.HEADING = (By.CSS_SELECTOR, "form div.relative h2")
        self.BACK_BUTTON = (By.CSS_SELECTOR, "form div.relative button")
        self.PLAN_TYPE = (
            By.CSS_SELECTOR, "form div.relative + div > p:first-child")
        self.PLAN_MATURITY_AMOUNT = (
            By.CSS_SELECTOR, "form div.relative + div > p:nth-child(2)")
        self.PLAN_DATE = (
            By.CSS_SELECTOR, "form div.relative + div > p:nth-child(3)")
        self.PLAN_INVESTMENT_AMOUNT = (
            By.XPATH, "//form//p[contains(text(),'Investments')]")
        self.PLAN_INVESTMENT_RETURN = (
            By.XPATH, "//form//p[contains(text(),'Returns $')]")
        self.PLAN_NAME = (
            By.XPATH, "//form//p[contains(text(), 'Plan Name')]/following-sibling::p")
        self.PLAN_INTEREST_RATE = (
            By.XPATH, "//form//p[contains(text(), 'interest rate')]/following-sibling::p")
        self.PLAN_RECURRING_RETURN = (
            By.XPATH, "//form//p[contains(text(), 'recurring')]/following-sibling::p")
        self.DISCLOSURE_LINK = (By.LINK_TEXT, "Read our Disclosures")
        self.CONTINUE_BUTTON = (
            By.XPATH, "//form//button[text()='Agree & Continue']")
        self.START_OVER_BUTTON = (
            By.XPATH, "//form//button[text()='Start Over']")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def check_investment_amount(self, amount: float):
        """ 
        Checks the investment amount

        Params
        ------
        amount: float
            The investment amount to check against
        """
        investment_amount = self.get_element(self.PLAN_INVESTMENT_AMOUNT)
        self.tester.assertIn(f"${round(amount, 2)}", investment_amount.text,
                             "Investment amount not matched.")

        self.logger.info(f"{__class__}: Checked Investment amount")

    def check_interest_rate(self, est_interest_rate: float):
        """
        Check the estimated interest rate, which is the product of 
        the rate by the time period

        Params
        ------
        est_interest_rate: float
            The calculated interest rate to check against
        """
        investment_rate = self.get_element(self.PLAN_INTEREST_RATE)
        self.tester.assertIn(f"{round(est_interest_rate, 2)}%", investment_rate.text,
                             "Interest rate not matched.")

        self.logger.info(f"{__class__}: Checked Interest rate")

    def check_recurring_investment(self, est_recurring_amount: float):
        """
        Check the recurring investment amount, which is the product of
        the investment amount and the period in months

        Params
        ------
        est_recurring_amount: float
            The calculated recurring amount to check against
        """
        recurring_return = self.get_element(self.PLAN_RECURRING_RETURN)
        self.tester.assertEqual(f"${round(est_recurring_amount, 2)}", recurring_return.text,
                                "Recurring Investment amount not matched.")

        self.logger.info(f"{__class__}: Checked Recurring return")

    def check_returns_amount(self, returns_amount: float):
        """
        Check the returns amount, which is the product of
        the investment amount and estimated rate

        Params
        ------
        returns_amount: float
            The calculated investment return amount to check against
        """
        investment_return = self.get_element(self.PLAN_INVESTMENT_RETURN)
        self.tester.assertEqual(f"${round(returns_amount, 2)}", investment_return.text,
                                "Investment Returns not matched.")

        self.logger.info(f"{__class__}: Checked Recurring return")

    def check_maturity_amount(self, maturity_amount: float):
        """
        Check the maturity amount, which is the sum of
        the investment amount and investment return

        Params
        ------
        maturity_amount: float
            The calculated investment maturity amount to check against
        """
        full_amount = self.get_element(self.PLAN_MATURITY_AMOUNT)
        self.tester.assertEqual(f"${round(maturity_amount, 2)}", full_amount.text,
                                "Investment Returns not matched.")

        self.logger.info(f"{__class__}: Checked Investment return")

    def click_continue(self):
        """ Click the Agree & Continue button """
        continue_button = self.get_element(self.CONTINUE_BUTTON)
        continue_button.click()

    def validate_page(self):
        WebDriverWait(self.browser, 20).until(EC.url_contains("stage=review"))

        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(
            heading.text, "Review", "Heading text is not matched.")

        self.tester.assertIsNotNone(self.get_element(
            self.BACK_BUTTON), "Back button not detected.")

        plan_text = self.get_element(self.PLAN_TYPE)
        self.tester.assertEqual(plan_text.text, self.plan_data['type'].title(),
                                "Plan text is not matched.")

        full_amount = self.get_element(self.PLAN_MATURITY_AMOUNT)
        self.tester.assertEqual(f"${round(self.plan_data['maturity_amount'], 2)}", full_amount.text,
                                "Investment Returns not matched.")

        investment_amount = self.get_element(
            self.PLAN_INVESTMENT_AMOUNT)
        self.tester.assertIn(f"Investments ${round(self.plan_data['investment_amount'], 2)}",
                             investment_amount.text, "Investment amount not matched.")

        investment_return = self.get_element(
            self.PLAN_INVESTMENT_RETURN)
        self.tester.assertEqual(f"Returns ${round(self.plan_data['returns_amount'], 2)}",
                                investment_return.text, "Investment Returns not matched.")

        plan_name = self.get_element(self.PLAN_NAME)
        self.tester.assertEqual(plan_name.text, self.plan_data['name'],
                                "Plan name is not matched.")

        interest_rate = self.get_element(self.PLAN_INTEREST_RATE)
        self.tester.assertIn(f"{round(self.plan_data['est_interest_rate'])}%",
                             interest_rate.text, "Estimated Interest Rate not matched.")

        self.tester.assertIn(
            f"{self.plan_data['period']} months", interest_rate.text, "Investment period not matched.")

        disclosure_link = self.get_element(self.DISCLOSURE_LINK)
        self.tester.assertEqual(
            disclosure_link.text, "Read our Disclosures", "Disclosure link text is not matched.")

        continue_button = self.get_element(self.CONTINUE_BUTTON)
        self.tester.assertEqual(
            continue_button.text, "Agree & Continue", "Continue button text is not matched.")

        start_over_button = self.get_element(self.START_OVER_BUTTON)
        self.tester.assertEqual(
            start_over_button.text, "Start Over", "Start over button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
