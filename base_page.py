from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage(Browser):
    #Login
    def check_error_message(self, locator, expected_result, message_fail):
        actual_result = self.chrome.find_element(*locator).text
        assert actual_result == expected_result, message_fail

    def check_page_url(self, partial_url):
        actual_url = self.chrome.current_url
        assert partial_url in actual_url, "ERROR: Page url is not correct. Please check your data"

    def check_link(self, url, error_message=""):
        current_url = self.chrome.current_url
        assert current_url == url, error_message


    #Create_Employee
    #
    # def wait_for_element_to_be_clickable(self, locator):
    #     WebDriverWait(self.chrome,10).until(EC.element_to_be_clickable(locator))
    #
    # def wait_for_element_to_be_visible(self, locator):
    #     WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(locator))
    #
    # def wait_for_text_to_be_present_in_element(self, locator, text):
    #     WebDriverWait(self.chrome, 10).until(EC.text_to_be_present_in_element(locator, text))
