import logging

from selenium import webdriver
from tests.config import BehaveConfig


def before_all(context):
    selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    selenium_logger.setLevel(logging.WARN)

    browser = webdriver.Firefox()
    browser.set_page_load_timeout(BehaveConfig.SELENIUM_PAGE_LOAD_TIMEOUT)
    context.browser = browser


def after_all(context):
    context.browser.quit()