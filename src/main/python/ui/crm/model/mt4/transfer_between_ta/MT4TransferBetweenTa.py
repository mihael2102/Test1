from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MT4TransferBetweenTa(CRMBasePage):
    # def __init__(self):
    #     super().__init__()

    def make_transfer_between_ta(self, first_account, second_account, amount, description_transfer):
        self.select_first_account(first_account)
        self.select_second_account(second_account)
        self.set_amount(amount)
        self.set_description(description_transfer)
        self.create_transfer()

    '''
        Select first account from drop down for transfer between
        :parameter account, the live account of the client
        :returns MT4 Transfer Between Ta instance
    '''

    def select_first_account(self, first_account):
        drop_down = super().wait_element_to_be_clickable("//select[@name='sourceloginserver']")
        drop_down.click()
        select_account = self.driver.find_element(By.XPATH, "//select[@name='sourceloginserver']//"
                                                            "following-sibling::*[contains(text(),'%s')]" % first_account)
        select_account.click()
        Logging().reportDebugStep(self, "The first account selected:  " + first_account)
        return MT4TransferBetweenTa(self.driver)

    '''
        Select second account from drop down for transfer between
        :parameter account the live account of the client
        :returns MT4 Transfer Between Ta instance
    '''

    def select_second_account(self, second_account):
        drop_down = super().wait_element_to_be_clickable("//select[@name='destinationlogin']")
        drop_down.click()
        select_account = self.driver.find_element(By.XPATH, "//select[@name='destinationlogin']//"
                                                            "following-sibling::*[contains(text(),'%s')]" % second_account)
        select_account.click()
        Logging().reportDebugStep(self, "The second account selected:  " + second_account)
        return MT4TransferBetweenTa(self.driver)

    '''
        Set the amount in the field for deposit
        :parameter account the live account of the client
        :returns MT4 Transfer Between Ta instance
    '''

    def set_amount(self, amount):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='amount']")
        amount_filed.clear()
        amount_filed.send_keys(amount)
        Logging().reportDebugStep(self, "The amount of transfer between ta module was set:  " + amount)
        return MT4TransferBetweenTa(self.driver)

    '''
       Set the description in the field 
       :parameter account the account of the  client
       :returns MT4 Transfer Between Ta instance
   '''

    def set_description(self, description_deposit):
        amount_filed = self.driver.find_element(By.XPATH, "//textarea[@id='transfer_comment']")
        amount_filed.clear()
        amount_filed.send_keys(description_deposit)
        Logging().reportDebugStep(self,
                                  "The description of transfer between ta was set: " + description_deposit)
        return MT4TransferBetweenTa(self.driver)

    '''
        Create deposit button
        :returns CRM Client Profile Page instance
    '''

    def create_transfer(self):
        sleep(1)
        create_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Create')]")
        create_button.click()
        Logging().reportDebugStep(self, "The Create button was clicked")
        return ClientProfilePage(self.driver)
