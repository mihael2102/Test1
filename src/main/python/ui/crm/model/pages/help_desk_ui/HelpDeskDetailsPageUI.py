from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskCreateTicketPageUI import HelpDeskCreateTicketPageUI
from src.main.python.utils.logs.Loging import Logging


class HelpDeskDetailsPageUI(CRMBasePage):

    def get_text_from_field(self, field):
        data = GlobalDetailsPageUI(self.driver)\
            .get_text_from_field(field)
        return data

    def open_tab(self, title):
        GlobalDetailsPageUI(self.driver)\
            .open_tab(title)
        return HelpDeskDetailsPageUI(self.driver)

    def click_edit_btn(self):
        GlobalDetailsPageUI(self.driver)\
            .click_edit_btn()
        return HelpDeskCreateTicketPageUI(self.driver)

    def edit_text_field_via_pencil(self, field, text):
        GlobalDetailsPageUI(self.driver)\
            .click_pencil_icon_in_field(field) \
            .set_text_pencil_field(field, text) \
            .click_confirm_btn_pencil_field(field)
        return HelpDeskDetailsPageUI(self.driver)

    def edit_list_field_via_pencil(self, field, item):
        GlobalDetailsPageUI(self.driver) \
            .click_pencil_icon_in_field(field) \
            .select_item_list_pencil_field(field, item) \
            .click_confirm_btn_pencil_field(field)
        return HelpDeskDetailsPageUI(self.driver)
