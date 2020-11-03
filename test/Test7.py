from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/dragdrop")

image = driver.find_element_by_id("image")

box = driver.find_element_by_id("box")

actions = ActionChains(driver)
actions.drag_and_drop(image,box).perform()

time.sleep(2)

driver.quit()


