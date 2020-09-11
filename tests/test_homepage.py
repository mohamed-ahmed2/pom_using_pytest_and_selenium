import pytest
from tests.TestBase import TestBase
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

class TestHome(TestBase):


    def test_navigate_to_home(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_jobs()

    def test_links_are_visible(self):
        new_title = "Browse Jobs by Company, Location, Skills, Designation & Industry - Naukri.com"
        login_title = "Jobseeker's Login: Search the Best Jobs available in India & Abroad - Naukri.com"
        self.home = HomePage(self.driver)
        self.home.switch_to_tab(1)
        self.home.is_jobs_visible()
        self.home.is_Recruiters_visible()
        self.home.is_companies_visible()
        self.home.is_tools_visible()
        self.home.is_services_visible()
        self.home.is_more_visible()
        self.home.is_login_button_visible()
        current_title = self.home.get_title()
        assert current_title == new_title