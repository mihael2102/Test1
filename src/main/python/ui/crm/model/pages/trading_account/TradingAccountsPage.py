from time import sleep

from datetime import *
import allure
from allure.constants import AttachmentType
from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.utils.logs.Loging import Logging


class TradingAccountsPage(CRMBasePage):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')

    def __init__(self):
        super().__init__()

    def open_create_filter_pop_up(self):
        element = super().wait_element_to_be_clickable("//a[contains(text(),'Create Filter')]")
        self.driver.execute_script("arguments[0].click();", element)
        Logging().reportDebugStep(self, "The filter pop-up is opened")
        return FilterPage()

    def select_filter(self, test_filter):
        drop_down_filter = super().wait_visible_of_element("//span[@class='filter-option pull-left']")

        drop_down_filter.click()

        sleep(2)
        select_test_filter = self.driver.find_element(By.XPATH,
                                                      "//span[contains(text(), '%s')]" % test_filter)

        select_test_filter.click()
        Logging().reportDebugStep(self, "The filter was selected: " + test_filter)

        return TradingAccountsPage()

    def get_show_all_tab_text(self):
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'All')]")
        tab.click()
        sleep(2)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'All')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        self.perform_screen_shot_trading_account("the live trading account tab " + self.now)
        return tab_text.text

    def get_balance_above_zero_tab_text(self):
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'Balance Above Zero')]")
        tab.click()
        sleep(2)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Balance Above Zero')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        self.perform_screen_shot_trading_account("the balance_above zero tab " + self.now)
        return tab_text.text

    def get_balance_below_zero_tab_text(self):
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'Balance Below Zero')]")
        tab.click()
        sleep(2)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Balance Below Zero')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        self.perform_screen_shot_trading_account("the balance below zero tab " + self.now)
        return tab_text.text

    def get_demo_trading_accounts_tab_text(self):
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'Demo Trading Accounts')]")
        tab.click()
        sleep(2)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Demo Trading Accounts')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        self.perform_screen_shot_trading_account("the demo_trading_accounts tab " + self.now)
        return tab_text.text

    def get_live_trading_account_tab_text(self):
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'Live Trading Account')]")
        tab.click()
        sleep(2)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Live Trading Account')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        self.perform_screen_shot_trading_account("the live trading account tab " + self.now)
        return tab_text.text

    def perform_screen_shot_trading_account(self, tab):
        allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(),
                                    type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed for " + tab)
        return TradingAccountsPage()
