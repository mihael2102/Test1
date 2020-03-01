from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MT4TransferPageUI(CRMBasePage):

    def mt4_transfer_ui(self, list1=None, source=None, list2=None, destination=None, field1=None, amount=None):
        if source:
            self.select_pick_list_item(list1, source)
        if destination:
            self.select_pick_list_item(list2, destination)
        if amount:
            self.set_text_field(field1, amount)
        sleep(1)
        self.click_transfer()

    def select_pick_list_item(self, pick_list, item):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select " + pick_list + ": " + item)
        title = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[contains(text(),'%s')]" % (pick_list, item))
        self.driver.execute_script("arguments[0].click();", title)
        return MT4TransferPageUI(self.driver)

    def set_text_field(self, field, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set " + field + ": " + text)
        input_field = super().wait_load_element(
            "//div[contains(label,'%s')]//following-sibling::mat-form-field//input" % field)
        input_field.clear()
        input_field.send_keys(text)
        return MT4TransferPageUI(self.driver)

    def click_transfer(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Deposit' button")
        deposit_btn = super().wait_element_to_be_clickable("//button[span=' Transfer ']")
        self.driver.execute_script("arguments[0].click();", deposit_btn)
        sleep(1)
        self.wait_loading_to_finish_new_ui(8)
        return MT4TransferPageUI(self.driver)
