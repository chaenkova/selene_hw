from tests.application import app
from tests.data import users


def test_registers_user():
    app.open()
    app.panel.open_simple_registration_form()
    app.simple_registration.register(users.student)

