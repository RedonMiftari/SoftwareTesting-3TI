from behave import *


use_step_matcher('re')

@when('I click on the link with id "(.*)"') # Wat binnen "(.*)" komt is link_id, de "(.*)" is een groep.
def step_impl(context, link_id):
    link = context.browser.find_element_by_id(link_id)
    link.click()