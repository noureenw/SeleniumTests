from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/radiobutton")

radioButton3 = driver.find_element_by_xpath("/html/body/div/div[3]/input")
radioButton3.click()
time.sleep(1)

radioButton1 = driver.find_element_by_id("radio-button-1")
radioButton1.click()

time.sleep(1)

radioButton2 = driver.find_element_by_css_selector("input[value='option2']")
radioButton2.click()
time.sleep(1)

driver.quit()


