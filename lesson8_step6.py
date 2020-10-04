from selenium.webdriver import Chrome
import time
import math

url = 'http://suninjuly.github.io/execute_script.html'
browser = Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def scroll(element):
    browser.execute_script('return arguments[0].scrollIntoView(true);', element)


try:
    browser.get(url)
    input_value = browser.find_element_by_id('input_value').text
    y = calc(input_value)
    input_text = browser.find_element_by_id('answer')
    scroll(input_text)
    input_text.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    scroll(checkbox)
    checkbox.click()
    radio = browser.find_element_by_id('robotsRule')
    scroll(radio)
    radio.click()
    button = browser.find_element_by_css_selector('form button[type=submit]')
    scroll(button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
