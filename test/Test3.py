import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/scroll")

name = driver.find_element_by_id("name")

actions = ActionChains(driver)
actions.move_to_element(name)
name.send_keys("Jane Doe")


date = driver.find_element_by_id("date")
date.send_keys("11/1/2020")

time.sleep(1)
driver.quit()





