from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MT4CreditOutPageUI(CRMBasePage):

    def mt4_credit_out_ui(self, list1=None, t_account=None, field1=None, amount=None, field2=None, granted_by=None,
                          field3=None, comment=None):
        if t_account:
            self.select_pick_list_item(list1, t_account)
        if amount:
            self.set_text_field(field1, amount)
        if granted_by:
            self.set_text_field(field2, granted_by)
        if comment:
            self.set_text_field(field3, comment)
        sleep(1)
        self.click_credit_out()

    def select_pick_list_item(self, pick_list, item):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select " + pick_list + ": " + item)
        title = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[contains(text(),'%s')]" % (pick_list, item))
        self.driver.execute_script("arguments[0].click();", title)
        return MT4CreditOutPageUI(self.driver)

    def set_text_field(self, field, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set " + field + ": " + text)
        input_field = super().wait_load_element(
            "//div[contains(label,'%s')]//following-sibling::mat-form-field//input" % field)
        input_field.clear()
        input_field.send_keys(text)
        return MT4CreditOutPageUI(self.driver)

    def click_credit_out(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Deposit' button")
        deposit_btn = super().wait_element_to_be_clickable("//button[span=' Credit out ']")
        self.driver.execute_script("arguments[0].click();", deposit_btn)
        sleep(1)
        self.wait_loading_to_finish_new_ui(8)
        return MT4CreditOutPageUI(self.driver)
