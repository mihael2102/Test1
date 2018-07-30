from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskCreationTicket import HelpDeskCreationTicket
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskDetailViewPage import HelpDeskDetailViewPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskEditPage import HelpDeskEditPage
from src.main.python.utils.logs.Loging import Logging


class HelpDeskPage(CRMBasePage):
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
        return HelpDeskPage()

    def open_create_ticket_page(self):
        create_ticket_page_button = super().wait_load_element("//td[@class='moduleName']//button[1]")
        create_ticket_page_button.click()
        Logging().reportDebugStep(self, "The create ticket page was opened")
        return HelpDeskCreationTicket()

    def open_create_filter_pop_up(self):
        filter_button = super().wait_element_to_be_clickable("//a[@title='Create Filter']")
        filter_button.click()
        Logging().reportDebugStep(self, "The filter pop-up is opened")
        return FilterPage()

    def get_all_tab_text(self):
        all_tab = super().wait_element_to_be_clickable("//li[contains(text(),'All')]")
        all_tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'All')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_closed_tab_text(self):
        closed_tab = super().wait_element_to_be_clickable("//li[contains(text(),'Closed')]")
        closed_tab.click()
        sleep(1)
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'Closed')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab.text)
        return tab.text

    def get_in_progress_tab_text(self):
        in_progress = super().wait_element_to_be_clickable("//li[contains(text(),'In Progress')]")
        in_progress.click()
        sleep(1)
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'In Progress')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab.text)
        return tab.text

    def get_open_tab_text(self):
        open_tab = super().wait_element_to_be_clickable("//li[contains(text(),'Open')]")
        open_tab.click()
        sleep(1)
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'Open')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab.text)
        return tab.text

    def get_open_today_tab_text(self):
        open_today_tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Opened Today')]")
        open_today_tab_text.click()
        sleep(1)
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'Opened Today')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab.text)
        return tab.text

    def get_wait_for_response_tab_text(self):
        wait_for_response = super().wait_element_to_be_clickable("//li[contains(text(),'Wait For Response')]")
        wait_for_response.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//li[contains(text(),'Wait For Response')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

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

        return HelpDeskPage()

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
        return HelpDeskPage()

    def find_ticket_by_title(self, tittle):
        tittle_field = super().wait_load_element("//input[@name='tks_subject']")
        tittle_field.clear()
        tittle_field.send_keys(tittle)
        Logging().reportDebugStep(self, "The tittle was find: " + tittle)
        return HelpDeskPage()

    ''' 
         Perform  search ticket    
         :return Help Desk instance
    '''

    def perform_search_ticket(self):
        search_button = super().wait_load_element("//td[@class='txt_al_c']")
        search_button.click()
        Logging().reportDebugStep(self, "Perform search")
        return HelpDeskPage()

    def click_edit_ticket_pencil(self):
        pencil_link = super().wait_element_to_be_clickable("//div[@class='actions_wrapper']//a[@alt='Edit']")
        self.driver.execute_script("arguments[0].click();", pencil_link)
        Logging().reportDebugStep(self, "Click edit of the ticket by pencil link")
        return HelpDeskEditPage()

    def find_ticket_by_columns(self, ticket_number, related_to, priority, assigned_to, status, brand):
        self.enter_ticket_number(ticket_number)
        self.enter_related_to(related_to)
        self.enter_priority(priority)
        self.enter_assigned_to(assigned_to)
        self.enter_status(status)
        self.enter_brand(brand)

    def enter_ticket_number(self, ticket_number):
        ticket_number_field = super().wait_visible_of_element("//input[@id='tks_ticket_no']")
        ticket_number_field.send_keys(ticket_number)
        Logging().reportDebugStep(self, "The ticket number was entered: " + ticket_number)
        return HelpDeskPage()

    def enter_related_to(self, related_to):
        ticket_number_field = super().wait_visible_of_element("//input[@id='tks_parent_id']")
        ticket_number_field.send_keys(related_to)
        Logging().reportDebugStep(self, "The ticket number was entered: " + related_to)
        return HelpDeskPage()

    def enter_priority(self, priority):
        country_drop_down = self.driver.find_element(By.XPATH,
                                                     "//tr[@id='customAdvanceSearch']//td[8]//span[@class='multiselect-selected-text']")

        country_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[8]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(priority)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % priority)
        country_choice.click()

        country_drop_down.click()
        Logging().reportDebugStep(self, "The country was entered : " + priority)
        return HelpDeskPage()

    def enter_assigned_to(self, assigned_to):
        country_drop_down = self.driver.find_element(By.XPATH,
                                                     "//tr[@id='customAdvanceSearch']//td[8]//span[@class='multiselect-selected-text']")

        country_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[8]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(priority)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % assigned_to)
        country_choice.click()

        country_drop_down.click()
        Logging().reportDebugStep(self, "The country was entered : " + assigned_to)
        return HelpDeskPage()

    def enter_status(self, status):
        country_drop_down = self.driver.find_element(By.XPATH,
                                                     "//tr[@id='customAdvanceSearch']//td[8]//span[@class='multiselect-selected-text']")

        country_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@id='customAdvanceSearch']//td[8]//input[@class='form-control multiselect-search']")
        search_field.clear()
        search_field.send_keys(priority)
        country_choice = self.driver.find_element(By.XPATH,
                                                  "//label[contains(text(),'%s')]" % status)
        country_choice.click()

        country_drop_down.click()
        Logging().reportDebugStep(self, "The country was entered : " + status)
        return HelpDeskPage()

    def enter_brand(self, brand):
        ticket_number_field = super().wait_visible_of_element("//input[@id='tks_ticket_no']")
        ticket_number_field.send_keys(brand)
        Logging().reportDebugStep(self, "The brand was entered: " + brand)
        return HelpDeskPage()
