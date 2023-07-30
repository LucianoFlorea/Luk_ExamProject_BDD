from selenium import webdriver

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class Browser:
    # def __init__(self):
    #     # Add the Chrome options
    #     chrome_options = Options()
    #     chrome_options.add_argument('--ignore-certificate-errors')
    #     chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    #
    #     # Set the capability to ignore SSL errors
    #     capabilities = webdriver.DesiredCapabilities().CHROME.copy()
    #     capabilities['acceptInsecureCerts'] = True
    #
    #     # Initialize the WebDriver with the options and capabilities
    #     self.chrome = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)
    #     self.chrome.maximize_window()
    #     self.chrome.implicitly_wait(5)
    #
    # def close(self):
    #     self.chrome.quit()
    service = Service("C:\Program Files\Google\chromedriver")
    chrome = webdriver.Chrome(service=service)

    chrome.maximize_window()
    chrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    chrome.implicitly_wait(5)
    sleep(3)

    def close(self):
        self.chrome.quit()

