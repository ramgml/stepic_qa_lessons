from selenium.webdriver import Chrome
import time
from helpers import calc

url = 'http://suninjuly.github.io/alert_accept.html'
browser = Chrome()

try:
    browser.get(url)
    browser.find_element_by_css_selector('form button[type=submit]').click()
    browser.switch_to.alert.accept()
    input_value = browser.find_element_by_id('input_value').text
    y = calc(input_value)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_css_selector('form [type=submit]').click()

finally:
    time.sleep(10)
    browser.quit()
