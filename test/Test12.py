from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome("/Users/noureen/PycharmProjects/FirstSeleniumTest/drivers/chromedriver")
    driver.get("https://formy-project.herokuapp.com/form")

    submitForm(driver)
    waitForAlert(driver)

    # Assertions
    assert "The form was successfully submitted!" in driver.page_source

    # https://formy-project.herokuapp.com/thanks
    driver.quit()

def waitForAlert(driver):
    # Add explicit wait
    wait = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))


def submitForm(driver):
    driver.find_element_by_id("first-name").send_keys("Jane")
    driver.find_element_by_id("last-name").send_keys("Does")
    driver.find_element_by_id("job-title").send_keys("Engineer")
    driver.find_element_by_id("radio-button-3").click()
    driver.find_element_by_id("checkbox-2").click()
    driver.find_element_by_id("select-menu").find_element_by_xpath("//*[@id='select-menu']/option[4]").click()
    time.sleep(1)
    driver.find_element_by_id("select-menu").find_element_by_css_selector("option[value ='1']").click()

    driver.find_element_by_id("datepicker").send_keys("12/12/2020")
    driver.find_element_by_id("datepicker").send_keys(Keys.RETURN)

    driver.find_element_by_class_name("btn.btn-lg.btn-primary").click()


if __name__ == "__main__":
    main()
