from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    page = BlogPage(context.driver)
    context.driver.get(page.url)

# dankzij context kunnen we van given de browser variabele overnemen naar then

@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url #dit is een test om te zien of we krijgen wat we verwachten




@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url  # dit is een test om te zien of we krijgen wat we verwachten


@given('I am a new post page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    page = NewPostPage(context.driver)
    context.driver.get(page.url)


