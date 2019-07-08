from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.financial_transactions.FinancialTransactionInformationPage import \
    FinancialTransactionInformationPage
from src.main.python.utils.logs.Loging import Logging
import datetime
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import autoit

class FinancialTransactionsPage(CRMBasePage):

    # def __init__(self):
    #     super().__init__()

    def get_all_tab_text(self):
        tab = self.driver.find_element(By.XPATH, "//li[contains(text(),'All')]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'All')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_credit_in_tab_text(self):
        tab = self.driver.find_element(By.XPATH, "//li[contains(text(),'Credit In')]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Credit In')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_credit_out_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["tab"])
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable(
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["tab"])
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_demo_accounts_transactions_tab_text(self):
        demo_tab = self.driver.find_element(
            By.XPATH,
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["demo_tab"])
        demo_tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable(
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["demo_tab"])
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_decline_tab_text(self):
        decline_tab = self.driver.find_element(By.XPATH, "//li[contains(text(),'Decline')]")
        decline_tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Decline')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_deposits_tab_text(self):
        deposits_tab = self.driver.find_element(
            By.XPATH,
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["deposits_tab"])
        deposits_tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable(
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["deposits_tab"])
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_withdraw_tab_text(self):
        withdraw_tab = self.driver.find_element(
            By.XPATH,
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["withdraw_tab"])
        withdraw_tab.click()
        sleep(1)
        self.wait_loading_to_finish(35)
        tab_text = super().wait_load_element(
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["withdraw_tab"]).text
        Logging().reportDebugStep(self, "Returns the tab name: " + tab_text)
        return tab_text

    def open_first_transactions(self):
        transaction_number = self.driver.find_element(By.XPATH, "//tr[@class='lvtColData']//td[2]")
        transaction_number.click()
        return FinancialTransactionInformationPage()

    def get_transaction_id_by_position_from_list(self, position_in_list=3):
        if position_in_list != 3:
            sleep(2)    # Waiting until page reloading will be finished

        if (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "rimarkets-staging"):
            sleep(3)

        transaction_number_element = self.driver.find_element(By.XPATH,
                                                              "(//a[contains(text(), 'MTT')])[%s]" % position_in_list)
        Logging().reportDebugStep(self, "Returns the transaction_id: " + transaction_number_element.text)
        return transaction_number_element.text

    def get_client_name_by_position_from_list(self, position_in_list=3):
        if position_in_list != 3:
            sleep(2)    # Waiting until page reloading will be finished
        client_name_element = self.driver.find_element(
            By.XPATH,
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["client_name_element"]
            % position_in_list)
        Logging().reportDebugStep(self, "Returns the client name: " + client_name_element.text)
        return client_name_element.text

    def get_transaction_type_by_position_from_list(self, position_in_list=3):
        if position_in_list != 3:
            sleep(2)    # Waiting until page reloading will be finished
        transaction_type_element = self.driver.find_element(
            By.XPATH,
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["transaction_type_element"]
            % position_in_list)
        Logging().reportDebugStep(self, "Returns the transaction type: " + transaction_type_element.text)
        return transaction_type_element.text

    def get_modified_time_by_position_from_list(self, position_in_list=3):
        if position_in_list != 3:
            sleep(2)    # Waiting until page reloading will be finished
        modified_time_element = self.driver.find_element(
            By.XPATH,
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["modified_time_element"]
            % position_in_list)
        Logging().reportDebugStep(self, "Returns the modified time: " + modified_time_element.text)
        return modified_time_element.text

    def is_modified_time_in_search_results(self, modified_time):
        # Get collection of time search results because search does not consider hours/minutes but only date
        sleep(2)
        # current_year = datetime.datetime.now().year
        current_year = modified_time[6:11]
        modified_time_elements = self.driver.find_elements(
                By.XPATH,
                "//div[@class='main_tbl_wrapper']//tbody[@id = 'listBody']//td[contains(text(), '%s')]" % current_year)
        Logging().reportDebugStep(self, "looking for created/modified time...")
        for time_item in modified_time_elements:
            Logging().reportDebugStep(self, "Time from the page list: " + time_item.text)
            if time_item.text == modified_time:
                Logging().reportDebugStep(self, "Correct time has been found: " + time_item.text)
                return True
        Logging().reportDebugStep(self, "Initial time has not been found!")
        return False

    def get_trading_account_by_position_from_list(self, position_in_list=3):
        if position_in_list != 3:
            sleep(2)    # Waiting until page reloading will be finished
        if global_var.current_brand_name == "itrader":
            sleep(5)
        trading_account_element = self.driver.find_element(
            By.XPATH,
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["trading_account_element"]
            % position_in_list)
        Logging().reportDebugStep(self, "Returns the trading account: " + trading_account_element.text)
        return trading_account_element.text

    def perform_searching_trading_account_via_filters(self, transaction_number, client_name, transaction_type_text,
                                                      trading_account):
        self.enter_transaction_number(transaction_number)
        self.enter_client_name(client_name)
        if global_var.current_brand_name != "forex_staging":
            self.enter_transaction_type_text(transaction_type_text)
        # self.enter_modified_time(modified_time)
        self.enter_trading_account(trading_account)
        self.click_search_button()
        return FinancialTransactionsPage(self.driver)

    def enter_transaction_number(self, transaction_number):
        sleep(2)
        transaction_number_field = self.driver.find_element(By.XPATH, "//input[@name='tks_transaction_no']")
        transaction_number_field.clear()
        transaction_number_field.send_keys(transaction_number)
        Logging().reportDebugStep(self, "In filter the transaction number was entered: " + transaction_number)
        return FinancialTransactionsPage(self.driver)

    def enter_client_name(self, client_name):
        client_name_field = self.driver.find_element(By.XPATH, "//input[@name='tks_vtigeraccountid']")
        client_name_field.clear()
        client_name_field.send_keys(client_name)
        Logging().reportDebugStep(self, "In filter the client_name was entered: " + client_name)
        return FinancialTransactionsPage(self.driver)

    def enter_transaction_type_text(self, transaction_type_text):
        transaction_type_drop_down = self.driver.find_element(By.XPATH,
            global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["transaction_type_drop_down"])
        transaction_type_drop_down.click()
        transaction_type_field = self.driver.find_element(
            By.XPATH,
            "(//select[contains(@name, 'tks_transactiontype')]//..//input)[1]")
        transaction_type_field.clear()
        transaction_type_field.send_keys(transaction_type_text)
        transaction_type_checkbox = self.driver.find_element(By.XPATH,
                             "//li/a/label[@class='checkbox']/input[contains(@value, '%s')]" % transaction_type_text)
        transaction_type_checkbox.click()
        Logging().reportDebugStep(self, "In filter the transaction_type was entered: " + transaction_type_text)
        return FinancialTransactionsPage(self.driver)

    def enter_modified_time(self, modified_time):
        modified_time_field = self.driver.find_element(By.XPATH, "//input[@name='tks_createdtime_date1']")
        modified_time_field.clear()
        modified_time_field.send_keys(modified_time)
        Logging().reportDebugStep(self, "In filter the modified_time was entered: " + modified_time)
        return FinancialTransactionsPage(self.driver)

    def enter_trading_account(self, trading_account):
        trading_account_field = self.driver.find_element(By.XPATH, "//input[@name='tks_tradingaccountsid']")
        trading_account_field.clear()
        trading_account_field.send_keys(trading_account)
        Logging().reportDebugStep(self, "In filter the trading_account was entered: " + trading_account)
        return FinancialTransactionsPage(self.driver)

    def click_search_button(self):
        search_button = super().wait_element_to_be_clickable("//td[@class='txt_al_c']/input")
        search_button.click()
        Logging().reportDebugStep(self, "The search button was clicked ")
        return FinancialTransactionsPage(self.driver)

    def open_first_financial_transaction_in_list(self):
        sleep(2)
        if global_var.current_brand_name == "rimarkets-staging":
            sleep(3)
        transaction_number_element = self.driver.find_element(By.XPATH, "//a[contains(text(), 'MTT')]")
        self.scroll_into_view(transaction_number_element)
        transaction_number_element.click()
        Logging().reportDebugStep(self, "First financial transaction in search results was opened")
        return FinancialTransactionInformationPage(self.driver)

    def open_search_form(self):
        search_form_element = self.driver.find_element(By.XPATH, "//tr/td[1]/div/button[1]")
        search_form_element.click()
        Logging().reportDebugStep(self, "Search form was opened")
        return FinancialTransactionsPage(self.driver)

    def __fill_search_field_with_value(self, search_value):
        search_input = self.driver.find_element(By.XPATH, "//input[@name='search_text']")
        search_input.clear()
        search_input.send_keys(search_value)

    def __click_search_now_button(self):
        search_now_button = self.driver.find_element(By.XPATH, "//input[@value=' Search Now ']")
        search_now_button.click()

    def __change_search_criteria_by_visible_text(self, criteria_from_drop_down_list):
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='search_field']"))
        select.select_by_visible_text(criteria_from_drop_down_list)

    def search_for_transaction_id(self, transaction_id):
        self.__change_search_criteria_by_visible_text("Transaction No")
        self.__fill_search_field_with_value(transaction_id)
        self.__click_search_now_button()
        Logging().reportDebugStep(self, "Searching for transaction ID: %s was performed" % transaction_id)
        return FinancialTransactionsPage(self.driver)

    def search_for_client_name(self, client_name):
        self.__change_search_criteria_by_visible_text("Client")
        self.__fill_search_field_with_value(client_name)
        self.__click_search_now_button()
        Logging().reportDebugStep(self, "Searching for client name: %s was performed" % client_name)
        return FinancialTransactionsPage(self.driver)

    def search_for_transaction_type(self, transaction_type):
        self.__change_search_criteria_by_visible_text(TestDataConstants.TRANSACTION_TYPE)
        self.__fill_search_field_with_value(transaction_type)
        self.__click_search_now_button()
        Logging().reportDebugStep(self, "Searching for transaction type: %s was performed" % transaction_type)
        return FinancialTransactionsPage(self.driver)

    def search_for_modified_time(self, modified_time):
        self.__change_search_criteria_by_visible_text(TestDataConstants.CREATED_TIME)
        self.__fill_search_field_with_value(modified_time)
        self.__click_search_now_button()
        Logging().reportDebugStep(self, "Searching for modified time: %s was performed" % modified_time)
        return FinancialTransactionsPage(self.driver)

    def search_for_trading_account(self, trading_account):
        self.__change_search_criteria_by_visible_text("Trading Account")
        self.__fill_search_field_with_value(trading_account)
        self.__click_search_now_button()
        Logging().reportDebugStep(self, "Searching for trading account: %s was performed" % trading_account)
        return FinancialTransactionsPage(self.driver)

    def click_select_all_checkbox(self):
        sleep(1)
        element = self.driver.find_element(By.XPATH, "//*[@id='selectCurrentPageRec']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        select_checkbox = super().wait_element_to_be_clickable("//*[@id='selectCurrentPageRec']")
        self.driver.execute_script("arguments[0].click();", select_checkbox)
        sleep(1)
        select_all_records = super().wait_element_to_be_clickable("//*[@id='selectAllRec']")
        sleep(1)
        select_all_records.click()
        Logging().reportDebugStep(self, "Select all checkbox")
        return FinancialTransactionsPage(self.driver)

    def click_export(self):
        sleep(1)
        element = self.driver.find_element(By.XPATH, "//button[@title='Export Financial Transactions']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(1)
        button_export = super().wait_element_to_be_clickable("//button[@title='Export Financial Transactions']")
        # button_export.click()
        self.driver.execute_script("arguments[0].click();", button_export)
        Logging().reportDebugStep(self, "Click export")
        return FinancialTransactionsPage(self.driver)

    def click_export_pop_ups(self):
        button_export = super().wait_element_to_be_clickable("//*[@id='exportpopupcontent']/form/div[2]/button[2]")
        self.driver.execute_script("arguments[0].click();", button_export)
        Logging().reportDebugStep(self, "Click export in pop ups")
        return FinancialTransactionsPage(self.driver)

    def click_save_as(self, name_file):
        sleep(3)
        autoit.win_wait_active("Сохранение")
        sleep(2)
        autoit.control_send("Сохранение", "Edit1", "%s" % name_file)
        autoit.send("{ENTER}")
        return FinancialTransactionsPage(self.driver)

    def select_xls_format(self):
        sleep(2)
        radio_xls = super().wait_element_to_be_clickable("//*[@value='excel']")
        self.driver.execute_script("arguments[0].click();", radio_xls)
        Logging().reportDebugStep(self, "Select xls format")
        return FinancialTransactionsPage(self.driver)

    def scroll_financial_transaction(self):
        element = self.driver.find_element(By.XPATH, "//*[@id='selectCurrentPageRec']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return FinancialTransactionsPage(self.driver)
