from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys


def  test_github():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com')

    s("span[data-target='qbsearch-input.inputButtonText']").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").send_keys(Keys.ENTER)

    s(by.link_text('eroshenkoam/allure-example')).click()
    s("span[data-content='Issues']").click()
    s(by.partial_text("#76")).should(be.visible)

