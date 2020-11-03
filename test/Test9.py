from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/datepicker")

date = driver.find_element_by_id("datepicker")
date.send_keys("01/01/2022")
date.send_keys(Keys.RETURN)
time.sleep(1)


driver.quit()