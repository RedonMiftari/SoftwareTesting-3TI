from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')

@given('I wait for the posts to load')
def step_impl(context):

    # Wachten om een element te laten laden, anders kan de test fout gaan doordat de driver niet wacht.
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(BlogPageLocators.POST_SECTION)
    )