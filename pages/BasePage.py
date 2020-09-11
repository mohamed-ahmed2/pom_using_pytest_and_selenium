from selenium.webdriver import chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def click_element(self,locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click()

    def input_text(self,locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self,locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).text
        return element

    def is_visible(self,locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return bool(element)
    def switch_to_tab(self,index):
        tab = self.driver.switch_to.window(self.driver.window_handles[index])
        return tab
    def get_title(self):
        title = self.driver.title
        return title