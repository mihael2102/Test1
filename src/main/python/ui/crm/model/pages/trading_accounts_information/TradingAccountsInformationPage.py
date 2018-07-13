from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class TradingAccountsInformationPage(CRMBasePage):

    def __init__(self):
        super().__init__()

    ''' 
        Returns the account text   
    '''

    def get_account_text(self):
        super().wait_load_element("//span[@id='dtlview_Trading Account Login']")
        count_id_field = self.driver.find_element(By.XPATH, "//span[@id='dtlview_Trading Account Login']")
        Logging().reportDebugStep(self, "Returns the account from crm: " + count_id_field.text)
        return count_id_field.text

    ''' 
        Returns the currency text   
    '''

    def get_currency_text(self):
        super().wait_load_element("//span[@id='dtlview_Trading Account Login']")
        currency_field = self.driver.find_element(By.XPATH, "//td[@class='dvtCellInfo']//font[1]")
        Logging().reportDebugStep(self, "Returns the currency from crm: " + currency_field.text)
        return currency_field.text

    ''' 
        Returns the balance text   
    '''

    def get_balance_text(self):
        balance_text = self.driver.find_element(By.XPATH, "//span[@id='dtlview_Balance']")
        parser_balance = balance_text.text.split(".")[0]
        Logging().reportDebugStep(self, "Returns the balance from crm: " + parser_balance)
        return parser_balance
