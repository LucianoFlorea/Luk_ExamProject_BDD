from behave import *
import base_page
from pages.login_page import Login_page
from pages.create_employee_page import CreateEmployeePage


@given("I am on the employee creation page")
def step_impl(context):
    context.login_page.signin()
    context.create_employee_page.open_create_employee_page()

@when("I fill out the form with the employee's information")
def step_impl(context):
    context.create_employee_page.fill_employee_form(
        employee_id="12345",
        first_name="John",
        last_name="Doe")

@when("I click on the Save button")
def step_impl(context):
    context.create_employee_page.click_save_button()

@then("the employee should be created and I should be taken to the employee's profile page")
def step_impl(context):
    context.create_employee_page.check_my_proffile_page()

@then("I should see an error message that says \"Employee Id already exists\"")
def step_impl(context):
    error_message = context.create_employee_page.get_error_message()
    assert error_message == "Employee Id already exists", f"Actual error message: {error_message}"
