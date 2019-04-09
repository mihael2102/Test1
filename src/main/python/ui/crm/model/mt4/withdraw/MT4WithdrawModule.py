from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging


class MT4WithdrawModule(CRMBasePage):
    # def __init__(self):
    #     super().__init__()

    # '''
    #     Make withdraw from CRM
    #     :parameter account number,the account of client
    #     :parameter amount, the amount of establishing a withdraw
    #     :parameter payment method, the method set in the drop down
    #     :parameter withdraw status the status set in the drop down
    #     :parameter description withdraw the description set in the field
    #     returns  Client Profile  instance
    # '''

    def make_withdraw(self, account_number, amount, payment_method, withdraw_status, description_withdraw, cleared_by):
        self.select_payment_method(payment_method)
        self.select_status(withdraw_status)
        self.select_account(account_number)
        self.set_amount(amount)
        self.set_description(description_withdraw)
        try:
            self.set_cleared_by(cleared_by)
        except:
            return self
        self.create_withdraw_button()
        return ClientProfilePage(self.driver)

    '''
         Choice a payment method from drop down
         :parameter payment method the method of withdraw  in the drop down
        :returns MT4 Withdraw instance
    '''

    def set_cleared_by(self, cleared_by):
        try:
            amount_filed = self.driver.find_element(By.XPATH, "//input[@id='cleared_by']")
            amount_filed.clear()
            amount_filed.send_keys(cleared_by)
            Logging().reportDebugStep(self, "The cleared by was set:  " + cleared_by)
        except:
            return self
        return MT4WithdrawModule(self.driver)

    def select_payment_method(self, payment_method):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='payment_type']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@id='payment_type']"))
        select.select_by_visible_text(payment_method)
        Logging().reportDebugStep(self, "The payment method of withdraw was selected: " + payment_method)
        return MT4WithdrawModule(self.driver)

    '''
        Choice a status  from drop down
        :parameter withdraw status the status of the withdraw e.g Approve,Pending....
        :returns MT4 Withdraw instance
    '''

    def select_status(self, withdraw_status):
        select = Select(self.driver.find_element(By.XPATH, "//select[@id='transaction_status_id']"))
        select.select_by_visible_text(withdraw_status)
        Logging().reportDebugStep(self, "The status of withdraw module was selected:  " + withdraw_status)
        return MT4WithdrawModule(self.driver)

    '''
       Choice an account from drop down
       :parameter account the account of the  client
       :returns MT4 Withdraw instance
    '''

    def select_account(self, account):
        drop_down = super().wait_element_to_be_clickable("//select[@name='loginserver']")
        drop_down.click()
        select_account = super().wait_load_element("//select[@name='loginserver']// \
                                                            following-sibling::*[contains(text(),'%s')]" % account)
        select_account.click()
        Logging().reportDebugStep(self, "The account of withdraw module was selected:  " + account)
        return MT4WithdrawModule(self.driver)

    '''
       Set the amount in the field for deposit
       :parameter account the live account of the  client
       :returns MT4 Withdraw instance
    '''

    def set_amount(self, amount):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='amount']")
        amount_filed.clear()
        amount_filed.send_keys(amount)
        Logging().reportDebugStep(self, "The amount of withdraw module was set:  " + amount)
        return MT4WithdrawModule(self.driver)

    '''
       Set the description in the field 
       :parameter account the account of the  client
       :returns MT4 Withdraw instance
    '''

    def set_description(self, description_withdraw):
        amount_filed = self.driver.find_element(By.XPATH, "//textarea[@id='transaction_comment']")
        amount_filed.clear()
        amount_filed.send_keys(description_withdraw)
        Logging().reportDebugStep(self, "The  description of withdraw module was set:  " + description_withdraw)
        return MT4WithdrawModule(self.driver)

    '''
        Create deposit button,confirmation of deposit
        :returns MT4 Withdraw instance
    '''

    def create_withdraw_button(self):
        create_button = self.driver.find_element(By.XPATH, "(//button[contains(text(),'Save')])[3]")
        create_button.click()
        Logging().reportDebugStep(self, "The create withdraw button of withdraw module was clicked")
        return ClientProfilePage(self.driver)
