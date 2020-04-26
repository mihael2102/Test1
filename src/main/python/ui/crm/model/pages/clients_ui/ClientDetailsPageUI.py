import re
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from selenium.webdriver.support.select import Select
from src.main.python.utils.logs.Loging import Logging


class ClientDetailsPageUI(CRMBasePage):

    def get_text_from_field(self, field):
        sleep(0.1)
        try:
            try:
                data = super().wait_load_element(
                    "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-txt-wrapper')]" % field,
                    timeout=10).text
            except(NoSuchElementException, TimeoutException):
                Logging().reportDebugStep(self, "Field " + field + " is not editable")
                data = super().wait_load_element(
                    "//div[label='%s']//following-sibling::div//div[@class]" % field).text
            Logging().reportDebugStep(self, "Get data from field " + field + ": " + data)
            return data
        except:
            Logging().reportDebugStep(self, "Field " + field + " does not exist")
            return False

    """ TAB functionality """
    def open_tab(self, title):
        GlobalDetailsPageUI(self.driver)\
            .open_tab(title)
        return ClientDetailsPageUI(self.driver)

    """ Get last record number from table (string) """
    def get_last_record_number(self):
        records = GlobalModulePageUI(self.driver)\
            .get_last_record_number()
        return records

    """ Get data from table by column and row """
    def get_data_cell_table(self, column, row):
        data = GlobalModulePageUI(self.driver)\
            .get_data_from_list_view_ui(column, row)
        return data

    def get_data_from_info_tag(self, tag_title):
        sleep(0.1)
        tag = super().wait_load_element(
            "(//div[contains(text(),'%s')]//following-sibling::div[contains(@class,'info-tags')])[1]" % tag_title).text
        Logging().reportDebugStep(self, "Get data from tag '" + tag_title + "': " + tag)
        return tag

    def open_mt4_module_newui(self, module):
        try:
            sleep(0.2)
            module_item = super().wait_load_element("//div[text()=' %s ']" % module)
            self.driver.execute_script("arguments[0].click();", module_item)
            Logging().reportDebugStep(self, module + " module is opened")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Module does not exist (NOT RUNNED)")

    """
        Edit field via pencil icon
    """

    def edit_list_via_pencil(self, field, item):
        GlobalDetailsPageUI(self.driver)\
            .click_pencil_icon_in_field(field) \
            .select_item_list_pencil_field(field, item) \
            .click_confirm_btn_pencil_field(field)
        return ClientDetailsPageUI(self.driver)

    def refresh_client_page(self):
        self.refresh_page()
        return ClientDetailsPageUI(self.driver)

    def click_edit_btn(self):
        GlobalDetailsPageUI(self.driver)\
            .click_edit_btn()
        return ClientDetailsPageUI(self.driver)
