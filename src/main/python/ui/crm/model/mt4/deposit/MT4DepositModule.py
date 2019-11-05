from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.MT4ModuleConstants import MT4ModuleConstants
from time import sleep


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
                global_var.current_brand_name == "olympiamarkets":
            self.select_cleared_by(MT4ModuleConstants.CLEARED_BY)
        if global_var.current_brand_name == "dax-300" or global_var.current_brand_name == "stox50" or \
                global_var.current_brand_name == "aztrades":
            self.select_cleared_by(MT4ModuleConstants.CLEARED_BY1)
        self.create_deposit()
        return ClientProfilePage(self.driver)

    def make_deposit_new_ui(self, account_number, amount, payment_method, deposit_status, description_deposit,
                            cleared_by):
        self.select_payment_method_new_ui(payment_method)
        self.select_status_new_ui(deposit_status)
        self.select_account_new_ui(account_number)
        self.set_amount(amount)
        self.set_description(description_deposit)
        self.select_cleared_by_new_ui(cleared_by)
        self.create_deposit()
        return ClientProfilePage(self.driver)

    '''
         Choice a payment method from drop down
         :parameter payment method the method of deposit  in the drop down
        :returns MT4 Deposit instance
    '''

    def select_cleared_by(self, cleared_by):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='cleared_by']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='cleared_by']"))
        select.select_by_visible_text(cleared_by)
        Logging().reportDebugStep(self, "The cleared_by of deposit module was selected: " + cleared_by)
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
        Logging().reportDebugStep(self, "The status of deposit module was selected: " + deposit_status)
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
        Logging().reportDebugStep(self, "The account of deposit module was selected: " + account)
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
        Logging().reportDebugStep(self, "The amount of deposit module was set: " + amount)
        return MT4DepositModule()

    '''
        Set the description in the field 
        :parameter account the account of the  client
        :returns MT4 Deposit instance
    '''

    def set_description(self, description_deposit):
        description_filed = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element
            (self.__class__.__name__)["description_filed"])
        description_filed.clear()
        description_filed.send_keys(description_deposit)
        Logging().reportDebugStep(self, "The description of deposit was set: " + description_deposit)
        return MT4DepositModule()

    '''
        Create deposit button
        :returns MT4 Deposit instance
    '''

    def create_deposit(self):
        create_deposit_button = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element
            (self.__class__.__name__)["create_deposit_button"])
        create_deposit_button.click()
        Logging().reportDebugStep(self, "The Create Deposit button was clicked")
        return ClientProfilePage()

    ######################################## NEW UI METHODS ###################################

    def select_payment_method_new_ui(self, method):
        sleep(0.1)
        payment_method = super().wait_load_element("//span[text()='%s']" % method)
        self.driver.execute_script("arguments[0].click();", payment_method)
        Logging().reportDebugStep(self, "The payment method of deposit module was selected: " + method)
        return MT4DepositModule()

    def select_status_new_ui(self, status):
        sleep(0.1)
        status_item = super().wait_load_element("//span[text()='%s']" % status)
        self.driver.execute_script("arguments[0].click();", status_item)
        Logging().reportDebugStep(self, "The status of deposit module was selected: " + status)
        return MT4DepositModule()

    def select_account_new_ui(self, account):
        sleep(0.1)
        account_item = super().wait_load_element("//span[contains(text(),'%s')]" % account)
        self.driver.execute_script("arguments[0].click();", account_item)
        Logging().reportDebugStep(self, "The account number of deposit module was selected: " + account)
        return MT4DepositModule()

    def select_cleared_by_new_ui(self, cleared_by):
        try:
            cleared_by_item = super().wait_load_element("//span[text()='%s']" % cleared_by)
            self.driver.execute_script("arguments[0].click();", cleared_by_item)
            Logging().reportDebugStep(self, "The Cleared by was selected: " + cleared_by)
        except:
            Logging().reportDebugStep(self, "The Cleared by pick-list is not existing")
        return MT4DepositModule()
