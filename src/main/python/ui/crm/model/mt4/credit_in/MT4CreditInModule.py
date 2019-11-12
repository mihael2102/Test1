from time import sleep
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging


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

    def make_credit_in_new_ui(self, account_number, amount, day, month, year, garanted_by, comment):
        self.select_trading_account_new_ui(account_number)
        self.set_amount(amount)
        self.set_expire_date_new_ui(day, month, year)
        self.set_garanted_by(garanted_by)
        self.set_description(comment)
        self.perform_create_credit_in()
        return ClientProfilePage(self.driver)

    '''
        Choice an account from drop down
        :parameter account the account of the  client
        :returns MT4 Credit In instance
    '''

    def select_account(self, account):
        drop_down = super().wait_element_to_be_clickable("//select[@name='loginserver']")
        drop_down.click()

        select_account = self.driver.find_element(By.XPATH, "//select[@name='loginserver']//"
                                                            "following-sibling::*[contains(text(),'%s')]" % account)
        select_account.click()
        Logging().reportDebugStep(self, "The account of deposit in module was selected:  " + account)
        return MT4CreditInModule()

    '''
        Set the amount in the field for deposit
        :parameter account the account of the client
        :returns MT4 Credit In instance
    '''

    def set_amount(self, amount):
        amount_filed = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element
        (self.__class__.__name__)["amount_filed"])
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
        description_filed = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element
                                                        (self.__class__.__name__)["description_filed"], timeout=5)
        description_filed.clear()
        description_filed.send_keys(description_credit_in)
        Logging().reportDebugStep(self, "The Comment was set: " + description_credit_in)
        return MT4CreditInModule()

    '''
        Perform  credit in button 
        :returns MT4 Deposit instance
    '''

    def perform_create_credit_in(self):
        create_button = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element
                                                        (self.__class__.__name__)["create_button"], timeout=5)
        create_button.click()
        Logging().reportDebugStep(self, "Perform the create Credit in was clicked")
        return ClientProfilePage()

####################################### NEW UI METHODS #########################################

    def select_trading_account_new_ui(self, account):
        account_item = super().wait_load_element("//span[contains(text(),'%s')]" % account)
        self.driver.execute_script("arguments[0].click();", account_item)
        Logging().reportDebugStep(self, "The trading account for Credit In was selected:  " + account)
        return MT4CreditInModule()

    def set_expire_date_new_ui(self, day, month, year):
        date_field = super().wait_load_element(
            "//div[contains(label,'Expire date')]//following-sibling::mat-form-field")
        self.driver.execute_script("arguments[0].click();", date_field)
        current_date_btn = super().wait_load_element(
            "(//span[@class='mat-button-wrapper' and contains(text(),'2019')])[1]")
        current_date_btn.click()
        select_year = super().wait_load_element("//div[contains(text(),'%s')]" % year)
        select_year.click()
        select_month = super().wait_load_element("//div[contains(text(),'%s')]" % month)
        select_month.click()
        select_day = super().wait_load_element("(//div[contains(text(),'%s')])[1]" % day)
        select_day.click()
        set_btn = super().wait_load_element("(//span[text()='Set'])[1]")
        set_btn.click()
        Logging().reportDebugStep(self, "The Expire date was set")
        return MT4CreditInModule(self.driver)

    def set_garanted_by(self, garanted_by):
        garanted_by_field = super().wait_load_element("//input[@formcontrolname='grantedBy']")
        garanted_by_field.clear()
        garanted_by_field.send_keys(garanted_by)
        Logging().reportDebugStep(self, "The Garanted by was set:  " + garanted_by)
        return MT4CreditInModule()
