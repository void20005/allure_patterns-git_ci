import allure


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(allure.severity_level.BLOCKER)
    allure.dynamic.feature("Task in the repository")
    allure.dynamic.story('Unauthorized user cannot make task in repository')
    allure.dynamic.link('https://github.com', name = 'Testing')

@allure.tag('Critical')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owher", 'Sasa')
@allure.feature("Tasks")
@allure.story('User can make a task in repository')
@allure.link('https://github.com', name = 'Testing')
def test_decorator_labels():
    pass