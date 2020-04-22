import re
from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage



class CaServiceDesk(CRMBasePage):



    '''
       Open the ticket tabs 
       :return Service Desk instance  
    '''

    def open_tickets_tab(self):
        sleep(2)
        create_ticket_button = super().wait_visible_of_element("//span[contains(text(),'Open Tickets')]")
        create_ticket_button.click()
        Logging().reportDebugStep(self, "Ticket tab is opened")
        return CaServiceDesk()

    ''' 
        Create a new ticket
       :return Service Desk instance
    '''

    def create_new_ticket(self):
        create_ticket_button = super().wait_visible_of_element("//button[contains(text(),'Create New Ticket')]")
        create_ticket_button.click()
        Logging().reportDebugStep(self, "The new ticket was created")
        return CaServiceDesk()

    ''' 
        Set a subject in the field 
        :return Service Desk instance   
    '''

    def set_subject_field(self, subject):
        subject_field = self.driver.find_element(By.XPATH, "//input[@name='subject']")
        subject_field.clear()
        subject_field.send_keys(subject)
        Logging().reportDebugStep(self, "Subject is set: " + subject)
        return CaServiceDesk()

    ''' 
         Set a category  in the drop-down 
         :return Service Desk instance   
    '''

    def set_category_drop_down(self, category):
        category_drop_down = self.driver.find_element(By.XPATH, "//custom-select[@name='category']")
        category_drop_down.click()
        select_category = self.driver.find_element(By.XPATH, "//custom-select[@name='category']//"
                                                             "following-sibling::*[contains(text(),'%s')]" % category)
        select_category.click()
        Logging().reportDebugStep(self, "The category was selected : " + category)
        return CaServiceDesk()

    ''' 
        Set a description  in the field 
        :return Service Desk instance   
    '''

    def set_description(self, description):
        description_field = self.driver.find_element(By.XPATH, "//textarea[@name='description']")
        description_field.clear()
        description_field.send_keys(description)
        Logging().reportDebugStep(self, "Description  was set in the field : : " + description)
        return CaServiceDesk()

    ''' 
        Open a new ticket button 
        :return Service Desk instance   
    '''

    def open_new_ticket_button(self):
        open_new_ticket_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Open new ticket')]")
        open_new_ticket_button.click()
        Logging().reportDebugStep(self, "The open ticket button was clicked")
        return CaServiceDesk()

    ''' 
        Returns the subject id  
    '''

    def get_subject_id_text(self):
        subject_text = super().wait_load_element_present("//div[@class='subtitle-pandats'][1]")
        new_sub = re.sub('Subject: ', "", subject_text.text)
        Logging().reportDebugStep(self, "The subject text was received: " + new_sub)
        return new_sub

    ''' 
         Returns the category tittle   
    '''

    def get_category_tittle(self):
        category_tittle = super().wait_load_element_present("//div[@class='description-pandats'][1]")
        new_sub = re.sub('Category: ', "", category_tittle.text)
        Logging().reportDebugStep(self, "The category text was received: " + new_sub)
        return new_sub

    ''' 
        Returns the ticket status of the ticket   
    '''

    def get_ticket_status(self):
        status_text = super().wait_load_element_present("//td[@class='td-20-pandats'][2]")
        Logging().reportDebugStep(self, "The ticket status text was received: " + status_text.text)
        return status_text.text

    ''' 
       Returns the ca id of the ticket 
    '''

    def get_ca_id(self):
        ca_id = super().wait_load_element_present("//td[@class='td-20-pandats']//div[1]")
        new_ca_id = re.sub('#', "", ca_id.text)
        Logging().reportDebugStep(self, "The ca id text was received: " + new_ca_id)
        return new_ca_id
