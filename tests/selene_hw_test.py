from data.user import User
from pages.registration_page import RegistrationPage


def test_user_can_send_form():
    page = RegistrationPage()
    user = User('Masha',
                'Maria',
                'mama@mail.ru',
                'Female',
                '7987654543',
                '2022', 'July', '12',
                'Hindi',
                'Sports',
                'picture.jpg',
                'Address',
                'NCR',
                'Delhi'
                )
    page.open().register(user).should_registered_user_with(user)
