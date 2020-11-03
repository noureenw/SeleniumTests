from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/fileupload")

fileUploadField = driver.find_element_by_id("file-upload-field")
fileUploadField.send_keys('cars.txt')

time.sleep(2)
driver.quit()