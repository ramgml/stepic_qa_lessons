from selenium.webdriver import Chrome
import time

url = 'http://suninjuly.github.io/cats.html'
browser = Chrome()

try:
    browser.get(url)
    browser.find_element_by_id('button')
finally:
    time.sleep(10)
    browser.quit()
