from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    first_name_input = browser.find_element_by_css_selector('.first_block input.first')
    first_name_input.send_keys('Ivan')
    last_name_input = browser.find_element_by_css_selector('.first_block input.second')
    last_name_input.send_keys('Petrov')
    email_input = browser.find_element_by_css_selector('.first_block input.third')
    email_input.send_keys('test@example.com')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(30)
    browser.quit()
