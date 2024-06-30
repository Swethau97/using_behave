from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Register:
    register_link_text="Register"
    register_account_check="//div[@id='content']/h1[text()='Register Account']"
    first_name="input-firstname"
    last_name="input-lastname"
    email="input-email"
    telephone="input-telephone"
    password="input-password"
    confirm_password="input-confirm"
    agree_button= "(//div[@class='pull-right']//input)[1]"
    continue_button="(//div[@class='pull-right']//input)[2]"
    alert="//div[@class='alert alert-danger alert-dismissible']"
    expected_message = "Warning: E-Mail Address is already registered!"
    emil_adress_is_not_valid="//input[@id='input-email']/following-sibling::div"
    expected_message_valid_email= "E-Mail Address is already registered!"
    expected_string_account_creation = "Your Account Has Been Created!"
    login_page_hyperlink="login page"
    def __init__(self,driver):
        self.driver=driver

    def register_option_click(self):
        self.driver.find_element(By.LINK_TEXT,self.register_link_text).click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.register_account_check))
        )
    def firstname(self,name):
        self.driver.find_element(By.ID,self.first_name).send_keys(name)
    def lastname(self,lname):
        self.driver.find_element(By.ID, self.last_name).send_keys(lname)
    def e_mail(self,mailid):
        self.driver.find_element(By.ID, self.email).send_keys(mailid)
    def telephone_Number(self,P_number):
        self.driver.find_element(By.ID, self.telephone).send_keys(P_number)
    def password_1(self,pword):
        self.driver.find_element(By.ID, self.password).send_keys(pword)
    def cpassword(self,cword):
        self.driver.find_element(By.ID, self.confirm_password).send_keys(cword)
    def agree_button_click(self):
        self.driver.find_element(By.XPATH,self.agree_button).click()
    def continue_button_click(self):
        self.driver.find_element(By.XPATH, self.continue_button).click()
    def existing_mailId(self):
        WebDriverWait(self.driver, 23).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.alert))
        )
        actual = self.driver.find_element(By.XPATH, self.alert).text
        #print(text1)
        return self.expected_message in actual, f"Expected '{self.expected_message}' to be in '{actual}'"
    def invalid_email_address(self):

        WebDriverWait(self.driver, 25).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.emil_adress_is_not_valid))
        )
        text2 = self.driver.find_element(By.XPATH, self.emil_adress_is_not_valid).text
        print(text2)
        assert self.expected_message_valid_email in text2, f"Expected '{self.expected_message_valid_email}' to be in '{text2}'"
    def account_creation(self):

        WebDriverWait(self.driver, 24).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='content']/h1"))
        )
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
        print(actual_text)
        assert self.expected_string_account_creation in actual_text, f"Expected '{self.expected_string_account_creation}' to be in '{actual_text}'"

    def warning_without_entering_the_details(self):
        WebDriverWait(self.driver, 23).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, self.login_page_hyperlink))
        )
        assert self.driver.find_element(By.LINK_TEXT, self.login_page_hyperlink).is_displayed()
