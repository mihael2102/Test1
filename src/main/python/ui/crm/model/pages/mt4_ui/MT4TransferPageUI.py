from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MT4TransferPageUI(CRMBasePage):

    def mt4_transfer_ui(self, list1=None, source=None, list2=None, destination=None, field1=None, amount=None,
                        final_btn=None):
        if source:
            self.select_pick_list_item(list1, source)
        if destination:
            self.select_pick_list_item(list2, destination)
        if amount:
            self.set_text_field(field1, amount)
        sleep(1)
        self.click_transfer(final_btn)
        return MT4TransferPageUI(self.driver)

    def select_pick_list_item(self, pick_list, item):
        GlobalPopupPageUI(self.driver) \
            .select_pick_list_item(pick_list, item)
        return MT4TransferPageUI(self.driver)

    def set_text_field(self, field, text):
        GlobalPopupPageUI(self.driver) \
            .set_text_field(field, text)
        return MT4TransferPageUI(self.driver)

    def click_transfer(self, final_btn):
        GlobalPopupPageUI(self.driver) \
            .click_final_btn(final_btn)
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        return MT4TransferPageUI(self.driver)
