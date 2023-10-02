import os
from selene import browser, have, command


def test_Positive_Student_Registration_Form():
    browser.open("/automation-practice-form")
    browser.element("#firstName").type("Anton")
    browser.element("#lastName").type("Bagrov")
    browser.element("#userEmail").type("021023test@gmail.com")
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type("8945691453")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element('option[value="5"]').click()
    browser.element(".react-datepicker__year-select").click().element('[value="1980"]').click()
    browser.element(".react-datepicker__day--028").click()
    browser.element("#subjectsInput").type("Com")
    browser.all(".subjects-auto-complete__menu-list").first.click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath('tests/bug-ficha.jpg'))
    browser.element("#currentAddress").type("some text")
    browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
    browser.element("#state").click()
    browser.all(". css-1uccc91-singleValue").element_by(have.text("Haryana")).click()
    browser.element("#city").click()
    browser.all(". css-1uccc91-singleValue").element_by(have.text("Panipat")).click()
    browser.element("#submit").click()
    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
        'Anton Bagrov',
        '021023test@gmail.com',
        'Male',
        '8945691453',
        '28 June,1980',
        'Computer Science',
        'Music',
        'bug-ficha.jpg',
        'some text',
        'Haryana Panipat'
    ))
