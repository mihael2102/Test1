import random
import re

from selenium.webdriver.common.by import By

from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage


class CaServiceDesk(BrandBasePage):
    def __init__(self):
        super().__init__()

    '''
       Open the ticket tabs 
       :return Service Desk instance  
    '''

    def open_tickets_tab(self):
        create_ticket_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Open Tickets')]")
        create_ticket_button.click()
        return CaServiceDesk()

    ''' 
        Create a new ticket
       :return Service Desk instance
    '''

    def create_new_ticket(self):
        create_ticket_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Create New Ticket')]")
        create_ticket_button.click()
        return CaServiceDesk()

    ''' 
        Set a subject in the field 
        :return Service Desk instance   
    '''

    def set_subject_field(self, subject):
        subject_field = self.driver.find_element(By.XPATH, "//input[@name='subject']")
        subject_field.clear()
        subject_field.send_keys(subject)
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
        return CaServiceDesk()

    ''' 
        Set a description  in the field 
        :return Service Desk instance   
    '''

    def set_description(self, description):
        description_field = self.driver.find_element(By.XPATH, "//textarea[@name='description']")
        description_field.clear()
        description_field.send_keys(description)
        return CaServiceDesk()

    ''' 
        Open a new ticket button 
        :return Service Desk instance   
    '''

    def open_new_ticket_button(self):
        open_new_ticket_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Open new ticket')]")
        open_new_ticket_button.click()
        return CaServiceDesk()

    ''' 
        Returns the subject id  
    '''

    def get_subject_id_text(self):
        subject_text = super().wait_load_element("//div[@class='subtitle-pandats'][1]")
        new_sub = re.sub('Subject: ', "", subject_text.text)

        return new_sub

    ''' 
         Returns the category tittle   
    '''

    def get_category_tittle(self):
        category_tittle = super().wait_load_element("//div[@class='italic-pandats'][1]")
        new_sub = re.sub('Category: ', "", category_tittle.text)

        return new_sub

    ''' 
        Returns the ticket status   
    '''

    def get_ticket_status(self):
        status_text = super().wait_load_element("//td[@class='td-20-pandats'][1]")
        return status_text.text

    def get_ca_id(self):
        ca_id = super().wait_load_element("//td[@class='td-30-pandats']//div[1]")
        new_ca_id = re.sub('#', "", ca_id.text)
        return new_ca_id
