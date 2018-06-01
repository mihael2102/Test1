from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage


class CRMTradingAccountsInformationPage(CRMBasePage):

    def __init__(self):
        super().__init__()

    ''' 
        Returns the account text   
    '''

    def get_account_text(self):
        super().wait_load_element("//span[@id='dtlview_Trading Account Login']")
        count_id_field = self.driver.find_element(By.XPATH, "//span[@id='dtlview_Trading Account Login']")
        return count_id_field.text

    ''' 
        Returns the currency text   
    '''

    def get_currency_text(self):
        super().wait_load_element("//span[@id='dtlview_Trading Account Login']")
        count_id_field = self.driver.find_element(By.XPATH, "//td[@class='dvtCellInfo']//font[1]")
        return count_id_field.text

    ''' 
        Returns the balance text   
    '''

    def get_balance_text(self):
        balance_text = self.driver.find_element(By.XPATH, "//span[@id='dtlview_Balance']")
        return balance_text.text
