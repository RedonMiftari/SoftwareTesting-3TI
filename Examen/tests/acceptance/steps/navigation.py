from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


use_step_matcher('re')

@given('Ik ben op de homepage')
def step_impl(context):

    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.get('http://127.0.0.1:5000')


@then('Ben ik op de blog page')
def step_impl(context):

    expected_url = 'http://127.0.0.1:5000/blog'

    assert context.browser.current_url == expected_url