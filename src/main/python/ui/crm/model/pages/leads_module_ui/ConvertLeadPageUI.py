from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class ConvertLeadPageUI(CRMBasePage):

    def convert_lead(self, first_name=None, last_name=None, email=None, phone=None, day=None, month=None, year=None,
                     citizenship=None, address=None, postal_code=None, city=None, country=None, password=None,
                     currency=None, referral=None, brand=None, source_name=None):
        if first_name:
            self.set_text_field(field1, first_name)
        if last_name:
            self.set_text_field(field2, last_name)
        if email:
            self.set_text_field(field3, email)
        if phone:
            self.set_text_field(field4, phone)
        if day and month and year:
            self.set_birth_day(day, month, year)
        if citizenship:
            self.select_pick_list_item(list1, citizenship)
        if ui_language:
            self.select_pick_list_item(list2, ui_language)
        if address:
            self.set_text_field(field5, address)
        if postal_code:
            self.set_text_field(field6, postal_code)
        if city:
            self.set_text_field(field7, city)
        if country:
            self.select_pick_list_item(list3, country)
        if password:
            self.set_text_field(field9, password)
        if currency:
            self.select_pick_list_item(list4, currency)
        if referral:
            self.set_text_field(field10, referral)
        if brand:
            self.select_pick_list_item(list5, brand)
        if source_name:
            self.set_text_field(field11, source_name)
        sleep(1)
        self.click_submit()

    def click_convert_lead_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Convert lead' button")
        btn = super().wait_element_to_be_clickable("//button[@class='btn convert-lead-button']")
        self.driver.execute_script("arguments[0].click();", btn)
        sleep(1)
        self.wait_loading_to_finish_new_ui(5)
        return ConvertLeadPageUI(self.driver)

    def select_pick_list_item(self, pick_list, item):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select " + pick_list + ": " + item)
        title = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[text()='%s']" % (pick_list, item))
        self.driver.execute_script("arguments[0].click();", title)
        return ConvertLeadPageUI(self.driver)

    def set_text_field(self, field, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set " + field + ": " + text)
        input_field = super().wait_load_element(
            "//div[contains(label,'%s')]//following-sibling::mat-form-field//input" % field)
        input_field.clear()
        input_field.send_keys(text)
        return ConvertLeadPageUI(self.driver)

    def set_birth_day(self, day, month, year):
        date_field = super().wait_load_element(
            "//input[@placeholder='Choose date of birth']")
        self.driver.execute_script("arguments[0].click();", date_field)
        current_date_btn = super().wait_load_element(
            "(//span[@class='mat-button-wrapper' and contains(text(),'2020')])[1]")
        current_date_btn.click()
        prev_btn = super().wait_load_element(
                                "(//button[@class='mat-calendar-previous-button mat-icon-button mat-button-base'])[1]")
        prev_btn.click()
        sleep(0.5)
        prev_btn.click()
        select_year = super().wait_load_element("//div[contains(text(),'%s')]" % year)
        select_year.click()
        select_month = super().wait_load_element("//div[contains(text(),'%s')]" % month)
        select_month.click()
        select_day = super().wait_load_element("(//div[contains(text(),'%s')])[1]" % day)
        select_day.click()
        set_btn = super().wait_load_element("(//span[text()='Set'])[1]")
        set_btn.click()
        Logging().reportDebugStep(self, "The birthday was set")
        return ConvertLeadPageUI(self.driver)

    def click_create_lead_btn(self):
        sleep(0.1)
        save_button = super().wait_element_to_be_clickable("//button/span[text()=' Create lead ']")
        save_button.click()
        Logging().reportDebugStep(self, "Create lead button clicked")
        return ConvertLeadPageUI(self.driver)
