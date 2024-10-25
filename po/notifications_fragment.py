from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from po.base_page import BasePage


class NotificationsModal(BasePage):
    """ The notifications modal after logging in successfully """

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
        self.NO_BUTTON = (
            By.CSS_SELECTOR, "div[data-testid='sentinelStart'] + div button:nth-child(1)")
        self.YES_BUTTON = (
            By.CSS_SELECTOR, "div[data-testid='sentinelStart'] + div button:nth-child(2)")

        self.logger.info(f"{__class__}: In {__class__.__qualname__}")

    def cancel_modal(self):
        """
        Close the notifications modal
        """
        cancel_button = self.get_element(self.NO_BUTTON)
        cancel_button.click()

        self.logger.info(f"{__class__}: Clicked the No, maybe later button")

    def confirm_modal_changed(self):
        """
        Confirm the modal is closed
        """
        heading = self.get_element(self.HEADING)
        self.tester.assertNotEqual("Allow notifications", heading.text)

        WebDriverWait(self.browser, 20).until(
            EC.invisibility_of_element(self.YES_BUTTON))

        self.logger.info(
            f"{__class__}: Check that the modal elements have changed")

    def validate_page(self):
        self.get_element(self.NOTIFICATION_MODAL)
        heading = self.get_element(self.HEADING)
        self.tester.assertEqual(
            heading.text, "Allow notifications", "Heading not detected.")

        icon = self.get_element(self.ICON)
        self.tester.assertIsNotNone(icon, "No icon detected.")

        notifications_text = self.get_element(self.MESSAGE)
        self.tester.assertIn(
            "Get notified about Rise updates", notifications_text.text, "Notification text is not matched.")

        cancel_button = self.get_element(self.NO_BUTTON)
        self.tester.assertEqual(
            cancel_button.text, "No, maybe later", "No button text is not matched.")

        ok_button = self.get_element(self.YES_BUTTON)
        self.tester.assertEqual(
            ok_button.text, "Yes, allow notifications", "Yes button text is not matched.")

        self.logger.info(
            f"{__class__}: Validated the presence of web elements")
