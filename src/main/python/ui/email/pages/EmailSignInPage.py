from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.main.python.ui.email.pages.EmailHomePage import EmailHomePage
from src.main.python.utils.config import Config
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC

from src.test.python.ui.automation.BaseTest import BaseTest


class EmailSignInPage(object):

    def __init__(self) -> None:
        super().__init__()
        self.driver = BaseTest().get_driver

    def open_second_tab_page(self, url):
        self.driver.execute_script("window.open()")
        Config.window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(Config.window_after)
        self.driver.get(url)
        Logging().reportDebugStep(self, "The second tab was opened")
        return EmailSignInPage()

    def click_use_another_email(self):
        another_link = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "(//content)[3]//span")))
        another_link.click()
        another_email = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, ".//p[contains(text(),'Use another account')]")))
        another_email.click()
        Logging().reportDebugStep(self, "The another email was clicked")
        return EmailSignInPage()

    def set_login_email(self, login):
        login_field = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
        login_field.send_keys(login)
        Logging().reportDebugStep(self, "The email address was set: " + login)
        return EmailSignInPage()

    def set_password_email(self, password):
        password_field = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
        password_field.send_keys(password)
        Logging().reportDebugStep(self, "The password  was set: " + password)
        return EmailSignInPage()

    def click_first_next(self):
        next_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_button.click()
        Logging().reportDebugStep(self, "The next button was clicked")
        return EmailSignInPage()

    def click_second_next(self):
        next_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_button.click()
        Logging().reportDebugStep(self, "The next button was clicked")
        return EmailHomePage()
