from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MT4CreateTAPageUI(CRMBasePage):

    def mt4_create_ta_ui(self, list1=None, server=None, list2=None, currency=None, list3=None, group_number=None,
                         list4=None, leverage=None, final_btn=None):
        if server:
            self.select_pick_list_item(list1, server)
        if currency:
            self.select_pick_list_item(list2, currency)
        if group_number:
            try:
                self.select_pick_list_item_by_number(list3, group_number)
            except(TimeoutException, NoSuchElementException):
                Logging().reportDebugStep(self, "No option select group")
        if leverage:
            try:
                self.select_pick_list_item(list4, leverage)
            except(TimeoutException, NoSuchElementException):
                Logging().reportDebugStep(self, "No option select leverage")
        sleep(1)
        self.click_create(final_btn)

    def select_pick_list_item(self, pick_list, item):
        GlobalPopupPageUI(self.driver)\
            .select_pick_list_item(pick_list, item)
        return MT4CreateTAPageUI(self.driver)

    def select_pick_list_item_by_number(self, pick_list, number):
        GlobalPopupPageUI(self.driver) \
            .select_pick_list_item_by_number(pick_list, number)
        return MT4CreateTAPageUI(self.driver)

    def click_create(self, final_btn):
        GlobalPopupPageUI(self.driver)\
            .click_final_btn(final_btn)
        GlobalModulePageUI(self.driver)\
            .verify_success_message() \
            .click_ok()
        return MT4CreateTAPageUI(self.driver)
