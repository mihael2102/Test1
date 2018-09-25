from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
import time

class EditEventModule(CRMBasePage):
    # def __init__(self):
    #     super().__init__()

    def edit_event(self, status, type, duration, date, time, assign_to, subject, priority,
                   comments):
        self.set_event_status(status)
        self.set_event_type(type)
        self.set_time(date, time)
        self.set_duration(duration)
        self.set_priority(priority)
        self.set_assign_to(assign_to)
        self.set_subject(subject)
        self.set_description(comments)
        self.click_save()
        return EditEventModule()

    def set_event_status(self, status):
        event_element = super().wait_element_to_be_clickable("//select[@id='eventstatus']")
        select_status = Select(event_element)
        select_status.select_by_visible_text(status)
        Logging().reportDebugStep(self, "The event status was set " + status)
        return EditEventModule()

    def set_event_type(self, type):
        type_element = self.driver.find_element(By.XPATH, "//select[@id='activitytype']")
        select = Select(type_element)
        select.select_by_visible_text(type)
        Logging().reportDebugStep(self, "The event type is set " + type)
        return EditEventModule()

    def set_duration(self, duration):
        duration_element = self.driver.find_element(By.XPATH, "//select[@id='duration_minutes']")
        select = Select(duration_element)
        select.select_by_visible_text(duration)
        Logging().reportDebugStep(self, "The duration  is set " + duration)
        return EditEventModule()

    def set_priority(self, priority):
        priority_element = super().wait_element_to_be_clickable("//select[@id='priority']")
        select = Select(priority_element)
        select.select_by_visible_text(priority)
        Logging().reportDebugStep(self, "The priority is set " + priority)
        return EditEventModule()

    def set_time(self, date, time):
        time_element = self.driver.find_element(By.XPATH, "//input[@id='date_time_start']")
        time_element.clear()
        time_element.send_keys(date + " " + time)
        Logging().reportDebugStep(self, "The date  is set " + date)
        Logging().reportDebugStep(self, "The time  is set " + time)
        return EditEventModule()

    def set_assign_to(self, assign_to):
        assign_to_element = self.driver.find_element(By.XPATH, "//select[@id='smownerid']")
        select = Select(assign_to_element)
        select.select_by_visible_text(assign_to)
        Logging().reportDebugStep(self, "The assign to is set " + assign_to)
        return EditEventModule()

    # def set_account_name(self, account_name):
    #     account_name_element = self.driver.find_element(By.XPATH,
    #                                                     "//input[@class='form-control ng-pristine ng-valid ng-touched']")
    #     account_name.clear()
    #     account_name_element.send_keys(account_name)
    #     selecting_account_element = super().wait_element_to_be_clickable(
    #         "//div[@class='ngui-auto-complete']//ul//li[4]")
    #     selecting_account_element.click()
    #     Logging().reportDebugStep(self, "The account is set " + account_name)
    #     return CRMEditEventModule()

    def set_subject(self, subject):
        description_element = self.driver.find_element(By.XPATH, "//input[@id='subject']")
        description_element.clear()
        description_element.send_keys(subject)
        Logging().reportDebugStep(self, "The subject is set " + subject)
        return EditEventModule()

    def set_description(self, comments):
        description_element = self.driver.find_element(By.XPATH, "//textarea[@id='description']")
        description_element.clear()
        description_element.send_keys(comments)
        Logging().reportDebugStep(self, "The comments is set " + comments)
        return EditEventModule()

    def click_save(self):
        save_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        save_button.click()
        Logging().reportDebugStep(self, "Click the 'save' button ")
        return EditEventModule()
