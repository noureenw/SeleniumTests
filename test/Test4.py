from selenium import webdriver

import time

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/switch-window")

tab_button = driver.find_element_by_id("new-tab-button")
tab_button.click()

originalHandle = driver.window_handles[0]

print(originalHandle)

newHandle = driver.window_handles[1]

print(newHandle)

# Switch to new window

driver.switch_to.window(newHandle)
time.sleep(2)

# switch to original window
driver.switch_to.window(originalHandle)
time.sleep(2)
driver.quit()
