from browser import Browser
from pages.login_page import Login_page
from pages.create_employee_page import CreateEmployeePage


def before_all(context):
    context.browser = Browser()
    context.login_page = Login_page()
    context.create_employee_page = CreateEmployeePage()


def after_all(context):
    context.browser.close()