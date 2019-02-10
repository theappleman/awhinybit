#!/usr/bin/env python

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

try:
    driver.get("http://localhost:1234")
    driver.get_screenshot_as_file('0.png')
    assert driver.find_element_by_id("main").text == "Yes!"

    driver.get("http://localhost:1234?daniel")
    driver.get_screenshot_as_file('1.png')
    assert driver.find_element_by_id("main").text == "No"
finally:
    driver.quit()
