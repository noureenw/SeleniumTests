from selenium import webdriver

import time

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/keypress")

name = driver.find_element_by_id("name")
name.click()
name.send_keys("Jack Doe")

time.sleep(10)

button = driver.find_element_by_id("button")
button.click()

driver.quit()





