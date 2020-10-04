import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from helpers import calc


url = 'http://suninjuly.github.io/explicit_wait2.html'
browser = Chrome()

try:
    browser.get(url)
    price = WebDriverWait(browser, 15).until(
        ec.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element_by_id('book')
    button.click()
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_css_selector('button[type=submit]').click()

finally:
    time.sleep(10)
    browser.quit()
