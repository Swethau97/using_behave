from behave import *
from selenium.webdriver.common.by import By
import datetime
import time
from features.POM.LoginPage import LoginPage
from features.POM.Loginpage1 import loginpage1

@given(u'the login endpoints')  #---all this happens in HOMEPAGE
def step_impl(context):
    time.sleep(5)
    context.loginInstance = LoginPage(context.driver)
    context.loginInstance.click_on_account_dropdown()
    context.loginInstance.login_page()
    context.Loginpage_components_instance = loginpage1(context.driver)

@when('the valid emailid as "{email}" and password as "{password}" in to the fields')
def step_impl(context, email, password):
    context.Loginpage_components_instance.mailid(email)
    context.Loginpage_components_instance.mailpassword(password)

@when(u'clicked on login button')
def step_impl(context):
    time.sleep(8)
    context.Loginpage_components_instance.submit_click()

@when(u'the in-valid email and valid password is entered in to the fields')
def step_impl(context):
    timestamp = datetime.datetime.now()
    string_format = timestamp.strftime("%Y_%m_%d_%H_%M_%S")
    invalidemail = "swetha" + string_format + "@gmail.com"
    context.Loginpage_components_instance.mailid(invalidemail)
    context.Loginpage_components_instance.mailpassword("Swetha5@")

@when(u'valid email id and invalid password is entered in to the field')
def step_impl(context):
    context.Loginpage_components_instance.mailid("swetha5.viji@gmail.com")
    context.Loginpage_components_instance.mailpassword("swe@")

@when(u'invalid mail id and password is entered in to the fields')
def step_impl(context):
    timestamp = datetime.datetime.now()
    str_format = timestamp.strftime("%Y_%m_%d_%H_%M_%S")
    invalidemail = "swetha" + str_format + "@gmail.com"
    context.Loginpage_components_instance.mailid(invalidemail)
    context.Loginpage_components_instance.mailpassword("Swetha5@")

@then(u'the system should log the user')
def step_impl(context):
    context.Loginpage_components_instance.logged_in()

@then(u'the proper warning message should be shown')
def step_impl(context):
    context.Loginpage_components_instance.warning()
