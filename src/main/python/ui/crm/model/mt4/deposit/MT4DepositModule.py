from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class MT4DepositModule(CRMBasePage):

    '''
        Make deposit from CRM   
        :parameter account number,the account of client 
        :parameter amount, the amount of establishing a deposit
        :parameter payment method, the method set in the drop down
        :parameter deposit status the status set in the drop down
        :parameter description deposit the description set in the field 
        returns  Client Profile instance    
    '''

    def make_deposit(self, account_number, amount, payment_method, deposit_status, description_deposit):
        self.select_payment_method(payment_method)
        self.select_status(deposit_status)
        self.select_account(account_number)
        self.set_amount(amount)
        self.set_description(description_deposit)
        if global_var.current_brand_name == "kontofx" or global_var.current_brand_name == "libramarkets" or \
           global_var.current_brand_name == "dax-300" or (global_var.current_brand_name == "olympiamarkets") or \
           global_var.current_brand_name == "stox50" or global_var.current_brand_name == "aztrades":
            self.select_cleared_by()
        self.create_deposit()
        return ClientProfilePage(self.driver)

    '''
         Choice a payment method from drop down
         :parameter payment method the method of deposit  in the drop down
        :returns MT4 Deposit instance
    '''


    def select_cleared_by(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='cleared_by']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='cleared_by']"))
        select.select_by_visible_text("BTC")
        Logging().reportDebugStep(self, "The payment method of deposit module was selected: BTC")
        return MT4DepositModule()

    def select_payment_method(self, payment_method):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='payment_method']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='payment_method']"))
        select.select_by_visible_text(payment_method)
        Logging().reportDebugStep(self, "The payment method of deposit module was selected: " + payment_method)
        return MT4DepositModule()

    '''
        Select a status  from drop down
         :parameter deposit status the status of the deposit e.g Approve,Pending....
        :returns MT4 Deposit instance
    '''

    def select_status(self, deposit_status):
        select = Select(self.driver.find_element(By.XPATH, "//select[@id='transaction_status_id']"))
        if global_var.current_brand_name == "safemarkets":
            select.select_by_visible_text("Pending")
        else:
            select.select_by_visible_text(deposit_status)
        Logging().reportDebugStep(self, "The status of deposit module was selected:  " + deposit_status)
        return MT4DepositModule()

    '''
        Select an account from drop down
        :parameter account the account of the  client
        :returns MT4 Deposit instance
    '''

    def select_account(self, account):
        drop_down = self.driver.find_element(By.XPATH, "//select[@name='loginserver']")

        drop_down.click()

        select_account = self.driver.find_element(By.XPATH, "//select[@name='loginserver']//"
                                                            "following-sibling::*[contains(text(),'%s')]" % account)
        select_account.click()
        Logging().reportDebugStep(self, "The account of deposit module was selected:  " + account)
        return MT4DepositModule()

    '''
        Set the amount in the field for deposit
        :parameter account the live account of the client
        :returns MT4 Deposit instance
    '''

    def set_amount(self, amount):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='amount']")
        amount_filed.clear()
        amount_filed.send_keys(amount)
        Logging().reportDebugStep(self, "The amount of deposit module was set:  " + amount)
        return MT4DepositModule()

    '''
        Set the description in the field 
        :parameter account the account of the  client
        :returns MT4 Deposit instance
    '''

    def set_description(self, description_deposit):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='transaction_comment']")
        amount_filed.clear()
        amount_filed.send_keys(description_deposit)
        Logging().reportDebugStep(self,
                                  "The  description of deposit module was set in the description field:  " + description_deposit)
        return MT4DepositModule()

    '''
        Create deposit button
        :returns MT4 Deposit instance
    '''

    def create_deposit(self):
        create_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Create')]")
        create_button.click()
        Logging().reportDebugStep(self, "The create withdraw button of deposit module was clicked")
        return ClientProfilePage()
