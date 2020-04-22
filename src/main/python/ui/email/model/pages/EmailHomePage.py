from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.main.python.utils.config import Config
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC

from src.test.python.ui.automation.BaseTest import BaseTest


class EmailHomePage(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def enter_subject(self, subject):
        subject_filed = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='aso_search_form_anchor']/div/input")))
        subject_filed.send_keys(subject)
        Logging().reportDebugStep(self, "The subject was entered: " + subject)
        return EmailHomePage(self.driver, self.config)

    def open_second_tab_page(self, url):
        self.driver.execute_script("window.open()")
        Config.window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(Config.window_after)
        self.driver.get(url)
        Logging().reportDebugStep(self, "The second tab was opened : " + url)
        return EmailHomePage(self.driver, self.config)

    def click_searching_button(self):
        search_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Search Mail']")
        search_button.click()
        Logging().reportDebugStep(self, "The search button was clicked")
        return EmailHomePage(self.driver, self.config)

    def click_exist_subject_link(self, subject):
        try:
            sleep(2)
            subject_link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//*[contains(text(),'%s')])[4]" % subject)))
            subject_link.click()
        except:
            self.refresh_page()
            sleep(2)
            subject_link = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "(//*[contains(text(),'%s')])[4]" % subject)))
            subject_link.click()
        Logging().reportDebugStep(self, "The subject link was clicked: " + subject)
        return EmailHomePage(self.driver, self.config)

    def click_tool_tip(self):
        tool_tip_link = self.driver.find_element(By.XPATH, "(//img[@data-tooltip='Show details'])[1]")
        tool_tip_link.click()
        Logging().reportDebugStep(self, "The tool tip was opened ")
        return EmailHomePage(self.driver, self.config)

    def get_support_email(self):
        support_email = self.driver.find_element(By.XPATH, "(//span[@class='go'])[2]")
        Logging().reportDebugStep(self, "The support email was getting: " + support_email.text)
        return support_email.text

    def get_comment_text(self):
        sleep(1)
        description = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='listitem']/div/div/div/div/div/div/div/div/div")))\
                .get_attribute("innerText")
        Logging().reportDebugStep(self, "The body of mail is: " + description)
        return description

    def open_google_accounts(self):
        self.driver.set_page_load_timeout(30)
        google_accounts_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//a)[33]//span")))
        google_accounts_button.click()
        Logging().reportDebugStep(self, "The google accounts  was clicked")
        return EmailHomePage(self.driver, self.config)

    def perform_sign_out(self):
        google_accounts_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, ".//a[@id='gb_71']")))
        google_accounts_button.click()
        Logging().reportDebugStep(self, "The google accounts  was clicked")
        return EmailHomePage(self.driver, self.config)

    def click_home_page_icon(self):
        home_page_icon = self.driver.find_element(By.XPATH, "//a[@title='Gmail']")
        home_page_icon.click()
        Logging().reportDebugStep(self, "The home page icon was clicked")
        return EmailHomePage(self.driver, self.config)

    def refresh_page(self):
        self.driver.refresh()
        Logging().reportDebugStep(self, "The page is refreshed")
        return EmailHomePage(self.driver, self.config)
