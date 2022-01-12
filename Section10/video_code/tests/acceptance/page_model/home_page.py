from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):

    @property
    def url(self):
        return super(HomePage, self).url + '/'

        # In python3 kunnen we zo een superklasse oproepen



    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)