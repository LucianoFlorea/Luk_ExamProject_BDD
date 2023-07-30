import base_page
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page(base_page.BasePage):
    # username = "luk2unlimit@yahoo.com"
    # password = "12345678Aa"
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    ERROR_MSG = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def open_login_page(self):
        self.chrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def insert_username(self, username):
        self.chrome.find_element(*self.USERNAME).send_keys(username)

    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)
    def click_login_btn(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()

    def check_successful_login(self):
        self.check_link("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", "error: I was not logged in")

    def check_login_error_message(self, expected_result):
        error_message = "error: the failed login message is not displayed"
        self.check_error_message(self.ERROR_MSG, expected_result, error_message)

