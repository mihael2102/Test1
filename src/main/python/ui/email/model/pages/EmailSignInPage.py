from time import sleep

from pytest import fail
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.main.python.ui.email.model.pages.EmailHomePage import EmailHomePage
from src.main.python.utils.config import Config
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from src.test.python.ui.automation.BaseTest import BaseTest


class EmailSignInPage(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def open_second_tab_page(self, url):
        self.driver.execute_script("window.open()")
        Config.window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(Config.window_after)
        self.driver.get(url)
        Logging().reportDebugStep(self, "The second tab was opened")
        return EmailSignInPage(self.driver, self.config)

    def click_use_another_email(self):
        try:
            sleep(3)
            if self.driver.find_element(By.XPATH, "(//content)[3]//span").is_displayed():
                self.driver.find_element(By.XPATH, "(//content)[3]//span").click()
                self.click_another_method()
        except (NoSuchElementException, StaleElementReferenceException):
            if self.driver.find_element(By.XPATH, "//div[@id='profileIdentifier']").is_displayed():
                self.driver.find_element(By.XPATH, "//div[@id='profileIdentifier']").click()
                self.click_another_method()
            else:
                raise NoSuchElementException()
        return EmailSignInPage(self.driver, self.config)

    def click_another_method(self):
        another_email = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, ".//p[contains(text(),'Use another account')]")))
        another_email.click()
        Logging().reportDebugStep(self, "The another email was clicked")
        return EmailSignInPage(self.driver, self.config)

    def set_login_email(self, login):
        login_field = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
        login_field.send_keys(login)
        Logging().reportDebugStep(self, "The email address was set: " + login)
        return EmailSignInPage(self.driver, self.config)

    def set_password_email(self, password):
        password_field = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
        password_field.send_keys(password)
        Logging().reportDebugStep(self, "The password  was set: " + password)
        return EmailSignInPage(self.driver, self.config)

    def click_first_next(self):
        try:
            next_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Weiter')]")
            next_button.click()
        except:
            next_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
            next_button.click()
        Logging().reportDebugStep(self, "The next button was clicked")
        return EmailSignInPage(self.driver, self.config)

    def click_second_next(self):
        try:
            next_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Weiter')]")
            next_button.click()
        except:
            next_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
            next_button.click()
        Logging().reportDebugStep(self, "The next button was clicked")
        return EmailHomePage(self.driver, self.config)
