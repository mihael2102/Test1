from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.utils.config import Config
from src.main.python.utils.logs.Loging import Logging

from src.main.python.utils.waitting_utils.WaitingUtils import WaitingUtils
from src.test.python.ui.automation.BaseTest import BaseTest


class CRMBasePage(object):

    def __init__(self):
        self.driver = BaseTest().get_driver

    def open_second_tab_page(self, url):
        self.driver.execute_script("window.open()")
        Config.window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(Config.window_after)
        self.driver.get(url)

    def open_first_tab_page(self, url):
        self.driver.get(url)
        Config.window_before = self.driver.window_handles[0]

    def wait_load_element(self, element):
        return WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, element)))

    def wait_visible_of_element(self, element):
        return WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, element)))

    def switch_first_tab_page(self):
        self.driver.switch_to_window(Config.window_before)

    def switch_first_window_page(self):
        self.driver.switch_to_window(Config.window_before)

    def switch_second_tab_page(self):
        self.driver.switch_to_window(Config.window_after)

    def came_back_on_previous_page(self):
        self.driver.back()

    def open_deposit_page(self):
        self.wait_load_element("//div[@class='button-pandats']")

    def wait_until_element_present(self, element, total_amount_crm):
        return WaitingUtils().wait_until_element_present_crm(element, total_amount_crm, self.driver)

    def wait_element_to_be_clickable(self, element):
        return WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, element)))

    def perform_scroll(self, parameter):
        self.driver.execute_script("scroll(0, '%s');" % parameter)
        Logging().reportDebugStep(self, "Scroll was performed ")

    def perform_scroll_right(self, parameter):
        self.driver.execute_script("scroll('%s', 0);" % parameter)
        Logging().reportDebugStep(self, "Scroll was performed ")

    def refresh_page(self):
        sleep(3)
        self.driver.refresh()
        Logging().reportDebugStep(self, "The page is refreshed")

    def perform_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Logging().reportDebugStep(self, "Perform scroll down ")

    def click_ok(self):
        button = self.wait_load_element("//button[contains(text(),'OK')]")
        button.click()
        Logging().reportDebugStep(self, "The Ok button was clicked ")
