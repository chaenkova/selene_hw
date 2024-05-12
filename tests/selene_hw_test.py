from selene import browser, command, have
import os


def test_user_can_send_form():
    browser.open("/automation-practice-form")

    #ФИО
    browser.element("#firstName").type('Masha')
    browser.element("#lastName").type('Maria')

    #email

    browser.element("#userEmail").type('mama@mail.ru')

    #gender(можно и по id)

    browser.element('[for="gender-radio-2"]').click()

    #phone
    browser.element('#userNumber').type('7987654543')

    #date
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(".react-datepicker__month-select option[value='6']").click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="2022"]').click()
    browser.element('.react-datepicker__day--012').click()


    #subjects
    browser.element('#subjectsInput').type("h").press_tab()

    #hobbies
    browser.element('[for="hobbies-checkbox-1"]').click()
    #picture

    browser.element('#uploadPicture').send_keys(os.path.abspath('./pictures/picture.jpg'))

    #address
    browser.element('#currentAddress').type('Address')

    #state and city

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

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
