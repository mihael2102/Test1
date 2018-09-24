from time import sleep

from datetime import *
import allure
from allure.constants import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsInformationPage import \
    TradingAccountsInformationPage
from src.main.python.utils.logs.Loging import Logging


class TradingAccountsPage(CRMBasePage):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')

    # def __init__(self):
    #     super().__init__()

    def open_create_filter_pop_up(self):
        element = super().wait_element_to_be_clickable("//a[contains(text(),'Create Filter')]")
        self.driver.execute_script("arguments[0].click();", element)
        Logging().reportDebugStep(self, "The filter pop-up is opened")
        return FilterPage(self.driver)

    def select_filter(self, test_filter):
        drop_down_filter = super().wait_visible_of_element("//span[@class='filter-option pull-left']")

        drop_down_filter.click()

        sleep(2)
        select_test_filter = self.driver.find_element(By.XPATH,
                                                      "//span[contains(text(), '%s')]" % test_filter)

        select_test_filter.click()
        Logging().reportDebugStep(self, "The filter was selected: " + test_filter)

        return TradingAccountsPage()

    def perform_searching_trading_account(self, trading_account, server, currency, balance, equity,
                                          assigned_to):
        self.enter_trading_account(trading_account)
        self.select_server(server)
        # self.select_brand(brand)
        self.enter_currency(currency)
        self.enter_balance(balance)
        self.enter_equity(equity)
        self.enter_assigned_to(assigned_to)
        self.click_search_button()
        return TradingAccountsPage()

    def open_client_login(self, account_login):
        sleep(2)
        select_test_filter = self.driver.find_element(By.XPATH,
                                                      "//a[contains(text(), '%s')]" % account_login)

        select_test_filter.click()
        return TradingAccountsInformationPage()

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

    def enter_trading_account(self, trading_account):
        sleep(2)
        trading_account_field = self.driver.find_element(By.XPATH, "//input[@name='tks_login']")
        trading_account_field.clear()
        trading_account_field.send_keys(trading_account)
        Logging().reportDebugStep(self, "The trading_account was entered : " + trading_account)
        return TradingAccountsPage()

    def select_server(self, server):
        server_drop_down = self.driver.find_element(By.XPATH,
                                                    "//tr[@id='customAdvanceSearch']//td[3]")

        server_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//*[@id='customAdvanceSearch']/td[3]//div/input")
        search_field.clear()
        search_field.send_keys(server)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % server)
        country_choice.click()
        server_drop_down.click()
        Logging().reportDebugStep(self, "The server was selected : " + server)
        return TradingAccountsPage()

    # def select_brand(self, brand):
    #     brand_drop_down = self.driver.find_element(By.XPATH,
    #                                                "//tr[@id='customAdvanceSearch']//td[4]")
    #
    #     brand_drop_down.click()
    #     search_field = self.driver.find_element(By.XPATH,
    #                                             "//*[@id='customAdvanceSearch']/td[4]//div/input")
    #     search_field.clear()
    #     search_field.send_keys(brand)
    #     country_choice = self.driver.find_element(By.XPATH,
    #                                               "//label[contains(text(),'%s')]" % brand)
    #     country_choice.click()
    #     brand_drop_down.click()
    #     Logging().reportDebugStep(self, "The brand( was selected : " + brand)
    #     return TradingAccountsPage()

    def enter_currency(self, currency):
        currency_drop_down = self.driver.find_element(By.XPATH,
                                                      "//tr[@id='customAdvanceSearch']//td[5]")

        currency_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//*[@id='customAdvanceSearch']/td[5]//div/input")
        search_field.clear()
        search_field.send_keys(currency)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % currency)
        country_choice.click()
        currency_drop_down.click()
        Logging().reportDebugStep(self, "The currency was selected : " + currency)
        return TradingAccountsPage()

    def enter_balance(self, balance):
        balance_field = self.driver.find_element(By.XPATH,
                                                 "//tr[@id='customAdvanceSearch']//td[6]//div/input")
        balance_field.clear()
        balance_field.send_keys(balance)
        Logging().reportDebugStep(self, "The balance was entered : " + balance)
        return TradingAccountsPage()

    def enter_equity(self, equity):
        equity_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[8]//div/input")
        equity_field.clear()
        equity_field.send_keys(equity)
        Logging().reportDebugStep(self, "The equity was entered : " + equity)
        return TradingAccountsPage()

    def enter_assigned_to(self, assigned_to):
        currency_drop_down = self.driver.find_element(By.XPATH,
                                                      "//tr[@id='customAdvanceSearch']//td[9]")

        currency_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//*[@id='customAdvanceSearch']/td[9]//div/input")
        search_field.clear()
        search_field.send_keys(assigned_to)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % assigned_to)
        country_choice.click()
        currency_drop_down.click()
        Logging().reportDebugStep(self, "The assigned to was selected : " + assigned_to)
        return TradingAccountsPage()

    def click_search_button(self):
        search_button = super().wait_element_to_be_clickable("//td[@class='txt_al_c']")
        search_button.click()
        Logging().reportDebugStep(self, "The search button was clicked ")
        return TradingAccountsPage()

    def get_first_name_column(self):
        name_first_column = super().wait_element_to_be_clickable(
            "//table[@id='resizeble_cols']//td[2]")
        Logging().reportDebugStep(self, "First column name  : " + name_first_column.text)
        return name_first_column.text

    def get_second_name_column(self):
        name_second_column = self.driver.find_element(By.XPATH,
                                                      "//table[@id='resizeble_cols']//td[3]")
        Logging().reportDebugStep(self, "Second column name: " + name_second_column.text)
        return name_second_column.text

    def get_third_name_column(self):
        name_third_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[4]")
        Logging().reportDebugStep(self, "Third column name: " + name_third_column.text)
        return name_third_column.text

    def get_fourth_name_column(self):
        name_fourth_column = self.driver.find_element(By.XPATH,
                                                      "//table[@id='resizeble_cols']//td[5]")
        Logging().reportDebugStep(self, "Fourth column name : " + name_fourth_column.text)
        return name_fourth_column.text

    def get_fifth_name_column(self):
        name_fifth_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[6]")
        Logging().reportDebugStep(self, "Fifth column name : " + name_fifth_column.text)
        return name_fifth_column.text

    def get_sixth_name_column(self):
        name_sixth_column = self.driver.find_element(By.XPATH,
                                                     "//table[@id='resizeble_cols']//td[7]")
        Logging().reportDebugStep(self, "Sixth column name : " + name_sixth_column.text)
        return name_sixth_column.text

    def get_seventh_name_column(self):
        name_seventh_column = self.driver.find_element(By.XPATH,
                                                       "//table[@id='resizeble_cols']//td[8]")
        Logging().reportDebugStep(self, "Seventh column name : " + name_seventh_column.text)
        return name_seventh_column.text

    def get_eighth_name_column(self):
        name_eighth_column = self.driver.find_element(By.XPATH,
                                                      "//table[@id='resizeble_cols']//td[9]")
        Logging().reportDebugStep(self, "Eighth column name : " + name_eighth_column.text)
        return name_eighth_column.text
