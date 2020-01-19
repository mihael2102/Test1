from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MT4CreateTAPageUI(CRMBasePage):

    def mt4_create_ta_ui(self, list1=None, server=None, list2=None, currency=None, list3=None, group=None, list4=None,
                         leverage=None):
        if server:
            self.select_pick_list_item(list1, server)
        if currency:
            self.select_pick_list_item(list2, currency)
        if group:
            try:
                self.select_pick_list_item(list3, group)
            except(TimeoutException, NoSuchElementException):
                Logging().reportDebugStep(self, "No option select group")
        if leverage:
            try:
                self.select_pick_list_item(list4, leverage)
            except(TimeoutException, NoSuchElementException):
                Logging().reportDebugStep(self, "No option select leverage")
        sleep(1)
        self.click_create()

    def select_pick_list_item(self, pick_list, item):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select " + pick_list + ": " + item)
        title = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[contains(text(),'%s')]" % (pick_list, item))
        self.driver.execute_script("arguments[0].click();", title)
        return MT4CreateTAPageUI(self.driver)

    def click_create(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Create' button")
        convert_lead_btn = super().wait_load_element("//button[span=' Create ']")
        convert_lead_btn.click()
        sleep(1)
        self.wait_loading_to_finish_new_ui(8)
        return MT4CreateTAPageUI(self.driver)
