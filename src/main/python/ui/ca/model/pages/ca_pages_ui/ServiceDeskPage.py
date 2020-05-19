from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.ca.model.pages.ca_global_ui.GlobalClientAreaPage import GlobalClientAreaPage
from time import sleep
import re
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.ca.model.constants.client_area.ServiceDeskConstants import ServiceDeskConstants


class ServiceDeskPage(CRMBasePage):

    def create_ticket(self, start_button=None, field1=None, subject=None, list1=None, category=None, field2=None,
                      description=None, final_button=None):
        self.click_button(start_button)
        if field1 and subject:
            self.set_text_field(field1, subject)
        if list1 and category:
            self.select_item_from_list(list1, category)
        if field2 and description:
            self.set_text_field(field2, description)
        self.click_button(final_button)
        return ServiceDeskPage(self.driver)

    def click_button(self, button):
        GlobalClientAreaPage(self.driver)\
            .click_btn(button)
        return ServiceDeskPage(self.driver)

    def select_item_from_list(self, pick_list, item):
        GlobalClientAreaPage(self.driver) \
            .select_item_from_list(pick_list, item)
        return ServiceDeskPage(self.driver)

    def set_text_field(self, field, text):
        GlobalClientAreaPage(self.driver) \
            .set_text_field(field, text)
        return ServiceDeskPage(self.driver)

    def get_ca_ticket_id(self):
        sleep(0.1)
        ca_id = super().wait_load_element("//td[@class='td-20-pandats']//div[1]").text
        ca_id = re.sub('#', "", ca_id)
        Logging().reportDebugStep(self, "Get Ticket id from CA: " + ca_id)
        return ca_id

    def get_ticket_data(self, row):
        sleep(0.1)
        data = super().wait_load_element("//tbody/tr[%s]" % row).get_attribute("innerText")
        Logging().reportDebugStep(self, "Get Subject from CA: " + data)
        return data

    def open_tab(self, title):
        sleep(0.1)
        try:
            Logging().reportDebugStep(self, "Open tab: " + title)
            tab = super().wait_load_element("//span[not(@class='active-pandats') and text()=' %s ']" % title)
            tab.click()
        except:
            Logging().reportDebugStep(self, "Tab '" + title + "' already opened")
        return ServiceDeskPage(self.driver)
