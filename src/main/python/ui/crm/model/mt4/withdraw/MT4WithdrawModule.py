from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from time import sleep


class MT4WithdrawModule(CRMBasePage):
    # def __init__(self):
    #     super().__init__()
    #
    # '''
    #     Make withdraw from CRM
    #     :parameter account number,the account of client
    #     :parameter amount, the amount of establishing a withdraw
    #     :parameter payment method, the method set in the drop down
    #     :parameter withdraw status the status set in the drop down
    #     :parameter description withdraw the description set in the field
    #     returns  Client Profile  instance
    # '''

    def make_withdraw(self, account_number, amount, payment_method, withdraw_status, description_withdraw):
        self.select_payment_method(payment_method)
        self.select_status(withdraw_status)
        self.select_account(account_number)
        self.set_amount(amount)
        self.set_description(description_withdraw)
        self.create_withdraw_button()
        return ClientProfilePage()

    def make_withdraw_new_ui(self, payment_method, account_number, amount, description_withdraw, withdraw_status,
                             cleared_by):
        self.select_payment_method_new_ui(payment_method)
        self.select_status_new_ui(withdraw_status)
        self.select_account_new_ui(account_number)
        self.set_amount(amount)
        self.set_description(description_withdraw)
        self.select_cleared_by_new_ui(cleared_by)
        self.create_withdraw_button()
        return ClientProfilePage()

    '''
         Choice a payment method from drop down
         :parameter payment method the method of withdraw  in the drop down
        :returns MT4 Withdraw instance
    '''

    def select_payment_method(self, payment_method):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='payment_method']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='payment_method']"))
        select.select_by_visible_text(payment_method)
        Logging().reportDebugStep(self, "The payment method of withdraw module was selected: " + payment_method)
        return MT4WithdrawModule(self.driver)

    '''
        Choice a status  from drop down
        :parameter withdraw status the status of the withdraw e.g Approve,Pending....
        :returns MT4 Withdraw instance
    '''

    def select_status(self, withdraw_status):
        select = Select(self.driver.find_element(By.XPATH, "//select[@id='transaction_status_id']"))
        select.select_by_visible_text(withdraw_status)
        Logging().reportDebugStep(self, "The status of withdraw was selected: " + withdraw_status)
        return MT4WithdrawModule(self.driver)

    '''
       Choice an account from drop down
       :parameter account the account of the  client
       :returns MT4 Withdraw instance
    '''

    def select_account(self, account):
        drop_down = self.driver.find_element(By.XPATH, "//select[@name='loginserver']")

        drop_down.click()

        select_account = self.driver.find_element(By.XPATH, "//select[@name='loginserver']// \
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
        comment_filed = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element
        (self.__class__.__name__)["comment_filed"])
        comment_filed.clear()
        comment_filed.send_keys(description_withdraw)
        Logging().reportDebugStep(self, "The  description of withdraw module was set:  " + description_withdraw)
        return MT4WithdrawModule(self.driver)

    '''
        Create deposit button,confirmation of deposit
        :returns MT4 Withdraw instance
    '''

    def create_withdraw_button(self):
        create_withdraw_button = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element
            (self.__class__.__name__)["create_withdraw_button"])
        sleep(2)
        create_withdraw_button.click()
        Logging().reportDebugStep(self, "The Create withdraw button was clicked")
        return ClientProfilePage(self.driver)

    def select_cleared_by(self, provider):
        super().wait_element_to_be_clickable("//*[@id='cleared_by']")
        select = Select(self.driver.find_element_by_xpath("//*[@id='cleared_by']"))
        select.select_by_visible_text(provider)
        Logging().reportDebugStep(self, "The Cleared By of withdraw module was selected: " + provider)
        return MT4WithdrawModule(self.driver)

    #################################### NEW UI METHODS ########################################

    def select_payment_method_new_ui(self, payment_method):
        sleep(0.2)
        payment_method_item = super().wait_load_element("//span[text()='%s']" % payment_method)
        self.driver.execute_script("arguments[0].click();", payment_method_item)
        Logging().reportDebugStep(self, "The Payment method of withdraw module was selected: " + payment_method)
        return MT4WithdrawModule(self.driver)

    def select_status_new_ui(self, withdraw_status):
        status_item = super().wait_load_element("//span[text()='%s']" % withdraw_status)
        self.driver.execute_script("arguments[0].click();", status_item)
        Logging().reportDebugStep(self, "The Status of withdraw was selected: " + withdraw_status)
        return MT4WithdrawModule(self.driver)

    def select_account_new_ui(self, account):
        account_item = super().wait_load_element("//ul//span[contains(text(),'%s')]" % account)
        self.driver.execute_script("arguments[0].click();", account_item)
        Logging().reportDebugStep(self, "The Account of withdraw module was selected:  " + account)
        return MT4WithdrawModule(self.driver)

    def select_cleared_by_new_ui(self, provider):
        cleared_by_item = super().wait_load_element("//span[text()='%s']" % provider)
        self.driver.execute_script("arguments[0].click();", cleared_by_item)
        Logging().reportDebugStep(self, "The Cleared By of withdraw module was selected: " + provider)
        return MT4WithdrawModule(self.driver)
