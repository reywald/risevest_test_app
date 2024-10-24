import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from unittest import TestCase

from .base_page import BasePage


class LoginPage(BasePage):
    """ The login page"""

    def __init__(self, browser, tester: TestCase):
        """Assign elements to the page members"""
        super().__init__(browser, tester)

        self.LOGO = (By.CSS_SELECTOR, "aside > svg")
        self.CATCHPRASE = (By.CSS_SELECTOR, "aside > p")
        self.HEADING = (By.CLASS_NAME, "text-title")
        self.SUB_HEADING = (By.CLASS_NAME, "text-soft")
        self.EMAIL_LABEL = (By.ID, "email-label")
        self.EMAIL_INPUT = (By.ID, "email")
        self.EMAIL_HELPER_TEXT = (By.ID, "email-helper-text")
        self.PASSWORD_LABEL = (By.ID, "password-label")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.PASSWORD_HELPER_TEXT = (By.ID, "password-helper-text")
        self.SIGNIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
        self.FORGOT_PASSWORD = (By.CSS_SELECTOR, "a[href='/forgot-password']")
        self.SIGNUP_SUBTEXT = (By.CSS_SELECTOR, "a[href*='password'] + p")
        self.SIGNUP = (By.CSS_SELECTOR, "a[href='/signup']")
        self.ERROR_MESSAGE = (
            By.CSS_SELECTOR, "[data-test-id='login-server-error'] > .MuiAlert-message")
        self.ERROR_ICON = (
            By.CSS_SELECTOR, "[data-test-id='login-server-error'] > .MuiAlert-icon > svg")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def login(self, username: str, password: str):
        """
        Attempt to login to the web application via the login form

        Params
        ------
        username: str - The user email address
        password: str - The user password
        """
        email_input = self.get_element(self.EMAIL_INPUT)
        password_input = self.get_element(self.PASSWORD_INPUT)
        signin_button = self.get_element(self.SIGNIN_BUTTON)

        # Clear the input fields using CTRL+A and backspace before input
        self.clear_input(email_input)
        email_input.send_keys(username)
        self.clear_input(password_input)
        password_input.send_keys(password)
        signin_button.click()

        self.logger.info(f"{__class__}: Logged into application")

    def check_email_error(self, message: str):
        """
        Verify that there is an error while attempting to enter value in 
        the email address input field

        Params
        ------
        message: str - any expected error message(s) triggered while entering
        the email address
        """
        error_message = self.get_element(self.EMAIL_HELPER_TEXT)
        WebDriverWait(self.browser, 20).until(EC.visibility_of(error_message))
        self.tester.assertEqual(error_message.text, message)

    def check_password_error(self, message: str):
        """
        Verify that there is an error while attempting to enter value in 
        the password input field

        Params
        ------
        message: str - any expected error message(s) triggered while entering
        the password
        """
        error_message = self.get_element(self.PASSWORD_HELPER_TEXT)
        WebDriverWait(self.browser, 20).until(EC.visibility_of(error_message))
        self.tester.assertEqual(error_message.text, message)

    def check_form_error(self, message: str):
        """
        Verify that there is an error while attempting to submit user credentials
        via the login form

        Params
        ------
        message: str - any expected error message(s) triggered after submitting
        login credentials
        """
        error_message = self.get_element(self.ERROR_MESSAGE)
        WebDriverWait(self.browser, 20).until(EC.visibility_of(error_message))
        self.tester.assertEqual(error_message.text, message)

    def clear_input(self, input_field: WebElement):
        """
        Clears the input field's contents

        Params
        ------
        input_field: WebElement - the input field to clear
        """
        self.tester.assertEqual(input_field.tag_name, "input")
        input_field.send_keys(Keys.CONTROL, "a")
        input_field.send_keys(Keys.BACKSPACE)

    def validate_page(self):
        self.await_page_load(f"{os.getenv('BASE_URL')}/login")
        self.tester.assertEqual(self.browser.title, "Login - Risevest")

        aside_logo = self.get_element(self.LOGO)
        self.tester.assertIsNotNone(aside_logo, "Logo not detected.")

        aside_text = self.get_element(self.CATCHPRASE)
        self.tester.assertEqual(
            aside_text.text, "Dollar investments that help you grow", "Catchphrase is not matched.")

        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(heading.text, "Welcome back",
                                "Page heading is not matched.")

        sub_heading = self.get_element(self.SUB_HEADING)
        self.tester.assertIn("Let's get you logged in",
                             sub_heading.text, "Sub-heading text is not matched.")

        email_label = self.get_element(self.EMAIL_LABEL)
        self.tester.assertEqual(
            email_label.text, "Email address", "Email label is not matched.")

        email_input = self.get_element(self.EMAIL_INPUT)
        self.tester.assertEqual(email_input.get_attribute(
            "type"), "email", "Email input is not matched.")

        password_label = self.get_element(self.PASSWORD_LABEL)
        self.tester.assertEqual(password_label.text,
                                "Password", "Password label is not matched.")

        password_input = self.get_element(self.PASSWORD_INPUT)
        self.tester.assertEqual(
            password_input.get_attribute("type"), "password", "Passord input is not matched.")

        signin_button = self.get_element(self.SIGNIN_BUTTON)
        self.tester.assertEqual(
            signin_button.text, "Sign In", "Sign in button is not matched.")

        forgot_password_link = self.get_element(self.FORGOT_PASSWORD)
        self.tester.assertEqual(
            forgot_password_link.text, "I forgot my password", "Forgot password link text is not matched.")

        signup_subtext = self.get_element(self.SIGNUP_SUBTEXT)
        self.tester.assertIn("Don't have an account?",
                             signup_subtext.text, "Sign up text is not matched.")

        signup_link = self.get_element(self.SIGNUP)
        self.tester.assertEqual(
            signup_link.text, "Sign up", "Sign up link is not matched.")

        self.get_element(self.ERROR_ICON)
        self.get_element(self.ERROR_MESSAGE)

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
