from behave import *


use_step_matcher('re')


@when('Ik op de "Go to blog" link met id "(.*)" klik')
def step_impl(context, link_id):


    link = context.browser.find_element_by_id(link_id)
    link.click()

