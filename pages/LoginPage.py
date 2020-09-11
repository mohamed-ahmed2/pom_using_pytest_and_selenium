from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage


class LoginPage(BasePage):
    email_textbox = (By.ID,"usernameField")
    password_textbox = (By.ID,"passwordField")
    login_button = (By.XPATH,"//button[@class='waves-effect waves-light btn-large btn-block btn-bold blue-btn textTransform']")
    error_message = (By.XPATH,"//span[contains(text(),'Invalid details')]")
    jobs_in_loginpage = (By.XPATH,"//div[contains(text(),'Jobs')]")
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)


    def login(self,email,password):
        self.input_text(self.email_textbox,email)
        self.input_text(self.password_textbox, password)

    def click_on_login(self):
        self.click_element(self.login_button)

    def is_error_visible(self):
        self.is_visible(self.error_message)
    def is_login_button_visible(self):
        return self.is_visible(self.login_button)

    def get_error(self):

        return self.get_text(self.error_message)

    def click_on_jobs(self):
        self.click_element(self.jobs_in_loginpage)
