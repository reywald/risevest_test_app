from selenium.webdriver.remote.webdriver import WebDriver
from unittest import TestCase

from po.login_page import LoginPage
from po.home_page import HomePage
from po.notifications_modal import NotificationsModal
from po.confirm_notifications_modal import ConfirmNotificationsModal


def app_login(credentials: dict, browser: WebDriver, tester: TestCase):
    """
    Login to the Risevest app, check the web elements and close the 
    notifications modal

    Parameters
    ----------
    credentials: {str, str}
      The username and password
    browser: WebDriver
      The browser driver
    tester: TestCase
      unittest's test library api
    """
    login_page = LoginPage(browser, tester)
    login_page.validate_page()
    login_page.login(
        username=credentials["username"],
        password=credentials["password"]
    )

    home_page = HomePage(browser, tester)
    home_page.validate_page()

    notifications_modal = NotificationsModal(browser, tester)
    notifications_modal.validate_page()
    notifications_modal.cancel_modal()
    notifications_modal.confirm_modal_changed()

    confirm_modal = ConfirmNotificationsModal(browser, tester)
    confirm_modal.validate_page()
    confirm_modal.close_modal()
    confirm_modal.confirm_modal_closed()
