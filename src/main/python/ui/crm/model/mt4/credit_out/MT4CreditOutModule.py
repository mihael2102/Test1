from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep
from selenium.webdriver.common.keys import Keys


class MT4CreditOutModule(CRMBasePage):

    # def __init__(self):
    #     super().__init__()
    #
    # '''
    #      Make credit out from CRM
    #      :parameter account number,the account of client
    #      :parameter amount, the amount of establishing a deposit
    #      :parameter description deposit the description set in the field
    #      :returns MT4 Credit Out instance
    # '''

    def make_credit_out(self, account_number, amount, comment, date):
        self.select_account(account_number)
        self.set_amount(amount)
        self.set_description(comment)
        self.set_expire_date(date)
        self.perform_create_credit_out()
        return ClientProfilePage()

    '''
        Select an account from drop down
        :parameter account the account of the client
        :returns MT4 Credit Out instance
    '''

    def select_account(self, account):
        drop_down = super().wait_element_to_be_clickable("//select[@name='loginserver']")
        drop_down.click()

        select_account = self.driver.find_element(By.XPATH, "//select[@name='loginserver']// \
                                                            following-sibling::*[contains(text(),'%s')]" % account)
        select_account.click()
        Logging().reportDebugStep(self, "The account for credit out was selected: " + account)
        return MT4CreditOutModule(self.driver)

    '''
        Set the amount in the field for deposit
        :parameter account the account of the client
        :returns MT4 Credit Out instance
    '''

    def set_amount(self, amount):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='amount']")
        amount_filed.clear()
        amount_filed.send_keys(amount)
        Logging().reportDebugStep(self, "The amount of credit out was set:  " + amount)
        return MT4CreditOutModule(self.driver)

    '''
        Set the description out the field 
        :parameter account the account of the  client
        :returns MT4 Credit Out instance
    '''

    def set_description(self, description_credit_in):
        comment_filed = self.driver.find_element(By.XPATH, "//textarea[@id='transaction_comment']")
        comment_filed.clear()
        comment_filed.send_keys(description_credit_in)
        Logging().reportDebugStep(self, "The Comment of credit out was set: " + description_credit_in)
        return MT4CreditOutModule(self.driver)

    '''
        Perform  credit out button 
        :returns MT4 Credit Out instance
    '''

    def set_granted_by(self, granted_by_text):
        granted_by_filed = self.driver.find_element(By.XPATH, "//input[@id='transaction_grantedBy']")
        granted_by_filed.clear()
        granted_by_filed.send_keys(granted_by_text)
        Logging().reportDebugStep(self, "The Granted by of credit out was set: " + granted_by_text)
        return MT4CreditOutModule(self.driver)

    def perform_create_credit_out(self):
        create_button = self.driver.find_element_by_xpath("(//button[contains(text(),'Save')])[3]")
        create_button.click()
        Logging().reportDebugStep(self, "Create of credit out button was clicked")
        return ClientProfilePage(self.driver)

    def get_credit_int(self):
        credit_text = self.driver.find_element_by_xpath("//span[@id='dtlview_Credit']").text
        credit = int((credit_text.split('.'))[0])
        Logging().reportDebugStep(self, "Actual credit amount is " + credit_text)
        return credit

    def set_expire_date(self, date):
        sleep(3)
        date_drop_down = self.driver.find_element(By.XPATH, "//input[@id='expire_date']")
        date_drop_down.clear()
        date_drop_down.send_keys(date)
        sleep(0.5)
        date_drop_down.send_keys(Keys.ENTER)
        Logging().reportDebugStep(self, "The expire date of credit out module was set:  " + date)
        return ClientProfilePage(self.driver)