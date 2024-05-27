from selene import browser, have, command
import os
import tests


class RegistrationPage:
    def __init__(self):
        self.state = browser.element('#state')
        self.city = browser.element('#city')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def fill_gender(self, value):
        browser.element(f'[for="gender-radio-{value}"]').click()
        return self

    def fill_phone_number(self, phone):
        browser.element('#userNumber').type(phone)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_tab()
        return self

    def fill_hobbies(self, value):
        browser.element(f'[for="hobbies-checkbox-{value}"]').click()
        return self

    def upload_picture(self, path):
        browser.element('#uploadPicture').send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), 'pictures/',path)
            ))
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^="react-select-3-option-"]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city(self, name):
        self.city.perform(command.js.scroll_into_view)
        self.city.click()
        browser.all('[id^="react-select-4-option-"]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def should_registered_user_with(self, full_name, email, gender, phone, date, subject, hobby, photo, address, state):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date,
                subject,
                hobby,
                photo,
                address,
                state,
            )
        )
