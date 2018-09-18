from time import sleep

from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.financial_transactions.FinancialTransactionInformationPage import \
    FinancialTransactionInformationPage
from src.main.python.utils.logs.Loging import Logging


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
        tab = self.driver.find_element(By.XPATH, "//li[contains(text(),'Credit Out')]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Credit Out')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_demo_accounts_transactions_tab_text(self):
        tab = self.driver.find_element(By.XPATH, "//li[contains(text(),'Demo Accounts Transactions')]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Demo Accounts Transactions')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_deposits_tab_text(self):
        tab = self.driver.find_element(By.XPATH, "//li[contains(text(),'Deposits')]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Deposits')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_withdraw_tab_text(self):
        tab = self.driver.find_element(By.XPATH, "//li[contains(text(),'Withdraw')]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Withdraw')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def open_first_transactions(self):
        transaction_number = self.driver.find_element(By.XPATH, "//tr[@class='lvtColData']//td[2]")
        transaction_number.click()
        return FinancialTransactionInformationPage()

    def get_transaction_id(self):
        transaction_number_element = self.driver.find_element(By.XPATH, "(//a[contains(text(), 'MTT')])[3]")
        return transaction_number_element.text

    def get_client_name(self):
        client_name_element = self.driver.find_element(By.XPATH, "(//td[3]/div/a)[3]")
        return client_name_element.text

    def get_transaction_type(self):
        transaction_type_element = self.driver.find_element(By.XPATH, "(//*[@id='listBody']//tr/td[4])[3]")
        return transaction_type_element.text

    def get_modified_time(self):
        modified_time_element = self.driver.find_element(By.XPATH, "(//*[@id='listBody']//tr/td[10])[3]")
        return modified_time_element.text

    def get_trading_account(self):
        trading_account_element = self.driver.find_element(By.XPATH, "(//*[@id='listBody']//tr/td[12])[3]//a")
        return trading_account_element.text

    def perform_searching_trading_account_via_filters(self, transaction_number, client_name, transaction_type_text,
                                                      modified_time, trading_account):
        self.enter_transaction_number(transaction_number)
        self.enter_client_name(client_name)
        self.enter_transaction_type_text(transaction_type_text)
        self.enter_modified_time(modified_time)
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
        transaction_type_drop_down = self.driver.find_element(By.XPATH, "//td[4]/div/div[1]/button")
        transaction_type_drop_down.click()

        transaction_type_field = self.driver.find_element(By.XPATH, "(//div/div[1]/ul/li[1]/div/input)[1]")
        transaction_type_field.clear()
        transaction_type_field.send_keys(transaction_type_text)
        transaction_type_checkbox = self.driver.find_element(By.XPATH, "//td[4]/div/div[1]/ul/li[5]/a/label/input")
        transaction_type_checkbox.click()
        Logging().reportDebugStep(self, "In filter the transaction_type was entered: " + transaction_type_text)
        return FinancialTransactionsPage(self.driver)

    def enter_modified_time(self, modified_time):
        modified_time_field = self.driver.find_element(By.XPATH, "//input[@name='tks_modifiedtime_date1']")
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
        transaction_number_element = self.driver.find_element(By.XPATH, "//a[contains(text(), 'MTT')]")
        transaction_number_element.click()
        Logging().reportDebugStep(self, "First financial transaction in search results was opened")
        return FinancialTransactionInformationPage(self.driver)
