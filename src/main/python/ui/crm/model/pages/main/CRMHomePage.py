from time import sleep
from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.help_desk.CRMHelpDesk import CRMHelpDesk
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from src.test.python.utils.XpathDataConstants import XpathDataConstants
from src.main.python.utils.config import Config

class CRMHomePage(CRMBasePage):

    def __init__(self):
        super().__init__()

    ''' 
        Select the filter in drop-down   
       :parameter test_filter the filter that is created in the filters drop down
       :return Home Page instance
    '''

    def select_filter(self, test_filter):
        drop_down_filter = super().wait_load_element("//span[@class='filter-option pull-left']")

        drop_down_filter.click()
        Logging().reportDebugStep(self, "Click the  drop down filter ")
        field_found = self.driver.find_element(By.XPATH, "//input[@class='input-block-level form-control']")
        field_found.clear()
        field_found.send_keys(test_filter)
        Logging().reportDebugStep(self, "The field found is : " + test_filter)
        select_test_filter = self.driver.find_element(By.XPATH, "//li[@rel='22']")
        select_test_filter.click()
        Logging().reportDebugStep(self, "Click on selected filter")
        return CRMHomePage()

    ''' 
         Select the filter in drop-down   
         :parameter email the email of exist user
         :parameter password the password of exist user
         :return Client Profile Page instance
    '''

    def find_client(self, email):
        sleep(2)
        email_field = self.driver.find_element(By.XPATH, "//input[@id='tks_email1']")

        email_field.send_keys(email)
        Logging().reportDebugStep(self, "Setting  the user's email in the email field  is : " + email)
        search_button = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        search_button.click()
        Logging().reportDebugStep(self, "Click the search button ")
        sleep(2)
        client_id = self.driver.find_element(By.XPATH, Config.data.get_xpath_data(XpathDataConstants.CRM_ID))
        client_id.click()
        Logging().reportDebugStep(self, "Clicking on user's name by email : ")
        return CRMClientProfilePage()

    ''' 
         Returns the account id   
    '''

    def get_account_id(self):
        print("account")

    '''
         Select the crm page again
         return  Home Page instance 
    '''

    def switch_second_tab_page(self):
        super().switch_second_tab_page()
        Logging().reportDebugStep(self, "switch the second tab ")
        return CRMHomePage()

    ''' 
        Open the help desk module 
        return Help Desk instance  
    '''

    def open_help_desk_module(self):
        help_desc_module = super().wait_load_element("//a[contains(text(), 'Help Desk')]")
        help_desc_module.click()
        Logging().reportDebugStep(self, "Open  the help desk module ")
        return CRMHelpDesk()

    def refresh(self):
        self.driver.refresh()
        Logging().reportDebugStep(self, "Perform the refresh ")
        return CRMHelpDesk()
