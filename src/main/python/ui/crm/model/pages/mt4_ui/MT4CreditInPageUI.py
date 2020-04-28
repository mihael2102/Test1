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


class MT4CreditInPageUI(CRMBasePage):

    def mt4_credit_in_ui(self, list1=None, t_account=None, field1=None, amount=None, day=None, month=None, year=None,
                         field2=None, granted_by=None, field3=None, comment=None, final_btn=None):
        if t_account:
            self.select_pick_list_item(list1, t_account)
        if amount:
            self.set_text_field(field1, amount)
        if day and month and year:
            self.set_expire_date(day, month, year)
        if granted_by:
            self.set_text_field(field2, granted_by)
        if comment:
            self.set_text_field(field3, comment)
        sleep(1)
        self.click_credit_in(final_btn)

    def select_pick_list_item(self, pick_list, item):
        GlobalPopupPageUI(self.driver)\
            .select_pick_list_item(pick_list, item)
        return MT4CreditInPageUI(self.driver)

    def set_text_field(self, field, text):
        GlobalPopupPageUI(self.driver) \
            .set_text_field(field, text)
        return MT4CreditInPageUI(self.driver)

    def set_expire_date(self, day, month, year):
        date_field = super().wait_load_element(
            "//input[@placeholder='Select expire date']")
        self.driver.execute_script("arguments[0].click();", date_field)
        current_date_btn = super().wait_load_element(
            "(//span[@class='mat-button-wrapper' and contains(text(),'2020')])[1]")
        current_date_btn.click()
        select_year = super().wait_load_element("//div[contains(text(),'%s')]" % year)
        select_year.click()
        select_month = super().wait_load_element("//div[contains(text(),'%s')]" % month)
        select_month.click()
        select_day = super().wait_load_element("(//div[contains(text(),'%s')])[1]" % day)
        select_day.click()
        set_btn = super().wait_load_element("(//span[text()='Set'])[1]")
        set_btn.click()
        Logging().reportDebugStep(self, "The Expire date was set")
        return MT4CreditInPageUI(self.driver)

    def click_credit_in(self, final_btn):
        GlobalPopupPageUI(self.driver) \
            .click_final_btn(final_btn)
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        return MT4CreditInPageUI(self.driver)
