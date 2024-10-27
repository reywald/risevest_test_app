from selenium.webdriver.common.by import By
from unittest import TestCase

from po.base_page import BasePage


class GoalsPanel(BasePage):
    """ The Goals on the Plans page"""

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.GOAL_CONTAINER = (
            By.CSS_SELECTOR, "[data-test-id='goal-plans']")
        self.BUSINESS_LINK = (
            By.CSS_SELECTOR, "a[href='/plans/goal/business']")
        self.SCHOOL_LINK = (By.CSS_SELECTOR, "a[href='/plans/goal/school']")
        self.WEDDING_LINK = (By.CSS_SELECTOR, "a[href='/plans/goal/wedding']")
        self.TRAVEL_LINK = (By.CSS_SELECTOR, "a[href='/plans/goal/travel']")
        self.HOME_LINK = (By.CSS_SELECTOR, "a[href='/plans/goal/home']")
        self.KIDS_LINK = (By.CSS_SELECTOR, "a[href='/plans/goal/kids']")
        self.RENT_LINK = (By.CSS_SELECTOR, "a[href='/plans/goal/rent']")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def click_business_goal(self):
        """ Click the business goal link """
        business_link = self.get_element(self.BUSINESS_LINK)
        business_link.click()

        self.logger.info(f"{__class__}: Clicked Business goal link")

    def click_school_goal(self):
        """ Click the school goal link """
        school_link = self.get_element(self.SCHOOL_LINK)
        school_link.click()

        self.logger.info(f"{__class__}: Clicked School goal link")

    def click_wedding_goal(self):
        """ Click the wedding goal link """
        wedding_link = self.get_element(self.WEDDING_LINK)
        wedding_link.click()

        self.logger.info(f"{__class__}: Clicked Wedding goal link")

    def click_travel_goal(self):
        """ Click the travel goal link """
        travel_link = self.get_element(self.TRAVEL_LINK)
        travel_link.click()

        self.logger.info(f"{__class__}: Clicked Travel goal link")

    def click_home_goal(self):
        """ Click the home goal link """
        home_link = self.get_element(self.HOME_LINK)
        home_link.click()

        self.logger.info(f"{__class__}: Clicked Home goal link")

    def click_kids_goal(self):
        """ Click the kids goal link """
        kids_link = self.get_element(self.KIDS_LINK)
        kids_link.click()

        self.logger.info(f"{__class__}: Clicked Kids goal link")

    def click_rent_goal(self):
        """ Click the rent goal link """
        rent_link = self.get_element(self.RENT_LINK)
        rent_link.click()

        self.logger.info(f"{__class__}: Clicked Rent goal link")

    def validate_page(self):
        self.tester.assertIsNotNone(self.get_element(
            self.GOAL_CONTAINER), "Goals not detected.")

        business_link = self.get_element(self.BUSINESS_LINK)
        self.tester.assertEqual(
            business_link.text, "Start a Business", "Business goal link text not matched.")

        school_link = self.get_element(self.SCHOOL_LINK)
        self.tester.assertEqual(
            school_link.text, "Save for School", "School goal link text not matched.")

        wedding_link = self.get_element(self.WEDDING_LINK)
        self.tester.assertEqual(
            wedding_link.text, "Plan a Wedding", "Wedding goal link text not matched.")

        travel_link = self.get_element(self.TRAVEL_LINK)
        self.tester.assertEqual(travel_link.text, "Travel",
                                "Travel goal link text not matched.")

        home_link = self.get_element(self.HOME_LINK)
        self.tester.assertEqual(
            home_link.text, "Own Your Own Home", "Home goal link text not matched.")

        kids_link = self.get_element(self.KIDS_LINK)
        self.tester.assertEqual(kids_link.text, "Kids",
                                "Kids goal link text not matched.")

        rent_link = self.get_element(self.RENT_LINK)
        self.tester.assertEqual(
            rent_link.text, "Save for Rent", "Rent goal link text not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
