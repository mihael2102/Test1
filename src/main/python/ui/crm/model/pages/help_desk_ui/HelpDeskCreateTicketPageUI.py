from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class HelpDeskCreateTicketPageUI(CRMBasePage):

    def create_edit_ticket(self, create_btn=None, edit_btn=None, row=None, field1=None, title=None, list1=None,
                           assigned_to=None, list2=None, priority=None, list3=None, status=None, list4=None,
                           category=None, related_to=None, list5=None, source=None, field2=None, description=None,
                           final_btn=None):
        if create_btn:
            self.click_create_ticket_btn()
        if edit_btn and row:
            self.edit_record(row)
        if field1 and title:
            self.set_text(field1,title)
        if list1 and assigned_to:
            self.select_assigned_to(assigned_to)
        if list2 and priority:
            self.select_priority(priority)
        if list3 and status:
            self.select_status(status)
        if list4 and category:
            self.select_category(category)
        if related_to:
            self.select_related_to(related_to)
        if list5 and source:
            self.select_from_list(list5, source)
        if field2 and description:
            self.set_text(field2, description)
        self.click_save_btn(final_btn)

    def click_create_ticket_btn(self):
        sleep(0.1)
        create_ticket_btn = super().wait_element_to_be_clickable("//button[@title='Create new']")
        create_ticket_btn.click()
        Logging().reportDebugStep(self, "Click 'Create Ticket' button")
        return HelpDeskCreateTicketPageUI(self.driver)

    """ Click Edit icon in table by row """
    def edit_record(self, row):
        GlobalModulePageUI(self.driver) \
            .open_actions_list(row) \
            .click_edit_icon_list_view(row)
        return HelpDeskCreateTicketPageUI(self.driver)

    def select_from_list(self, pick_list, item):
        GlobalPopupPageUI(self.driver) \
            .select_pick_list_item(pick_list, item)
        return HelpDeskCreateTicketPageUI(self.driver)

    def set_text(self, field, text):
        GlobalPopupPageUI(self.driver) \
            .set_text_field(field, text)
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
        related_to_field = super().wait_load_element("//span[text()='Related to']")
        related_to_field.click()
        sleep(1)
        field = super().wait_load_element("//span[contains(text(),' Relates To ')]//following-sibling::div//input")
        field.clear()
        field.send_keys(related_to)
        sleep(0.5)
        client = super().wait_load_element("(//help-desk-edit//span[contains(text(),'%s')])[1]" % related_to)
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

    def click_save_btn(self, button):
        sleep(0.1)
        btn = super().wait_load_element("//mat-sidenav//span[text()='%s']" % button)
        btn.click()
        Logging().reportDebugStep(self, "Click '" + button + "' button")
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        return HelpDeskCreateTicketPageUI(self.driver)

    def click_final_btn(self, button):
        GlobalPopupPageUI(self.driver) \
            .click_final_btn(button)
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        return HelpDeskCreateTicketPageUI(self.driver)
