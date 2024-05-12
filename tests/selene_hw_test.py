from selene import browser, command, have
import os


def test_user_can_send_form():
    browser.open("automation-practice-form")

    #ФИО
    browser.element("#firstName").type('Masha')
    browser.element("#lastName").type('Maria')

    #email

    browser.element("#userEmail").type('mama@mail.ru')

    #gender(можно и по id)

    browser.element('#genterWrapper').all('label[for^=gender-radio]').element_by(have.text('Female')).click()

    #phone
    browser.element('#userNumber').type('7987654543')

    #date
    browser.element('#dateOfBirthInput').type(command.Keys.COMMAND + 'a' + command.Keys.NULL + '07 12 2022').press_enter()


    #subjects
    browser.element('#subjectsInput').type("h").press_tab()

    #hobbies
    browser.element('#hobbiesWrapper').all('[class*=checkbox]').element_by(have.text('Sports')).click()
    #picture

    browser.element('#uploadPicture').send_keys(os.path.abspath('./pictures/picture.jpg'))

    #address
    browser.element('#currentAddress').type('Address')

    #state and city

    browser.element('#state').click()
    browser.element('#state').all('[class$=option]').element_by(have.text('NCR')).click()

    browser.element('#city').click()
    browser.element('#city').all('[class$=option]').element_by(have.text('Delhi')).click()

    browser.element('#submit').click()

    browser.element('.modal-content').element('table').all('tr').all('td').even.should(
        have.exact_texts(
            'Masha Maria',
            'mama@mail.ru',
            'Female',
            '7987654543',
            '12 July,2022',
            'Hindi',
            'Sports',
            'picture.jpg',
            'Address',
            'NCR Delhi',
        )
    )
