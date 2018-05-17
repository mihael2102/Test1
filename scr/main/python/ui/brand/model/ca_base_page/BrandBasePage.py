from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scr.main.python.utils.waitting_utils.WaitingUtils import WaitingUtils
from scr.main.python.utils.config import Config


class BrandBasePage(object):

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

    def get_amount_element(self, account, amount):
        return WaitingUtils().wait_until_element_present_ca(account, amount, self.driver)

    def switch_first_tab_page(self):
        self.driver.switch_to_window(Config.window_before)

    def switch_second_tab_page(self):
        self.driver.switch_to_window(Config.window_after)

    def came_back_on_previous_page(self):
        self.driver.back()

    def open_drop_down_menu(self):
        self.wait_load_element("//div[@class='button-pandats']")
        drop_down_panda = self.driver.find_element(By.XPATH, "//div[@class='button-pandats']")
        drop_down_panda.click()

    def back_on_previous_page(self):
        self.driver.back()

    def select_module(self, module):
        element_module = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='dropdown-pandats menu-pandats']//"
                                            "following-sibling::*[contains(text(),'%s')]" % module)))
        element_module.click()

    def open_deposit_page(self):
        self.wait_load_element("//div[@class='button-pandats']")

    def wait_until_element_present(self, element):
        return WaitingUtils().wait_until_element_present_crm(element, self.driver)

    def close_client_area_pop_up(self):
        close_pop_up_icon = self.wait_load_element("//a[@class='close-popup-pandats']")
        close_pop_up_icon.click()

    def refreshing_wait(self):
        self.driver.refresh()

    def get_amount_by_account_text(self, account):
        return WaitingUtils().get_amount_by_account_text(account, self.driver)
