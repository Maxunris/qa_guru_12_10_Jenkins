from demoqa_tests.pages.registration_page import RegistrationPage


def test_user_registration_form():
    registration_pages = RegistrationPage()
    registration_pages.open()
    registration_pages.fill_first_name('Max')
    registration_pages.fill_last_name('Cheshire')
    registration_pages.fill_email('Maxcheshire1@gmail.com')
    registration_pages.fill_gender('Male')
    registration_pages.fill_phone('7999123121')
    registration_pages.fill_date_of_birth("26", "March", "1998")
    registration_pages.fill_subjects('Computer Science')
    registration_pages.fill_hobbies('Reading')
    registration_pages.attach_photo('123.jpeg')
    registration_pages.fill_current_address('Pushkina-kolotushkina, Moscow, Russia')
    registration_pages.fill_state('NCR')
    registration_pages.fill_city('Delhi')
    registration_pages.sumbit()
    registration_pages.should_registration_form(
        'Max',
        'Cheshire',
        'Maxcheshire1@gmail.com',
        'Male',
        '7999123121',
        '26 March,1998',
        'Computer Science',
        'Reading',
        '123.jpeg',
        'Pushkina-kolotushkina, Moscow, Russia',
        'NCR',
        'Delhi',
    )