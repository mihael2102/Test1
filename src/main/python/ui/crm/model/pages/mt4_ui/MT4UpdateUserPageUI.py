from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MT4UpdateUserPageUI(CRMBasePage):

    def mt_update_ta_ui(self, list1=None, ta=None, list2=None, server=None, list3=None, currency=None, list4=None,
                        group_number=None, list5=None, leverage=None, box1=None, final_btn=None):
        if list1 and ta:
            self.select_pick_list_item(list1, ta)
        if list2 and server:
            self.select_pick_list_item(list2, server)
        if list3 and currency:
            self.select_pick_list_item(list3, currency)
        if list4 and group_number:
            try:
                self.select_pick_list_item_by_number(list4, group_number)
            except(TimeoutException, NoSuchElementException):
                Logging().reportDebugStep(self, "No option select group")
        if list5 and leverage:
            try:
                self.select_pick_list_item(list5, leverage)
            except(TimeoutException, NoSuchElementException):
                Logging().reportDebugStep(self, "No option select leverage")
        if box1:
            self.select_check_box(box1)
        sleep(1)
        self.click_create(final_btn)

    def select_pick_list_item(self, pick_list, item):
        GlobalPopupPageUI(self.driver) \
            .select_pick_list_item(pick_list, item)
        return MT4UpdateUserPageUI(self.driver)

    def select_pick_list_item_by_number(self, pick_list, number):
        GlobalPopupPageUI(self.driver) \
            .select_pick_list_item_by_number(pick_list, number)
        return MT4UpdateUserPageUI(self.driver)

    def select_check_box(self, title):
        GlobalPopupPageUI(self.driver) \
            .select_check_box(title)
        return MT4UpdateUserPageUI(self.driver)

    def click_create(self, final_btn):
        GlobalPopupPageUI(self.driver) \
            .click_final_btn(final_btn)
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        return MT4UpdateUserPageUI(self.driver)
