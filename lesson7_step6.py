from selenium.webdriver import Chrome
import time

url = 'http://suninjuly.github.io/math.html'
browser = Chrome()

try:
    browser.get(url)
    people_radio = browser.find_element_by_id('peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print('value of people radio: ', people_checked)
    assert people_checked is not None, 'People radio is not selected by default'
    assert people_checked == 'true', 'People radio is not selected by default'
    robots_radio = browser.find_element_by_id('robotsRule')
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None, 'Robots radio is selected'
finally:
    time.sleep(10)
    browser.quit()
