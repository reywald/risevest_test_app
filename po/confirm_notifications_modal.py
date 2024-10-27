from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from po.base_page import BasePage


class ConfirmNotificationsModal(BasePage):
    """ The confirm notifications modal after logging in successfully and 
    canceling notifications 
    """

    def __init__(self, browser, tester: TestCase):
        super().__init__(browser, tester)

        self.NOTIFICATION_MODAL = (
            By.CSS_SELECTOR, "div[data-testid='sentinelStart'] + div")
        self.HEADING = (By.CSS_SELECTOR,
                        "div[data-testid='sentinelStart'] + div h2")
        self.ICON = (By.CSS_SELECTOR,
                     "div[data-testid='sentinelStart'] + div svg")
        self.MESSAGE = (By.CSS_SELECTOR,
                        "div[data-testid='sentinelStart'] + div p")
        self.OK_BUTTON = (
            By.CSS_SELECTOR, "div[data-testid='sentinelStart'] + div button")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def close_modal(self):
        """
        Close the notifications modal
        """
        ok_button = self.get_element(self.OK_BUTTON)
        ok_button.click()

        self.logger.info(f"{__class__}: Close the notifications modal")

    def confirm_modal_closed(self):
        """
        Confirm the modal is closed
        """
        WebDriverWait(self.browser, 20).until(
            EC.invisibility_of_element(self.HEADING))

        self.logger.info(
            f"{__class__}: Check that the notifications modal is closed")

    def validate_page(self):
        self.get_element(self.NOTIFICATION_MODAL)
        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(
            heading.text, "To turn on later", "Heading not detected.")

        icon = self.get_element(self.ICON)
        self.tester.assertIsNotNone(icon, "No icon detected.")

        notifications_text = self.get_element(self.MESSAGE)
        self.tester.assertIn(
            "To start getting notifications", notifications_text.text, "Notification text is not matched.")

        ok_button = self.get_element(self.OK_BUTTON)
        self.tester.assertEqual(
            ok_button.text, "Okay, got it!", "Ok button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
