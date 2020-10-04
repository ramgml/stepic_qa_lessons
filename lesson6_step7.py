from selenium import webdriver
import time


browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/huge_form.html')
    elements = browser.find_elements_by_css_selector('input[type=text]')
    for el in elements:
        el.send_keys('Мой ответ')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
