import os

from selene import browser, have, by, command


def test_practice_form():
    browser.open("/automation-practice-form")
    browser.element('.main-header').should(have.text("Practice Form"))
    browser.element('#fixedban').execute_script('element.remove()')
    browser.element('footer').execute_script('element.remove()')
    # browser.element('#fixedban').perform(command.js.scroll_into_view)

    browser.element("#firstName").type('Anton')
    browser.element("#lastName").type('Bagrov')
    browser.element("#userEmail").type('031023_AntonQA@gmail.com')
    browser.element('#gender-radio-1').double_click()
    browser.element("#userNumber").type('8909898767')
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element(by.text("June")).click()
    browser.element(".react-datepicker__year-select").click().element(by.text("1980")).click()
    browser.element(".react-datepicker__day--028:not(.react-datepicker__day--outside-month)").click()
    browser.element('#currentAddress').perform(command.js.scroll_into_view)
    browser.element("#subjectsInput").type('Com')
    browser.element(".subjects-auto-complete__menu").element(by.text("Commerce")).click()
    browser.element("#hobbiesWrapper").element(by.text("Reading")).click()
    browser.element("#hobbiesWrapper").element(by.text("Music")).click()
    browser.element(by.css("input[type=file]")).send_keys(os.path.abspath('pic/bug-ficha.jpg'))
    browser.element('#currentAddress').type('Slovenia,1000 Ljubljana,Cesta na Loko 19')
    browser.element("#state").click().element(by.text("Haryana")).click()
    browser.element("#city").click().element(by.text("Karnal")).click()
    browser.element("#submit").click()

    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))

    browser.element('.table-responsive').all('td:nth-of-type(2)').should(
        have.texts(
            'Anton Bagrov',
            '031023_AntonQA@gmail.com',
            'Male',
            '8909898767',
            '28 June,1980',
            'Commerce',
            'Reading, Music',
            'bug-ficha.jpg',
            'Slovenia,1000 Ljubljana,Cesta na Loko 19',
            'Haryana Karnal',
        )
    )

    browser.element("#closeLargeModal").click()