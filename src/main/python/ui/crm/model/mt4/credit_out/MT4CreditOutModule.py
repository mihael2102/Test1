from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from src.main.python.utils.logs.Loging import Logging


class MT4CreditOutModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    '''
         Make credit out from CRM   
         :parameter account number,the account of client 
         :parameter amount, the amount of establishing a deposit
         :parameter description deposit the description set in the field 
         :returns MT4 Credit Out instance   
    '''

    def make_credit_out(self, account_number, amount, comment):
        self.select_account(account_number)
        self.set_amount(amount)
        self.set_description(comment)
        self.perform_create_credit_out()
        return CRMClientProfilePage()

    '''
        Select an account from drop down
        :parameter account the account of the client
        :returns MT4 Credit Out instance
    '''

    def select_account(self, account):
        drop_down = super().wait_element_to_be_clickable("//select[@name='loginserver']")
        drop_down.click()

        select_account = self.driver.find_element(By.XPATH, "//select[@name='loginserver']//"
                                                            "following-sibling::*[contains(text(),'%s')]" % account)
        select_account.click()
        Logging().reportDebugStep(self, "The account of deposit out module was selected:  " + account)
        return MT4CreditOutModule()

    '''
        Set the amount in the field for deposit
        :parameter account the account of the client
        :returns MT4 Credit Out instance
    '''

    def set_amount(self, amount):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='amount']")
        amount_filed.clear()
        amount_filed.send_keys(amount)
        Logging().reportDebugStep(self, "The amount of credit out module was set:  " + amount)
        return MT4CreditOutModule()

    '''
        Set the description out the field 
        :parameter account the account of the  client
        :returns MT4 Credit Out instance
    '''

    def set_description(self, description_credit_in):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='transaction_comment']")
        amount_filed.clear()
        amount_filed.send_keys(description_credit_in)
        Logging().reportDebugStep(self, "The description of credit out module was set in the description field:  " +
                                  description_credit_in)
        return MT4CreditOutModule()

    '''
        Perform  credit out button 
        :returns MT4 Credit Out instance
    '''

    def perform_create_credit_out(self):
        create_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Create')]")
        create_button.click()
        Logging().reportDebugStep(self, "Perform the create of credit out module was clicked")
        return CRMClientProfilePage()
