import pytest

from config.config import TestData
from pages.LoginPage import LoginPage
from tests.TestBase import TestBase


class TestLogin(TestBase):

    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login(TestData.Email,TestData.Password)
        self.loginpage.click_on_login()
        error = self.loginpage.get_error()
        expected_error = "Invalid details. Please check the Email ID - Password combination."
        assert error == expected_error
