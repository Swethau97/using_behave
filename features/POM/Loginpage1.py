from selenium.webdriver.common.by import By


class loginpage1:
    mail_id_xpath = "input-email"
    mail_password_xpath = "input-password"
    submit_button="//input[@type='submit']"
    after_logging_in="Edit your account information"
    expected_message = "Warning: No match for E-Mail Address and/or Password."
    warning_message="(//div[@id='account-login']/div)[1]"
    def __init__(self,driver):
        self.driver=driver
    def mailid(self,mailid):
        self.driver.find_element(By.ID,self.mail_id_xpath).send_keys(mailid)
    def mailpassword(self,mailpassword):
        self.driver.find_element(By.ID,self.mail_password_xpath).send_keys(mailpassword)
    def submit_click(self):
        submit_button_xpath=self.driver.find_element(By.XPATH,self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button_xpath)
        submit_button_xpath.click()
    def logged_in(self):
        self.driver.find_element(By.LINK_TEXT,self.after_logging_in).is_displayed()
    def warning(self):
        actual=self.driver.find_element(By.XPATH,self.warning_message).text
        assert self.expected_message in actual,f"Expected '{self.expected_message}' to be in '{actual}'"


