from selene.support.shared import browser

from tests.model.components.panel import Panel
from tests.model.pages.simple_registration_page import (
    SimpleRegistrationPage,
)


class Application:
    def __init__(self):
        self.simple_registration = SimpleRegistrationPage()
        self.panel = Panel()

    def open(self):
        browser.open('/elements')
        return self


app = Application()
