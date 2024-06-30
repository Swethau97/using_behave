from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import ConfigReader
def before_scenario(context,driver):
    context.driver_path = ChromeDriverManager().install()
    options = Options()
    service = Service(context.driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic config","url"))

def after_scenario(context,driver):
    context.driver.quit()