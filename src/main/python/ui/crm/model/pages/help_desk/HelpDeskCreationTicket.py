from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class HelpDeskCreationTicket(CRMBasePage):

    def __init__(self) -> None:
        super().__init__()

    def perform_create_new_ticket(self, tittle, related_to, assigned_to, status, priority, category, ticket_source,
                                  description,
                                  notes):
        self.set_title(tittle)
        self.select_related_to(related_to)
        self.click_exist_client_name(related_to)
        self.set_assigned_to(assigned_to)
        self.select_status(status)
        self.set_priority(priority)
        self.set_category(category)
        self.set_ticket_source(ticket_source)
        self.set_description(description)
        self.set_notes(notes)
        self.click_save_button()

    def set_title(self, tittle):
        tittle_field = super().wait_visible_of_element("//textarea[@name='subject']")
        tittle_field.clear()
        tittle_field.send_keys(tittle)
        Logging().reportDebugStep(self, "The tittle was set: " + tittle)
        return HelpDeskCreationTicket()

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
        Logging().reportDebugStep(self, "The related_to set: " + related_to)
        return HelpDeskCreationTicket()

    def click_exist_client_name(self, client_name):
        client_name_link = super().wait_visible_of_element("//a[contains(text(),'%s')]" % client_name)
        client_name_link.click()
        Logging().reportDebugStep(self, "The client name was set: " + client_name)
        return HelpDeskCreationTicket()

    def set_assigned_to(self, assigned_to):
        handle = self.driver.window_handles[0]
        self.driver.switch_to_window(handle)
        assigned_to_pick_list = Select(self.driver.find_element(By.XPATH, "//select[@name='assigned_user_id']"))
        assigned_to_pick_list.select_by_visible_text(assigned_to)
        Logging().reportDebugStep(self, "The assigned_to was set: ")
        return HelpDeskCreationTicket()

    def select_status(self, status):
        assigned_to_field = Select(self.driver.find_element(By.XPATH, "//select[@name='ticket_statuses']"))
        assigned_to_field.select_by_visible_text(status)
        Logging().reportDebugStep(self, "The status was set: " + status)
        return HelpDeskCreationTicket()

    def set_priority(self, priority):
        priority_pick_list = Select(self.driver.find_element(By.XPATH, "//select[@name='ticketpriorities']"))
        priority_pick_list.select_by_visible_text(priority)
        Logging().reportDebugStep(self, "The priority was set: " + priority)
        return HelpDeskCreationTicket()

    def set_category(self, category):
        category_pick_list = Select(self.driver.find_element(By.XPATH, "//select[@name='ticket_types']"))
        category_pick_list.select_by_visible_text(category)
        Logging().reportDebugStep(self, "The category was set: " + category)
        return HelpDeskCreationTicket()

    def set_ticket_source(self, ticket_source):
        ticket_source_pick_list = Select(self.driver.find_element(By.XPATH, "//select[@name='ticketsource']"))
        ticket_source_pick_list.select_by_visible_text(ticket_source)
        Logging().reportDebugStep(self, "The ticket source was set: " + ticket_source)
        return HelpDeskCreationTicket()

    def set_description(self, description):
        description_field = self.driver.find_element(By.XPATH, "//textarea[@name='description']")
        description_field.clear()
        description_field.send_keys(description)
        Logging().reportDebugStep(self, "The description was set: " + description)
        return HelpDeskCreationTicket()

    def set_notes(self, notes):
        assigned_to_field = self.driver.find_element(By.XPATH, "//textarea[@name='cf_1022']")
        assigned_to_field.clear()
        assigned_to_field.send_keys(notes)
        Logging().reportDebugStep(self, "The notes was set: " + notes)
        return HelpDeskCreationTicket()

    def click_save_button(self):
        save_button = self.driver.find_element(By.XPATH, "//input[@title='Save [Alt+S]']")
        save_button.click()
        Logging().reportDebugStep(self, "The save button was clicked")
        return HelpDeskCreationTicket()
