from selenium.webdriver import Chrome
import time
import os


url = 'http://suninjuly.github.io/file_input.html'
browser = Chrome()

try:
    browser.get(url)
    firstname = browser.find_element_by_css_selector('form input[name=firstname]').send_keys('Ivan')
    lastname = browser.find_element_by_css_selector('form input[name=lastname]').send_keys('Petrov')
    email = browser.find_element_by_css_selector('form input[name=email]').send_keys('test@example.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(current_dir, 'test.txt')
    uploader = browser.find_element_by_id('file')
    uploader.send_keys(file)
    browser.find_element_by_css_selector('form button[type=submit]').click()
finally:
    time.sleep(10)
    browser.quit()
