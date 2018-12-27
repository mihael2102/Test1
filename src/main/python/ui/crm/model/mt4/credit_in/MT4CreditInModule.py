from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
import time

class MT4CreditInModule(CRMBasePage):
    # def __init__(self) -> None:
    #     super().__init__()

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
        return ClientProfilePage(self.driver)

    '''
        Choice an account from drop down
        :parameter account the account of the  client
        :returns MT4 Credit In instance
    '''

    def select_account(self, account):
        time.sleep(3)
        drop_down = self.driver.find_element(By.XPATH, "//*[@id='loginserver']")
        self.driver.execute_script("arguments[0].click();", drop_down)
        # drop_down.click()

        select_account = self.wait_element_to_be_clickable(
            "//select[@id='loginserver']/option[contains(text(),'%s')]" % account)
        # select_account.click()
        self.driver.execute_script("arguments[0].click();", select_account)

        # drop_down = super().wait_element_to_be_clickable("//select[@name='loginserver']")
        # drop_down.click()
        #
        # select_account = self.driver.find_element(By.XPATH, "//select[@name='loginserver']//"
        #                                                     "following-sibling::*[contains(text(),'%s')]" % account)
        # select_account.click()
        Logging().reportDebugStep(self, "The account of deposit in module was selected:  " + account)
        return MT4CreditInModule()

    '''
        Set the amount in the field for deposit
        :parameter account the account of the client
        :returns MT4 Credit In instance
    '''

    def set_amount(self, amount):
        sleep(3)
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='amount']")
        amount_filed.clear()
        amount_filed.send_keys(amount)
        Logging().reportDebugStep(self, "The amount of credit in module was set:  " + amount)
        return MT4CreditInModule()

    '''
        Set the expire date in the drop down 
        :parameter date the selecting date in the calendar
        :returns MT4 CreditIn instance
    '''

    def set_expire_date(self, date):
        sleep(3)
        date_drop_down = self.driver.find_element(By.XPATH, "//input[@id='expire_date']")
        date_drop_down.clear()
        date_drop_down.send_keys(date)
        sleep(0.5)
        date_drop_down.send_keys(Keys.ENTER)
        Logging().reportDebugStep(self, "The expire date of credit in module was set:  " + date)
        return MT4CreditInModule()

    '''
        Set the description in the field 
        :parameter account the account of the  client
        :returns MT4 Deposit instance
     '''

    def set_description(self, description_credit_in):
        sleep(2)
        amount_filed = super().wait_element_to_be_clickable("//*[@id='transaction_comment']", timeout=5)
        amount_filed.clear()
        amount_filed.send_keys(description_credit_in)
        Logging().reportDebugStep(self, "The  description of credit in module was set in the description field:  " +
                                  description_credit_in)
        return MT4CreditInModule()

    '''
        Perform  credit in button 
        :returns MT4 Deposit instance
    '''

    def perform_create_credit_in(self):
        # for_old_forex
        sleep(2)
        create_button = self.wait_element_to_be_clickable("//*[@id='mt_interaction']/div/div[4]/button[2]")
        #self.driver.execute_script("arguments[0].click();", create_button)
        create_button.click()
        Logging().reportDebugStep(self, "The create withdraw button of deposit module was clicked")
        return ClientProfilePage()
