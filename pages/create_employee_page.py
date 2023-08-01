from selenium.webdriver.common.by import By
from browser import Browser
import base_page


class CreateEmployeePage(Browser):
    PIM = (By.XPATH, "//span[normalize-space()='PIM']")
    ADD = (By.XPATH, "//button[normalize-space()='Add']")
    EMPLOYEE_ID_INPUT = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")

    def open_create_employee_page(self):
        self.chrome.find_element(*self.PIM).click()
        self.chrome.find_element(*self.ADD).click()
    def fill_employee_form(self, employee_id, first_name, last_name):
        self.chrome.find_element(*self.EMPLOYEE_ID_INPUT).send_keys(employee_id)
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def check_my_profile_page(self):
        self.check_page_url("/viewPersonalDetails/empNumber")


    def click_save_button(self):
        self.chrome.find_element(*self.SAVE_BUTTON).click()

    def get_error_message(self):
        return self.chrome.find_element(*self.ERROR_MESSAGE).text

