from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/modal")

modalButton = driver.find_element_by_id("modal-button")
modalButton.click()

closeButton = driver.find_element_by_id("close-button")
driver.execute_script("arguments[0].click()",closeButton)

time.sleep(1)

driver.quit()