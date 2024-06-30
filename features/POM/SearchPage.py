from selenium.webdriver.common.by import By


class Search:
    valid_product="HP LP3065"
    def __init__(self,driver):
        self.driver=driver
    def display_product(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_product).is_displayed()
