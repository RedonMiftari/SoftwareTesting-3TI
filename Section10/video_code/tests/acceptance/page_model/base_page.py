# Bevat alles wat identiek is voor elke pagina
from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property  # Voor elke methode die geen argumenten opneemt, kan deze als property geroepen worden.
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

