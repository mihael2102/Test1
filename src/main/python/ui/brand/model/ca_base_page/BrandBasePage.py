#import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.utils.logs.Loging import Logging
from src.main.python.utils.waitting_utils.WaitingUtils import WaitingUtils
from src.main.python.utils.config import Config
from src.test.python.ui.automation.BaseTest import BaseTest


class BrandBasePage(object):

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

    def open_first_tab_page(self, url):
        self.driver.get(url)
        Config.window_before = self.driver.window_handles[0]

    def wait_load_element_present(self, element):
        return WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.XPATH, element)))

    def wait_element_to_be_clickable(self, element):
        return WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, element)))

    def wait_visible_of_element(self, element):
        return WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, element)))

    def get_amount_element(self, account, amount):
        return WaitingUtils().wait_until_element_present_ca(account, amount, self.driver)

    def switch_first_tab_page(self):
        self.driver.switch_to_window(Config.window_before)
        Logging().reportDebugStep(self, "Switch the first tab page")

    def switch_second_tab_page(self):
        self.driver.switch_to_window(Config.window_after)

    def came_back_on_previous_page(self):
        self.driver.back()

    def open_drop_down_menu(self):
        self.wait_load_element_present("//div[@class='button-pandats']")
        drop_down_panda = self.driver.find_element(By.XPATH, "//div[@class='button-pandats']")
        drop_down_panda.click()
        Logging().reportDebugStep(self, "Open the drop down menu")

    def back_on_previous_page(self):
        self.driver.back()

    def select_module(self, module):
        element_module = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='dropdown-pandats menu-pandats']//"
                                            "following-sibling::*[contains(text(),'%s')]" % module)))
        element_module.click()
        Logging().reportDebugStep(self, "Module was selected : " + module)

    def open_deposit_page(self):
        self.wait_load_element_present("//div[@class='button-pandats']")
        Logging().reportDebugStep(self, "Open deposit page")

    def wait_until_element_present(self, element):
        return WaitingUtils().wait_until_element_present_crm(element, self.driver)

    def close_client_area_pop_up(self):
        close_pop_up_icon = self.wait_load_element_present("//a[@class='close-popup-pandats']")
        close_pop_up_icon.click()

    def refreshing_wait(self):
        self.driver.refresh()

    def get_amount_by_account_text(self, account):
        return WaitingUtils().get_amount_by_account_text(account, self.driver)
