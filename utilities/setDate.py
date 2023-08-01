from selenium.webdriver.common.by import By


def set_date(driver, date, pickerXpath):
    datepicker_field = driver.find_element(By.XPATH, pickerXpath)
