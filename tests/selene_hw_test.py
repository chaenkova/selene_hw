from model.application import app
from model.data import users


def test_registers_user():
    app.panel.open_simple_registration_form()
    app.simple_registration.register(users.student)

