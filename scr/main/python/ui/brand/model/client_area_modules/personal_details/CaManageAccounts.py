from selenium.webdriver.common.by import By

from scr.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from scr.main.python.ui.brand.model.client_area_modules.personal_details.tabs.new_accounts_tab.CaNewAccountsTab import CaNewAccountsTab
from scr.main.python.ui.brand.model.client_area_modules.personal_details.tabs.transfer_funds_tab.CaTransferBetweenTab import \
    CaTransferBetweenTab
from scr.main.python.utils.logs.Loging import Logging


class CaManageAccounts(BrandBasePage):

    def __init__(self):
        super().__init__()

    '''
        Open the account button 
        return Manage Accounts Module  instance   
    '''

    def open_new_account_button(self):
        new_account = super().wait_load_element(
            "//button[@class='forex-button-pandats']//following-sibling::*[contains(text(),'Open New Account')]")
        new_account.click()
        Logging().reportDebugStep(self, "Open a new account")
        return CaNewAccountsTab()

    '''
         Open the demo account in CA
         return Manage Accounts Module instance  
    '''

    def open_demo_button(self):
        demo_button = self.driver.find_element(By.XPATH,
                                               "//li[@class ='header-menu-pandats']//span[contains(text(),'Demo')]")
        demo_button.click()
        Logging().reportDebugStep(self, "Open the demo button")
        return CaManageAccounts()

    def switch_first_tab_page(self):
        super().switch_first_tab_page()
        return CaManageAccounts()

    def refresh(self):
        self.driver.refresh()
        return CaManageAccounts()

    def get_amount_element(self, account, amount):
        return super().get_amount_element(account, amount)

    '''
         Open the transfer_between_accounts  
         return Brand Transfer Between Tab  instance   
    '''

    def open_transfer_between_accounts_button(self):
        transfer_between_button = super().wait_load_element(
            "//button[contains(text(),'Transfer Between Accounts')]")
        transfer_between_button.click()
        Logging().reportDebugStep(self, "Open a Transfer Between Accounts button")
        return CaTransferBetweenTab()

    '''
         Return account amount by id text
    '''

    def get_amount_by_account_text(self, account):
        return super().get_amount_by_account_text(account)


