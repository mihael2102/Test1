from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class ClientEditPageUI(CRMBasePage):

    def edit_client(self, field1=None, fname=None, field2=None, lname=None, day=None, month=None, year=None,
                    field3=None, c_source=None, list1=None, citizenship=None, list2=None, country=None, field4=None,
                    city=None, field5=None, address=None, field6=None, p_code=None, field7=None, phone=None, list3=None,
                    language=None, list4=None, currency=None, field8=None, referral=None, button=None):
        self.click_edit_client_btn()
        if field1 and fname:
            self.set_text(field1, fname)
        if field2 and lname:
            self.set_text(field2, lname)
        if day and month and year:
            self.set_birth_day(day, month, year)
        if field3 and c_source:
            self.set_text(field3, c_source)
        if list1 and citizenship:
            self.select_from_list(list1, citizenship)
        if list2 and country:
            self.select_from_list(list2, country)
        if field4 and city:
            self.set_text(field4, city)
        if field5 and address:
            self.set_text(field5, address)
        if field6 and p_code:
            self.set_text(field6, p_code)
        if field7 and phone:
            self.set_text(field7, phone)
        if list3 and language:
            self.select_from_list(list3, language)
        if list4 and currency:
            self.select_from_list(list4, currency)
        if field8 and referral:
            self.set_text(field8, referral)
        self.click_save_client_btn(button)

    def click_edit_client_btn(self):
        GlobalDetailsPageUI(self.driver) \
            .click_edit_btn()
        Logging().reportDebugStep(self, "'Edit Client' button was clicked")
        return ClientEditPageUI(self.driver)

    def select_from_list(self, pick_list, item):
        GlobalPopupPageUI(self.driver) \
            .select_pick_list_item(pick_list, item)
        return ClientEditPageUI(self.driver)

    def set_text(self, field, text):
        GlobalPopupPageUI(self.driver) \
            .set_text_field(field, text)
        return ClientEditPageUI(self.driver)

    def set_birth_day(self, day, month, year):
        GlobalPopupPageUI(self.driver) \
            .set_date(day, month, year)
        return ClientEditPageUI(self.driver)

    def click_save_client_btn(self, button):
        GlobalPopupPageUI(self.driver) \
            .click_final_btn(button)
        return ClientEditPageUI(self.driver)
