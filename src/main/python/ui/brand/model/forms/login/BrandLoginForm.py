from time import sleep

import allure
from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.forms.login.BrandForgotPassword import BrandForgotPassword
from src.main.python.ui.brand.model.pages.trading_platform.BrandTradingPlatformPage import BrandTradingPlatformPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.utils.screenshot.ScreenShot import ScreenShot


class BrandLoginForm(BrandBasePage):

    def __init__(self):
        super().__init__()

    def set_fields(self, email, password):
        with allure.step("E-mail " + email + " and " + password + " are set"):
            self.loginFieldLocator = self.driver.find_element(By.XPATH, "//input[@name='login']")
        self.loginFieldLocator.clear()
        self.loginFieldLocator.send_keys(email)
        Logging().reportDebugStep(self, "Set the email field " + email + '\n')
        self.passwordFieldLocator = self.driver.find_element(By.XPATH, "//input[@name='password']")
        self.passwordFieldLocator.clear()
        self.passwordFieldLocator.send_keys(password)
        Logging().reportDebugStep(self, "Set the password " + password + '\n')
        return BrandLoginForm()

    def click_login_button(self):
        with allure.step("Click the 'Login' button"):
            self.loginButtonLocator = self.driver.find_element(By.XPATH,
                                                               "//button[@class='forex-button-pandats short-button-pandats "
                                                               "login-button-pandats']")
        self.loginButtonLocator.click()
        Logging().reportDebugStep(self, "Click the 'Login' button" + '\n')
        return BrandTradingPlatformPage()

    def click_login_button_with_invalid_password(self):
        self.loginButtonLocator = self.driver.find_element(By.XPATH,
                                                           "//button[@class='forex-button-pandats short-button-pandats "
                                                           "login-button-pandats']")
        self.loginButtonLocator.click()
        Logging().reportDebugStep(self, "Click the 'Login' button" + '\n')
        return BrandLoginForm()

    def get_invalid_login_message(self):
        sleep(2)
        message_locator = super().wait_load_element_present("//div[@class='toast-content-pandats']")
        return message_locator.text

    def open_forgot_password_link(self):
        forgot_password_link = super().wait_load_element_present("//a[contains(text(),'Forgot password')]")
        forgot_password_link.click()
        return BrandForgotPassword()
