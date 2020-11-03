from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/dropdown")

dropdownMenu = driver.find_element_by_id("dropdownMenuButton")
dropdownMenu.click()

selection = driver.find_element_by_link_text("Enabled and disabled elements")
selection.click()

time.sleep(1)

driver.quit()
