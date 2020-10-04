import math
import time
from selenium import webdriver

href = 'http://suninjuly.github.io/find_link_text'
browser = webdriver.Chrome()
link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    browser.get(href)
    link = browser.find_element_by_link_text(link_text)
    link.click()

    value1 = 'input'
    value2 = 'last_name'
    value3 = 'city'
    value4 = 'country'

    input1 = browser.find_element_by_tag_name(value1).send_keys('Ivan')
    input2 = browser.find_element_by_name(value2).send_keys('Petrov')
    input3 = browser.find_element_by_class_name(value3).send_keys('Smolensk')
    input4 = browser.find_element_by_id(value4).send_keys('Russia')
    button = browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(5)
    browser.quit()
