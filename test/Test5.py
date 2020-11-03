from selenium import webdriver

import time

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/switch-window")

alertButton = driver.find_element_by_id("alert-button")
alertButton.click()

time.sleep(1)
alert = driver.switch_to.alert
time.sleep(1)
alert.accept()



driver.quit()