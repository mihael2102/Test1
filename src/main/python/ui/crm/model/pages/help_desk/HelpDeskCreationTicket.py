from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class HelpDeskCreationTicket(CRMBasePage):

    def perform_create_new_ticket(self, title, related_to, assigned_to, status, priority, category, ticket_source,
                                  description, notes):
        if title:
            self.set_title(title)
        if related_to:
            self.select_related_to(related_to)
        if related_to:
            self.click_exist_client_name(related_to)
        if assigned_to:
            self.set_assigned_to(assigned_to)
        if status:
            self.select_status(status)
        if priority:
            self.set_priority(priority)
        if category:
            self.set_category(category)
        if ticket_source:
            self.set_ticket_source(ticket_source)
        if description:
            self.set_description(description)
        if notes:
            self.set_notes(notes)
        self.click_save_button()

    def set_title(self, tittle):
        tittle_field = super().wait_visible_of_element("//textarea[@name='subject']")
        tittle_field.clear()
        tittle_field.send_keys(tittle)
        Logging().reportDebugStep(self, "Tittle was set: " + tittle)
        return HelpDeskCreationTicket(self.driver)

    def select_related_to(self, related_to):
        assigned_to_field = self.driver.find_element(By.XPATH, "//td[@class='dvtCellInfo']//img")
        assigned_to_field.click()
        handle = self.driver.window_handles[1]
        self.driver.switch_to_window(handle)
        client_name_field = super().wait_visible_of_element("//input[@name='search_text']")
        client_name_field.send_keys(related_to)
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='search_field']"))
        select.select_by_visible_text("Client Name")
        search_button = self.driver.find_element(By.XPATH, "//input[@name='search']")
        search_button.click()
        Logging().reportDebugStep(self, "Related to set: " + related_to)
        return HelpDeskCreationTicket(self.driver)

    def click_exist_client_name(self, client_name):
        sleep(0.1)
        client_name_link = super().wait_load_element("//a[contains(text(),'%s')]" % client_name, timeout=55)
        client_name_link.click()
        Logging().reportDebugStep(self, "Client name was set: " + client_name)
        return HelpDeskCreationTicket(self.driver)

    def set_assigned_to(self, assigned_to):
        handle = self.driver.window_handles[0]
        self.driver.switch_to_window(handle)
        assigned_to_pick_list = Select(self.driver.find_element(By.XPATH, "//select[@name='assigned_user_id']"))
        assigned_to_pick_list.select_by_visible_text(assigned_to)
        Logging().reportDebugStep(self, "Assigned_to was set: " + assigned_to)
        return HelpDeskCreationTicket(self.driver)

    def select_status(self, status):
        assigned_to_field = Select(self.driver.find_element(By.XPATH, "//select[@name='ticket_statuses']"))
        assigned_to_field.select_by_visible_text(status)
        Logging().reportDebugStep(self, "Status was set: " + status)
        return HelpDeskCreationTicket(self.driver)

    def set_priority(self, priority):
        priority_pick_list = Select(self.driver.find_element(By.XPATH, "//select[@name='ticketpriorities']"))
        priority_pick_list.select_by_visible_text(priority)
        Logging().reportDebugStep(self, "Priority was set: " + priority)
        return HelpDeskCreationTicket(self.driver)

    def set_category(self, category):
        category_pick_list = Select(self.driver.find_element(By.XPATH, "//select[@name='ticket_types']"))
        category_pick_list.select_by_visible_text(category)
        Logging().reportDebugStep(self, "Category was set: " + category)
        return HelpDeskCreationTicket(self.driver)

    def set_ticket_source(self, ticket_source):
        ticket_source_pick_list = Select(self.driver.find_element(By.XPATH, "//select[@name='ticketsource']"))
        ticket_source_pick_list.select_by_visible_text(ticket_source)
        Logging().reportDebugStep(self, "Ticket source was set: " + ticket_source)
        return HelpDeskCreationTicket(self.driver)

    def set_description(self, description):
        description_field = self.driver.find_element(By.XPATH, "//textarea[@name='description']")
        description_field.clear()
        description_field.send_keys(description)
        Logging().reportDebugStep(self, "Description was set: " + description)
        return HelpDeskCreationTicket(self.driver)

    def set_notes(self, notes):
        assigned_to_field = self.driver.find_element(By.XPATH, "//textarea[@name='cf_1022']")
        assigned_to_field.clear()
        assigned_to_field.send_keys(notes)
        Logging().reportDebugStep(self, "Notes was set: " + notes)
        return HelpDeskCreationTicket(self.driver)

    def click_save_button(self):
        save_button = self.driver.find_element(By.XPATH, "//input[@title='Save [Alt+S]']")
        save_button.click()
        sleep(1)
        self.wait_loading_to_finish(55)
        Logging().reportDebugStep(self, "Save button was clicked")
        return HelpDeskCreationTicket(self.driver)
