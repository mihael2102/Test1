from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage


class MT4CreditInModule(CRMBasePage):
    def __init__(self) -> None:
        super().__init__()

    '''
        Make credit in from CRM   
        :parameter account number,the account of client 
        :parameter amount, the amount of establishing a deposit
        :parameter description deposit the description set in the field 
        returns  MT4 Credit In instance    
    '''

    def make_credit_in(self, account_number, amount, expire_date, comment):
        self.select_account(account_number)
        self.set_amount(amount)
        self.set_expire_date(expire_date)
        self.set_description(comment)
        self.perform_create_credit_in()
        return CRMClientProfilePage()

    '''
        Select an account from drop down
        :parameter account the account of the  client
        :returns MT4 Credit In instance
    '''

    def select_account(self, account):
        drop_down = super().wait_element_to_be_clickable("//select[@name='loginserver']")
        drop_down.click()

        select_account = self.driver.find_element(By.XPATH, "//select[@name='loginserver']//"
                                                            "following-sibling::*[contains(text(),'%s')]" % account)
        select_account.click()
        return MT4CreditInModule()

    '''
        Set the amount in the field for deposit
        :parameter account the account of the client
        :returns MT4 Credit In instance
    '''

    def set_amount(self, amount):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='amount']")
        amount_filed.clear()
        amount_filed.send_keys(amount)
        return MT4CreditInModule()

    '''
        Set the expire date in the drop down 
        :parameter date the selecting date in the calendar
        :returns MT4 CreditIn instance
    '''

    def set_expire_date(self, date):
        date_drop_down = self.driver.find_element(By.XPATH, "//input[@id='expire_date']")
        date_drop_down.clear()
        date_drop_down.send_keys(date)
        date_drop_down.send_keys(Keys.ENTER)
        return MT4CreditInModule()

    '''
        Set the description in the field 
        :parameter account the account of the  client
        :returns MT4 Deposit instance
     '''

    def set_description(self, description_deposit):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='transaction_comment']")
        amount_filed.clear()
        amount_filed.send_keys(description_deposit)
        return MT4CreditInModule()

    def perform_create_credit_in(self):
        create_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Create')]")
        create_button.click()
        return CRMClientProfilePage()
