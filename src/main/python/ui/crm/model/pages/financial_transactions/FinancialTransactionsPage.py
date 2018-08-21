from time import sleep

from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.financial_transactions.FinancialTransactionInformationPage import \
    FinancialTransactionInformationPage
from src.main.python.utils.logs.Loging import Logging


class FinancialTransactionsPage(CRMBasePage):

    def __init__(self):
        super().__init__()

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
