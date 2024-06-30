from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    Account_dropdown_click = "//li[@class='dropdown']//span[text()='My Account']"
    Login_page_click="Login"
    search_button_xpath="//div[@id='search']/input"
    search_button_xpath1="//div[@id='search']//button"
    expected_message = "There is no product that matches the search criteria."
    warning_xpath= "//input[@id='button-search']/following-sibling::p"
    expected_message_no_product="There is no product that matches the search criteria."
    def __init__(self,driver):
        self.driver=driver

    def click_on_account_dropdown(self):
        self.driver.find_element(By.XPATH,self.Account_dropdown_click).click()

    def login_page(self):
        self.driver.find_element(By.LINK_TEXT,self.Login_page_click).click()

    def search_button(self,search_name):
        self.driver.find_element(By.XPATH,self.search_button_xpath).send_keys(search_name)

    def search_button_isDisplayed(self):
        wait=WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located((By.XPATH,self.search_button_xpath1)))
        wait.click()

    def blank_search_warning(self):
        actual= self.driver.find_element(By.XPATH,self.warning_xpath).text
        assert self.expected_message == actual

    def expected_message_no_product_function(self):
        actual=self.driver.find_element(By.XPATH,self.warning_xpath).text
        assert self.expected_message_no_product == actual

