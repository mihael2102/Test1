from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from src.main.python.utils.logs.Loging import Logging


class CRMCreateEvent(CRMBasePage):
    def __init__(self):
        super().__init__()

    def create_event(self, status, type, duration, time, date, assign_to, priority, comments):
        self.set_event_status(status)
        self.set_event_type(type)
        self.set_duration(duration)
        self.set_time(time)
        self.set_date(date)
        self.set_assign_to(assign_to)
        self.set_priority(priority)
        self.set_description(comments)
        self.click_save()
        return CRMClientProfilePage()

    def set_event_status(self, status):
        event_element = super().wait_element_to_be_clickable("//select[@name='event_status']")
        select_status = Select(event_element)
        select_status.select_by_visible_text(status)
        Logging().reportDebugStep(self, "The event status is set " + status)
        return CRMCreateEvent()

    def set_event_type(self, type):
        type_element = self.driver.find_element(By.XPATH, "//select[@name='event_type']")
        select = Select(type_element)
        select.select_by_visible_text(type)
        Logging().reportDebugStep(self, "The event type is set " + type)
        return CRMCreateEvent()

    def set_duration(self, duration):
        duration_element = self.driver.find_element(By.XPATH, "//select[@name='event_duration']")
        select = Select(duration_element)
        select.select_by_visible_text(duration)
        Logging().reportDebugStep(self, "The duration  is set " + duration)
        return CRMCreateEvent()

    def set_time(self, time):
        time_element = self.driver.find_element(By.XPATH, "//input[@id='event_start_time']")
        time_element.clear()
        time_element.send_keys(time)
        time_element.send_keys(Keys.ENTER)
        Logging().reportDebugStep(self, "The time  is set " + time)
        return CRMCreateEvent()

    def set_date(self, date):
        date_element = self.driver.find_element(By.XPATH, "//input[@id='event_start_date']")
        date_element.clear()
        date_element.send_keys(date)
        date_element.send_keys(Keys.ENTER)
        Logging().reportDebugStep(self, "The date is set " + date)
        return CRMCreateEvent()

    def set_assign_to(self, assign_to):
        assign_to_element = self.driver.find_element(By.XPATH, "//select[@id='tks_assigned_user_id']")
        select = Select(assign_to_element)
        select.select_by_visible_text(assign_to)
        Logging().reportDebugStep(self, "The  assign to is set " + assign_to)
        return CRMCreateEvent()

    def set_priority(self, priority):
        priority_element = self.driver.find_element(By.XPATH, "//select[@id='priority']")
        select = Select(priority_element)
        select.select_by_visible_text(priority)
        Logging().reportDebugStep(self, "The priority is set " + priority)
        return CRMCreateEvent()

    def set_description(self, comments):
        description_element = self.driver.find_element(By.XPATH, "//textarea[@name='description']")
        description_element.clear()
        description_element.send_keys(comments)
        Logging().reportDebugStep(self, "The comments is set " + comments)
        return CRMCreateEvent()

    def click_save(self):
        save_button = self.driver.find_element(By.XPATH, "//button[@id='save_btn']")
        save_button.click()
        Logging().reportDebugStep(self, "Click the 'save' button ")
        return CRMCreateEvent()
