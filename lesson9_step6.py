from selenium.webdriver import Chrome
import time
from helpers import calc

url = 'http://suninjuly.github.io/redirect_accept.html'
browser = Chrome()

try:
    browser.get(url)
    browser.find_element_by_xpath('//button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_css_selector('button[type=submit]').click()

finally:
    time.sleep(10)
    browser.quit()
