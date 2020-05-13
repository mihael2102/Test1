from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.client_modules.mass_sms.SendSMSClientsModule import SendSMSClientsModule
from src.main.python.ui.crm.model.modules.client_modules.send_email.SendEmailClientsModule import SendEmailClientsModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.modules.client_modules.mass_assign.MassAssignClientsModule import \
    MassAssignClientsModule
from src.main.python.ui.crm.model.modules.client_modules.mass_edit.MassEditClientsModule import MassEditClientsModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
#import allure
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class GlobalPopupPageUI(CRMBasePage):

    def select_pick_list_item(self, pick_list, item):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select " + pick_list + ": " + item)
        title = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[contains(text(),'%s')]" % (pick_list, item))
        self.driver.execute_script("arguments[0].click();", title)
        return GlobalPopupPageUI(self.driver)

    def select_pick_list_item_by_number(self, pick_list, number):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select " + pick_list + " by index: " + number)
        title = super().wait_load_element(
            "(//span[text()=' %s ']//following-sibling::ul//span)[%s]" % (pick_list, number))
        self.driver.execute_script("arguments[0].click();", title)
        return GlobalPopupPageUI(self.driver)

    def get_item_from_list_by_number(self, pick_list, number):
        sleep(0.1)
        Logging().reportDebugStep(self, "Get data from pick-list: " + pick_list)
        item = super().wait_load_element(
            "(//span[text()=' %s ']//following-sibling::ul//span)[%s]" % (pick_list, number), timeout=35)\
            .get_attribute("innerText")
        Logging().reportDebugStep(self, "Get data from pick-list(" + pick_list + ") by index(" + number + "): " + item)
        return item

    def set_text_field(self, field, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set " + field + ": " + text)
        input_field = super().wait_load_element(
            "//div[contains(label,'%s')]//following-sibling::mat-form-field//input" % field)
        try:
            sleep(0.1)
            input_field.clear()
            input_field.send_keys(text)
        except:
            Logging().reportDebugStep(self, "The " + field + " field is read only")
        return GlobalPopupPageUI(self.driver)

    def select_check_box(self, title):
        sleep(0.1)
        Logging().reportDebugStep(self, "Mark check-box: " + title)
        try:
            check_box = super().wait_load_element(
                "//mat-sidenav//span[text()=' %s ']//preceding-sibling::mat-checkbox[not(contains(@class,'checked'))]"
                % title)
            check_box.click()
        except:
            Logging().reportDebugStep(self, "Check-box: " + title + " already checked")
        return GlobalPopupPageUI(self.driver)

    def set_date(self, day, month, year):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set birthday (day: " + day + ", month: " + month + ", year: " + year + ")")
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
        return GlobalPopupPageUI(self.driver)

    def is_button_active(self, button):
        sleep(0.1)
        flag = super().wait_element_to_be_clickable("//button[span=' %s ']" % button).get_property("disabled")
        return not flag

    def click_final_btn(self, button):
        sleep(0.1)
        flag = self.is_button_active(button)
        if flag:
            Logging().reportDebugStep(self, "Click '" + button + "' button")
            btn = super().wait_element_to_be_clickable("//mat-sidenav//button[span=' %s ']" % button)
            self.driver.execute_script("arguments[0].click();", btn)
            sleep(1)
            self.wait_loading_to_finish_new_ui(55)
        else:
            Logging().reportDebugStep(self, button + " button is inactive")
        return GlobalPopupPageUI(self.driver)

    def click_cancel_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Cancel' button")
        btn = super().wait_element_to_be_clickable("//mat-sidenav//button[span=' Cancel ']")
        self.driver.execute_script("arguments[0].click();", btn)
        return GlobalPopupPageUI(self.driver)
