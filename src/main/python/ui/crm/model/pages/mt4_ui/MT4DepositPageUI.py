from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MT4DepositPageUI(CRMBasePage):

    def mt4_deposit_ui(self, list1=None, p_method=None, list2=None, status=None, list3=None, t_account=None,
                       field1=None, amount=None, field2=None, comment=None, list4=None, cleared_by=None,
                       final_btn=None):
        if p_method:
            self.select_pick_list_item(list1, p_method)
        if status:
            self.select_pick_list_item(list2, status)
        if t_account:
            self.select_pick_list_item(list3, t_account)
        if amount:
            self.set_text_field(field1, amount)
        if comment:
            self.set_text_field(field2, comment)
        if cleared_by:
            self.select_pick_list_item(list4, cleared_by)
        sleep(1)
        self.click_deposit(final_btn)

    def select_pick_list_item(self, pick_list, item):
        GlobalPopupPageUI(self.driver)\
            .select_pick_list_item(pick_list, item)
        return MT4DepositPageUI(self.driver)

    def set_text_field(self, field, text):
        GlobalPopupPageUI(self.driver)\
            .set_text_field(field, text)
        return MT4DepositPageUI(self.driver)

    def click_deposit(self, final_btn):
        GlobalPopupPageUI(self.driver)\
            .click_final_btn(final_btn)
        return MT4DepositPageUI(self.driver)
