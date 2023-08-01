from selenium.common.exceptions import NoAlertPresentException


def handle_alert(driver):
    try:
        alert = driver.switch_to.alert
        # Perform actions on the alert
        alert.accept()
    except NoAlertPresentException:
        # Handle the case when no alert is present
        print("No alert found.")
