from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class LeadsDetailsPageUI(CRMBasePage):

    def get_text_from_field(self, field):
        data = GlobalDetailsPageUI(self.driver)\
            .get_text_from_field(field, timeout=55)
        return data

    def open_tab(self, title):
        GlobalDetailsPageUI(self.driver)\
            .open_tab(title)
        return LeadsDetailsPageUI(self.driver)

    def edit_text_field_via_pencil_icon(self, field, text):
        GlobalDetailsPageUI(self.driver)\
            .click_pencil_icon_in_field(field) \
            .set_text_pencil_field(field, text) \
            .click_confirm_btn_pencil_field(field)
        return LeadsDetailsPageUI(self.driver)

    def get_data_from_field_click_to_view(self, field):
        data = GlobalDetailsPageUI(self.driver) \
            .click_to_view_btn(field) \
            .get_text_from_field(field)
        return data
