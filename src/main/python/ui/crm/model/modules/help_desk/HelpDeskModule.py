import re
from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskDetailViewPage import HelpDeskDetailViewPage
from src.main.python.utils.logs.Loging import Logging


class HelpDeskModule(CRMBasePage):
    def __init__(self):
        super().__init__()

    ''' 
        Open the today tabs  
        :return Help Desk instance  
    '''

    def opened_today_tab(self):
        tab = super().wait_load_element("//li[contains(text(),'Opened Today')]")
        tab.click()
        Logging().reportDebugStep(self, "The today tab was opened")
        return HelpDeskModule()

    '''
         Open the ticket number 
         :return Help Desk instance  
    '''

    def open_ticket_number(self):
        sleep(2)
        ticket_number = super().wait_load_element("//div[@class='link_field']")
        ticket_number.click()
        Logging().reportDebugStep(self, "Open ticket number")
        return HelpDeskDetailViewPage()

    ''' 
        Select the filter in drop-down   
        :parameter test_filter the filter that is created in the filters drop down
        :return Help Desk instance
    '''

    def select_filter(self, test_filter):
        sleep(2)
        drop_down_filter = super().wait_load_element("//span[@class='filter-option pull-left']")

        drop_down_filter.click()

        sleep(2)
        select_test_filter = self.driver.find_element(By.XPATH,
                                                      "//span[contains(text(), '%s')]" % test_filter)

        select_test_filter.click()
        Logging().reportDebugStep(self, "The filter was selected: " + test_filter)

        return HelpDeskModule()

    ''' 
         Returns the ticket status  
         :parameter ticket_id the ticket id  from CA 
         :return Help Desk instance
    '''

    def find_ticket_by_id(self, ticket_id):
        field_id = super().wait_load_element("//input[@name='tks_bl_id']")
        field_id.clear()
        field_id.send_keys(ticket_id)
        Logging().reportDebugStep(self, "The ticket was find: " + ticket_id)
        return HelpDeskModule()

    ''' 
         Perform  search ticket    
         :return Help Desk instance
    '''

    def perform_search_ticket(self):
        search_button = super().wait_load_element("//td[@class='txt_al_c']")
        search_button.click()
        Logging().reportDebugStep(self, "Perform search")
        return HelpDeskModule()
