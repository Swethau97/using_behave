from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from features.POM.LoginPage import LoginPage
from features.POM.SearchPage import Search


@given(u'the login endpoint1')
def step_impl(context):
    time.sleep(2)
    context.search_functionality=LoginPage(context.driver)
    context.SearchPage=Search(context.driver)

@when(u'the valid products is entered')
def step_impl(context):
    context.search_functionality.search_button("HP")
    #context.driver.find_element(By.XPATH, "//div[@id='search']/input").send_keys("HP")
    time.sleep(3)


@when(u'clicked on Search button')
def step_impl(context):
    context.search_functionality.search_button_isDisplayed()
   # Wait=WebDriverWait(context.driver,25).until(EC.presence_of_element_located((By.XPATH, "//div[@id='search']//button")))
    #Wait.click()
    time.sleep(9)


@then(u'the system should display the products matching the keyword')
def step_impl(context):
    assert context.SearchPage.display_product()
    #assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    time.sleep(9)



@when(u'the in-valid product is entered')
def step_impl(context):
    context.search_functionality.search_button("Patience")
  #  context.driver.find_element(By.XPATH, "//div[@id='search']/input").send_keys("Patience")
    time.sleep(9)

@then(u'the system should display the appropriate message')
def step_impl(context):
    context.search_functionality.expected_message_no_product_function()
   #expected_message="There is no product that matches the search criteria."
   #assert context.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_message)

@when(u'search button is left as blank')
def step_impl(context):
    context.search_functionality.search_button("")
    #context.driver.find_element(By.XPATH, "//div[@id='search']/input").send_keys("")
    time.sleep(5)


@then(u'the system should display the appropriate message for blank search')
def step_impl(context):
    context.search_functionality.blank_search_warning()
    #expected_message = "There is no product that matches the search criteria."
    #assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(
    #    expected_message)
   # time.sleep(5)
















