import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def browser():
    # initialize edge service
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
    driver_path = r"./driver/msedgedriver.exe"
    edge_service = Service(driver_path)

    # Set Default Users profile path
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument(
        "user-data-dir=C:\\Users\\rimal\\AppData\\Local\\Microsoft\\Edge\\User Data\\")
    edge_options.add_argument(f'user-agent={user_agent}')

    # Try to attach to an existing browser session
    try:
        # Create a new Edge WebDriver instance and close it immediately to get the session ID
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        session_id = driver.session_id
        driver.quit()

        # Attach to the existing browser session
        browser = webdriver.Remote(
            command_executor='http://localhost:9515', )
        browser.session_id = session_id

        print("Browser is", browser)
        return browser

    except Exception as e:
        print("Unable to attach to the existing browser session. Starting a new browser...")
        print(e)

        # Start a new browser session if attaching fails
        browser = webdriver.Edge(service=edge_service, options=edge_options)
        print("Browser is", browser)
        return browser


# def browser():
#     # intialzie edge service
#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
#     # driver_path = r"./driver/msedgedriver.exe"
#     # edge_service = Service(driver_path)
#     edge_service = Service(EdgeChromiumDriverManager().install())
#     edge_options = Options()
#     # edge_options.use_chromium = True
#     # Set Default Users profile path
#     edge_options.add_argument(
#         "user-data-dir=C:\\Users\\rimal\\AppData\\Local\\Microsoft\\Edge\\User Data\\")
#     # edge_options.add_argument("--disable-popup-blocking")

#     edge_options.add_experimental_option("detach", True)
#     edge_options.add_argument(f'user-agent={user_agent}')
#     browser = webdriver.Edge(service=edge_service, options=edge_options)
#     print("Browser is", browser)
#     return browser
