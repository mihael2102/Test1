from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class HelpDeskCreateTicketPageUI(CRMBasePage):

    def click_create_ticket_btn(self):
        sleep(0.1)
        create_ticket_btn = super().wait_element_to_be_clickable("//button[@title='Create new']")
        create_ticket_btn.click()
        Logging().reportDebugStep(self, "Click 'Create Ticket' button")
        return HelpDeskCreateTicketPageUI(self.driver)

    def set_title(self, tittle):
        sleep(0.1)
        tittle_field = super().wait_visible_of_element("//input[@id='subject']")
        tittle_field.clear()
        tittle_field.send_keys(tittle)
        Logging().reportDebugStep(self, "Tittle was set: " + tittle)
        return HelpDeskCreateTicketPageUI(self.driver)

    def select_assigned_to(self, assigned_to):
        sleep(0.1)
        item = super().wait_load_element("//nice-select[@id='assigned_id']//span[text()='%s']" % assigned_to)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Assigned to was set: " + assigned_to)
        return HelpDeskCreateTicketPageUI(self.driver)

    def select_priority(self, priority):
        sleep(0.1)
        item = super().wait_load_element(
            "//help-desk-edit//span[text()=' Priority ']//following-sibling::ul//span[text()='%s']" % priority)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Priority was set: " + priority)
        return HelpDeskCreateTicketPageUI(self.driver)

    def select_status(self, status):
        sleep(0.1)
        item = super().wait_load_element("//nice-select[@id='ticket_statuses']//span[text()='%s']" % status)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Status was set: " + status)
        return HelpDeskCreateTicketPageUI(self.driver)

    def select_category(self, category):
        sleep(0.1)
        item = super().wait_load_element("//nice-select[@id='ticket_types']//span[text()='%s']" % category)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Category was set: " + category)
        return HelpDeskCreateTicketPageUI(self.driver)

    def select_related_to(self, related_to):
        sleep(0.1)
        related_to_field = super().wait_load_element("//input[@id='parentName']")
        related_to_field.click()
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        client = super().wait_load_element("(//span[@class='td-link' and contains(text(),'%s')])[1]" % related_to)
        self.driver.execute_script("arguments[0].click();", client)
        Logging().reportDebugStep(self, "Related to set: " + related_to)
        return HelpDeskCreateTicketPageUI(self.driver)

    def select_ticket_source(self, ticket_source):
        sleep(0.1)
        item = super().wait_load_element(
            "//help-desk-edit//span[text()=' Ticket source ']//following-sibling::ul//span[text()='%s']"
            % ticket_source)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Ticket source was set: " + ticket_source)
        return HelpDeskCreateTicketPageUI(self.driver)

    def set_description(self, description):
        description_field = super().wait_load_element("//input[@id='description']")
        description_field.clear()
        description_field.send_keys(description)
        Logging().reportDebugStep(self, "Description was set: " + description)
        return HelpDeskCreateTicketPageUI(self.driver)

    def click_save_button(self):
        sleep(0.1)
        save_button = super().wait_element_to_be_clickable("//span[text()='Create ticket']")
        save_button.click()
        Logging().reportDebugStep(self, "Save button clicked")
        return HelpDeskCreateTicketPageUI(self.driver)
