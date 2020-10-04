from selenium.webdriver import Chrome
import time
import math

url = 'http://suninjuly.github.io/get_attribute.html'
browser = Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(url)
    image = browser.find_element_by_css_selector('form img')
    valuex = image.get_attribute('valuex')
    y = calc(valuex)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('form button[type=submit]').click()
finally:
    time.sleep(10)
    browser.quit()
