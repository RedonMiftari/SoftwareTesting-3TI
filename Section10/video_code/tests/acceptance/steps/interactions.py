from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')

''' ANDERE MANIER VOOR CLICK NAVIGATIE TEST
@when('I click on the link with id "(.*)"') # Wat binnen "(.*)" komt is link_id, de "(.*)" is een groep.
def step_impl(context, link_id):
    link = context.browser.find_element_by_id(link_id)
    link.click()
'''

#IPV link-id doen we nu met link text
@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()



@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I press on submit button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()

