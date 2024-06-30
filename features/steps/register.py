from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
from features.POM.LoginPage import LoginPage
from features.POM.RegisterPage import Register


@given(u'the login endpoint-1')
def step_impl(context):
    time.sleep(10)
    context.Register_Page = Register(context.driver)
    context.HomePage = LoginPage(context.driver)


@when('i navigate to register page')
def step_impl(context):

    context.HomePage.click_on_account_dropdown()
    context.Register_Page.register_option_click()
   # context.driver.find_element(By.XPATH, "//li[@class='dropdown']//span[text()='My Account']").click()
    #context.driver.find_element(By.LINK_TEXT, "Register").click()
   # WebDriverWait(context.driver, 10).until(
      #  EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/h1[text()='Register Account']"))
  #  )
  #  assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1[text()='Register Account']").is_displayed()

@when('provide all the fields')
def step_impl(context):
    context.Register_Page.firstname("Georgia")
    context.Register_Page.lastname("Miller")
    current_time = datetime.datetime.now()
    string_format = current_time.strftime("%Y_%m_%d_%H_%M_%S") + "@example.com"
    context.Register_Page.e_mail(string_format)
    context.Register_Page.telephone_Number("8248441803")
    context.Register_Page.password_1("Swetha53@")
    context.Register_Page.cpassword("Swetha53@")
   # context.driver.find_element(By.ID,"input-firstname").send_keys("Georgia")
   # context.driver.find_element(By.ID,"input-lastname").send_keys("Miller")

    #context.driver.find_element(By.ID,"input-email").send_keys(string_format)
   # context.driver.find_element(By.ID,"input-telephone").send_keys("8248441803")
  #  context.driver.find_element(By.ID,"input-password").send_keys("Swetha53@")
  #  context.driver.find_element(By.ID,"input-confirm").send_keys("Swetha53@")

@when('click on agree button')
def step_impl(context):
    context.Register_Page.agree_button_click()
    #context.driver.find_element(By.XPATH, "(//div[@class='pull-right']//input)[1]").click()

@when('click on Continue button')
def step_impl(context):
    context.Register_Page.continue_button_click()
   # context.driver.find_element(By.XPATH, "(//div[@class='pull-right']//input)[2]").click()


@then('the proper existing mail id warning message should be displayed')
def step_impl(context):
    context.Register_Page.existing_mailId()
    #expected_message = "Warning: E-Mail Address is already registered!"
    #WebDriverWait(context.driver, 23).until(
     #   EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']"))
   # )
   # text1 = context.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
   # print(text1)
  #  assert expected_message in text1, f"Expected '{expected_message}' to be in '{text1}'"

@then('the proper warning message should be displayed')
def step_impl(context):
    context.Register_Page.warning_without_entering_the_details()
    '''WebDriverWait(context.driver, 23).until(
        EC.presence_of_element_located((By.LINK_TEXT, "login page"))
    )
    assert context.driver.find_element(By.LINK_TEXT, "login page").is_displayed()
'''
@then('the user should be registered')
def step_impl(context):
    context.Register_Page.account_creation()
''' expected_string = "Your Account Has Been Created!"
    WebDriverWait(context.driver, 24).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='content']/h1"))
    )
    actual_text = context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
    print(actual_text)
    assert expected_string in actual_text, f"Expected '{expected_string}' to be in '{actual_text}'" 
    '''


@when(u'provide all the fields except  mail id')
def step_impl(context):
    context.Register_Page.firstname("Georgia")
    context.Register_Page.lastname("Miller")
    context.Register_Page.telephone_Number("8248441803")
    context.Register_Page.password_1("Swetha53@")
    context.Register_Page.cpassword("Swetha53@")


    #context.driver.find_element(By.ID, "input-firstname").send_keys("Georgia")
   # context.driver.find_element(By.ID, "input-lastname").send_keys("Miller")
   # context.driver.find_element(By.ID, "input-telephone").send_keys("8248441803")
   # context.driver.find_element(By.ID, "input-password").send_keys("Swetha53@")
   # context.driver.find_element(By.ID, "input-confirm").send_keys("Swetha53@")


@then(u'the warning E-Mail Address does not appear to be valid!should appear')
def step_impl(context):
    context.Register_Page.invalid_email_address()
    '''expected_message = "E-Mail Address does not appear to be valid!"
    WebDriverWait(context.driver, 25).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='input-email']/following-sibling::div"))
    )
    text2 = context.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text
    print(text2)
    assert expected_message in text2, f"Expected '{expected_message}' to be in '{text2}'"'''


@when(u'provide all the fields with exisitng mail id')
def step_impl(context):
    context.Register_Page.firstname("Georgia")
    context.Register_Page.lastname("Miller")
    context.Register_Page.e_mail("swetha5.viji@gmail.com")
    context.Register_Page.telephone_Number("8248441803")
    context.Register_Page.password_1("Swetha53@")
    context.Register_Page.cpassword("Swetha53@")

    #context.driver.find_element(By.ID, "input-firstname").send_keys("Georgia")
   # context.driver.find_element(By.ID, "input-lastname").send_keys("Miller")
   # context.driver.find_element(By.ID, "input-email").send_keys("swetha5.viji@gmail.com")
   # context.driver.find_element(By.ID, "input-telephone").send_keys("8248441803")
   # context.driver.find_element(By.ID, "input-password").send_keys("Swetha53@")
   # context.driver.find_element(By.ID, "input-confirm").send_keys("Swetha53@")





