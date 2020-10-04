from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
try:
    browser.get(url)
    x_value = browser.find_element_by_id('input_value').text
    y = calc(x_value)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button[type=submit]').click()

finally:
    time.sleep(10)
    browser.quit()
