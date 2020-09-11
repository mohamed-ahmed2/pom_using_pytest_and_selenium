from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage


class HomePage(BasePage):
    jobs_link = (By.XPATH,"//div[contains(text(),'Jobs')]")
    Recruiters_link=(By.XPATH,"// div[contains(text(), 'Recruiters')]")
    companies_link = (By.XPATH,"//div[contains(text(),'Companies')]")
    Tools_link = (By.XPATH,"//div[contains(text(),'Tools')]")
    Services_link = (By.XPATH,"//div[contains(text(),'Services')]")
    more_link = (By.XPATH,"//div[contains(text(),'More')]")
    login_link = (By.XPATH,"//div[@class='mTxt'][contains(text(),'Login')]")



    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)

    def is_jobs_visible(self):
        return  self.is_visible(self.jobs_link)

    def is_Recruiters_visible(self):
        return self.is_visible(self.Recruiters_link)

    def is_companies_visible(self):
        return  self.is_visible(self.companies_link)

    def is_tools_visible(self):
        return  self.is_visible(self.Tools_link)

    def is_services_visible(self):
        return self.is_visible(self.Services_link)

    def is_more_visible(self):
        return   self.is_visible(self.more_link)

    def is_login_button_visible(self):
        return self.is_visible(self.login_link)

    def click_on_jobs(self):
        self.click_element(self.jobs_link)
