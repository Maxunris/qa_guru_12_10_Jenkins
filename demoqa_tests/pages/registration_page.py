from selene import browser, have, be
from demoqa_tests import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').should(be.visible).type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').should(be.visible).type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').should(be.visible).type(email)

    def fill_gender(self, gender):
        browser.all('[for^=gender-radio]').element_by(
            have.exact_text(gender)).click()

    def fill_phone(self, phone):
        browser.element('#userNumber').should(be.visible).type(phone)

    def fill_date_of_birth(self, day, month, year):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").send_keys(year)
        browser.element(".react-datepicker__month-select").send_keys(month)
        browser.element(f".react-datepicker__day--0{day}").click()

    def fill_subjects(self, subjects):
        browser.element('#subjectsInput').type(subjects).press_enter()

    def fill_hobbies(self, hobbies):
        browser.all('[for^=hobbies-checkbox]').element_by(
            have.exact_text(hobbies)).click()

    def attach_photo(self, photo):
        browser.element("#uploadPicture").send_keys(
            resource.path_photo(photo))

    def fill_current_address(self, current_address):
        browser.element('#currentAddress').should(
            be.visible).type(current_address)

    def fill_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def fill_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def sumbit(self):
        browser.element('#submit').should(be.clickable).press_enter()

    def should_registration_form(self, first_name, last_name, email, gender,
                                 phone, date_of_birth, subjects, hobbies,
                                 photo, current_address, state, city):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.texts(f'{first_name} {last_name}', {email}, {gender}, {phone},
                       {date_of_birth}, {subjects}, {hobbies}, {photo},
                       {current_address}, f'{state} {city}'))