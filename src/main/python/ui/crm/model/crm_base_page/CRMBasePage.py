from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.utils.config import Config

from src.main.python.utils.waitting_utils.WaitingUtils import WaitingUtils


class CRMBasePage(object):

    def __init__(self):
        self.driver = Config.browser

    def open_second_tab_page(self, url):
        self.driver.execute_script("window.open()")
        Config.window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(Config.window_after)
        self.driver.get(url)

    def open_first_tab_page(self, url):
        self.driver.get(url)
        Config.window_before = self.driver.window_handles[0]

    def wait_load_element(self, element):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, element)))

    def refreshing_wait(self, account):
        return WaitingUtils().wait_until_element_present_ca(account, self.driver)

    def switch_first_tab_page(self):
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
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, element)))
