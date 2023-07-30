from behave import *
from behave import step
from pages.login_page import Login_page

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I am on the login page")
def step_impl(context):
    context.login_page = Login_page()
    context.login_page.open_login_page()

@when('I enter an invalid username "{username}" and the password "{password}"')
def step_impl(context, username, password):
    context.login_page.insert_username(username)
    context.login_page.insert_password(password)

@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_btn()

@then('I should be logged in')
def step_impl(context):
    context.login_page.check_successful_login()

@then('I should receive the error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_login_error_message(error_message)
