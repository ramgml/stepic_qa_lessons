from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/simple_form_find_task.html')
    button = browser.find_element_by_id('submit_button')


if __name__ == '__main__':
    main()
