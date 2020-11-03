from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
driver.get("https://formy-project.herokuapp.com/autocomplete")

auto = driver.find_element_by_id("autocomplete")
auto.click()
auto.send_keys("913 Cole Pl, Santa Clara, CA 95054")

# Implicit wait
# driver.implicitly_wait(3)

#Explicit wait
wait = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "pac-item")))

# result = driver.find_element_by_class_name("pac-item")


wait.click()

time.sleep(1)

driver.quit()

