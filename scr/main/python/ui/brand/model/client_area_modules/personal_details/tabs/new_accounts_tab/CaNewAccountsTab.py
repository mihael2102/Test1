import re
from time import sleep

from selenium.webdriver.common.by import By
from scr.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from scr.main.python.utils.logs.Loging import Logging


class CaNewAccountsTab(BrandBasePage):

    def __init__(self):
        super().__init__()

    '''
           Select currency from drop down
           :parameter currency
           return Manage Accounts Module  instance    
   '''

    def select_account_currency(self, currency):
        drop_down_currency = self.driver.find_element(By.XPATH, "//custom-select[@name='currency']")
        drop_down_currency.click()
        Logging().reportDebugStep(self, "Click the drop_down_currency: " + currency)
        sleep(1)
        select_currency = self.driver.find_element(By.XPATH,
                                                   "//custom-select[@name='currency']//following-sibling::*[contains(text(),'%s')]" % currency)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_currency)
        Logging().reportDebugStep(self, "Currency was selected: " + currency)
        select_currency.click()

        return CaNewAccountsTab()

    '''
         Return account id number   
    '''

    def get_account_id_text(self):
        new_account = super().wait_load_element(
            "//div[@class='tbody-wrap-pandats']//tr[last()]//td[@class='td-10-pandats'][1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", new_account)

        Logging().reportDebugStep(self, "Getting the account id text")
        return new_account.text

    '''
        Return the account currency text    
    '''

    def get_account_currency_text(self):
        new_account = super().wait_load_element(
            "//div[@class='tbody-wrap-pandats']//tr[last()]//td[@class='td-20-pandats'][1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", new_account)
        Logging().reportDebugStep(self, "Getting the account currency text")
        return new_account.text

    '''
        Set a deposit in the field initial_deposit
        return Manage Accounts Module instance  
    '''

    def set_initial_deposit(self, deposit):
        initial_deposit_field = self.driver.find_element(By.XPATH,
                                                         "//input[@class='initial-deposit-pandats ng-untouched ng-pristine ng-valid']")
        initial_deposit_field.clear()
        initial_deposit_field.send_keys(deposit)
        Logging().reportDebugStep(self, "Setting the initial deposit")
        return CaNewAccountsTab()

    '''
          Open the create_account_button 
          :return Manage Accounts Module instance    
    '''

    def create_account_button(self):
        create_account_button = super().wait_load_element(
            "//button[@class='forex-button-pandats']")
        create_account_button.click()
        Logging().reportDebugStep(self, "Create account button")
        return CaNewAccountsTab()

    '''
        Return the deposit balance number      
    '''

    def get_deposit_balance(self):
        balance = super().wait_load_element(
            "//div[@class='tbody-wrap-pandats']//tr[last()]//td[@class='td-20-pandats'][3]")

        balance_text = balance.text
        balance_split_text = balance_text.split(".")[0]
        balance_reg = re.sub('[$,£CA€]', '', balance_split_text)
        Logging().reportDebugStep(self, "Getting the deposit balance")
        return balance_reg
