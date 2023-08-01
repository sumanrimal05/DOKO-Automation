import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def browser():
    # Initialize Chrome service
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    chrome_service = Service(ChromeDriverManager(
        driver_version="114.0.5735.90").install())
    chrome_options = Options()

    # # Set default user profile path
    # chrome_options.add_argument(
    #     "user-data-dir=C:\\Users\\rimal\\AppData\\Local\\Google\\Chrome\\User Data\\")

    # Add user agent
    chrome_options.add_argument(f'user-agent={user_agent}')

    chrome_options.add_experimental_option("detach", True)

    # Create a Chrome WebDriver instance
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    print("Browser is", browser)
    return browser
