def test_registration(browser):
    browser.get('http://selenium1py.pythonanywhere.com/ru/ ')
    registration = browser.find_element_by_id("login_link")
    registration.click()
    input1 = browser.find_element_by_name("registration-email")
    input1.send_keys("fhdiwhgui85@hgrei.ru")
    input2 = browser.find_element_by_name("registration-password1")
    input2.send_keys("48g3ui48g3ui48g3ui")
    input3 = browser.find_element_by_name("registration-password2")
    input3.send_keys("48g3ui48g3ui48g3ui")
    button = browser.find_element_by_name("registration_submit")
    button.click()
    label = browser.find_element_by_css_selector("div.alert")
    assert label.text == '×\nСпасибо за регистрацию!'
