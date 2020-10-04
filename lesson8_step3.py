from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
import time

url = 'http://suninjuly.github.io/selects1.html'
browser = Chrome()

try:
    browser.get(url)
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    result = int(num1) + int(num2)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(result))
    browser.find_element_by_css_selector('form button[type=submit]').click()
finally:
    time.sleep(10)
    browser.quit()
