from behave import *
from pages.login_page import Login_page



@given("I am on the login page")
def step_impl(context):
    context.login_page.open_login_page()

@when('I enter my username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.insert_username(username)
    context.login_page.insert_password(password)

@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_btn()

@then('I should be logged in')
def step_impl(context):
    context.login_page.check_successful_login()

@when('I click on logout button')
def step_impl(context):
    context.login_page.logout()

@then('I should be logged out')
def step_impl(context):
    context.login_page.check_successful_logout()


@then('I should receive the error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_login_error_message(error_message)

