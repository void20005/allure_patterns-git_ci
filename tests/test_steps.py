from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys
import allure


def  test_dynamic_steps():
    with allure.step("Open the main page"):
        browser.config.window_width = 1920

        browser.config.window_height = 1080

        browser.open('https://github.com')

    with allure.step("Find repository"):
        s("span[data-target='qbsearch-input.inputButtonText']").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").send_keys(Keys.ENTER)
    with allure.step("Follow the link"):
        s(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step("Open the Issues Tab"):
        s("span[data-content='Issues']").click()
    with allure.step("Check whether issue #76 is available"):
        s(by.partial_text("#76")).should(be.visible)

def  test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    follow_the_link('eroshenkoam/allure-example')
    open_issues_tab()
    check_issue_with_number('766')


@allure.step("Open the main page")
def open_main_page():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com')

@allure.step("Find repository {repo}")
def search_for_repository(repo):
    s("span[data-target='qbsearch-input.inputButtonText']").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").send_keys(Keys.ENTER)

@allure.step("Follow the link {}")
def follow_the_link(repo):
    s(by.link_text(repo)).click()

@allure.step("Open the Issues Tab")
def open_issues_tab():
    s("span[data-content='Issues']").click()

@allure.step("Check whether issue #76 is available")
def check_issue_with_number(num):
    s(by.partial_text("#" + num)).should(be.visible)
