from tests.config import BehaveConfig


def visit_url(browser, endpoint=""):
    url = "%s/%s" % (BehaveConfig.TEST_HOST, endpoint)
    browser.get(url)
