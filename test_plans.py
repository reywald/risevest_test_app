import time
from dotenv import load_dotenv
import os
import unittest

from po.base_page import BasePage
from po.assets_panel import AssetsPanel
from po.goals_panel import GoalsPanel
from po.side_menu import SideMenu
from po.plan_page import PlansPage
from po.plans.plan_intro_page import PlanIntroPage
from po.plans.plan_name_page import PlanNamePage
from po.plans.plan_currency_choice_page import PlanCurrencyPage
from po.plans.plan_target_amount_page import PlanTargetAmountPage
from po.plans.plan_target_date_page import PlanTargetDatePage
from po.plans.plan_review_page import PlanReviewPage
from po.plans.plans_success_page import PlanSuccessPage

from data.data_generator import PlanTypes, get_plan_data, calculate_plan_stats

from utilities.driver_factory import DriverFactory
from utilities.driver_types import DriverTypes
from utilities.logs_handler import LogHandler
from utilities.commands import app_login


class TestPlans(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load environment variables for the test runner
        load_dotenv()
        cls.base_url = os.getenv("BASE_URL")
        cls.browser = DriverFactory.get_random_driver()

        cls.username = os.getenv("ACCOUNT_USERNAME")
        cls.password = os.getenv("ACCOUNT_PASSWORD")

        cls.logger = LogHandler.create_logger()
        BasePage.set_logger(cls.logger)

        cls.logger.info(f"{__class__}: Initialized Web Browser")

    def setUp(self):
        self.browser.get(self.base_url)
        self.browser.maximize_window()
        self.logger.info(f"{__class__}: Opened browser")
        app_login({"username": self.username,
                  "password": self.password}, self.browser, self)

    def tearDown(self):
        self.browser.close()
        self.logger.info(f"{__class__}: Closed browser window")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        cls.browser = None
        cls.logger.info(f"{__class__}: Closed browser and session")

    def test_view_plans_page(self):
        """User should be able to view plans"""
        side_menu = SideMenu(self.browser, self)
        side_menu.validate_page()
        side_menu.navigate_to_plans()

        plans_page = PlansPage(self.browser, self)
        plans_page.validate_page()

        assets_panel = AssetsPanel(self.browser, self)
        assets_panel.validate_page()

        goals_panel = GoalsPanel(self.browser, self)
        goals_panel.validate_page()

    def test_create_business_plan(self):
        """User should be able to create a new investment plan"""
        side_menu = SideMenu(self.browser, self)
        side_menu.validate_page()
        side_menu.navigate_to_plans()

        business_plans = get_plan_data(PlanTypes.BUSINESS_PLAN)

        for business_plan in business_plans:
            with self.subTest(business_plan["type"]):
                goals_panel = GoalsPanel(self.browser, self)
                goals_panel.validate_page()
                goals_panel.click_business_goal()

                calculate_plan_stats(business_plan)

                intro_page = PlanIntroPage(self.browser, self, business_plan)
                intro_page.validate_page()
                intro_page.click_continue()

                name_page = PlanNamePage(self.browser, self, business_plan)
                name_page.validate_page()
                name_page.fill_plan_name(business_plan["name"])
                name_page.click_continue()

                currency_page = PlanCurrencyPage(self.browser, self)
                currency_page.validate_page()
                currency_page.choose_naira()

                amount_page = PlanTargetAmountPage(
                    self.browser, self, business_plan)
                amount_page.validate_page()
                amount_page.fill_target_amount(business_plan["amount"])
                amount_page.check_currency_conversion(
                    round(business_plan["investment_amount"], 2)
                )
                amount_page.click_continue()

                date_page = PlanTargetDatePage(
                    self.browser, self, business_plan)
                date_page.validate_page()
                date_page.fill_target_date(business_plan["maturity_date"])
                date_page.click_continue()

                # review_page = PlanReviewPage(self.browser, self, business_plan)
                # review_page.validate_page()
                # review_page.check_interest_rate()
                # review_page.check_investment_amount()
                # review_page.check_recurring_investment()
                # review_page.check_returns_amount()
                # review_page.check_maturity_amount()
                # review_page.click_continue()

                # success_page = PlanSuccessPage(self.browser, self)
                # success_page.validate_page()
                # success_page.click_view_plan_button()
                time.sleep(4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
