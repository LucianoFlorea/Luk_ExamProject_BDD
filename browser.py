from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Browser:
    service = Service("C:\Program Files\Google\chromedriver")
    chrome = webdriver.Chrome(service=service)

    chrome.maximize_window()
    chrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    chrome.implicitly_wait(5)

    def close(self):
        self.chrome.quit()

