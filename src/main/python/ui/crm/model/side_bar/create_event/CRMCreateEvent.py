from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage


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

    def set_event_status(self, status):
        event_element = super().wait_element_to_be_clickable("//select[@name='event_status']")
        select_status = Select(event_element)
        select_status.select_by_visible_text(status)
        return CRMCreateEvent()

    def set_event_type(self, type):
        type_element = self.driver.find_element(By.XPATH, "//select[@name='event_type']")
        select = Select(type_element)
        select.select_by_visible_text(type)
        return CRMCreateEvent()

    def set_duration(self, duration):
        duration_element = self.driver.find_element(By.XPATH, "//select[@name='event_duration']")
        select = Select(duration_element)
        select.select_by_visible_text(duration)
        return CRMCreateEvent()

    def set_time(self, time):
        time_element = self.driver.find_element(By.XPATH, "//input[@id='event_start_time']")
        time_element.clear()
        time_element.send_keys(time)
        return CRMCreateEvent()

    def set_date(self, date):
        date_element = self.driver.find_element(By.XPATH, "//input[@id='event_start_date")
        date_element.clear()
        date_element.send_keys(date)
        return CRMCreateEvent()

    def set_assign_to(self, assign_to):
        assign_to_element = self.driver.find_element(By.XPATH, "//select[@id='tks_assigned_user_id']")
        select = Select(assign_to_element)
        select.select_by_visible_text(assign_to)
        return CRMCreateEvent()

    def set_priority(self, priority):
        priority_element = self.driver.find_element(By.XPATH, "//select[@id='priority']")
        select = Select(priority_element)
        select.select_by_visible_text(priority)
        return CRMCreateEvent()

    def set_subject(self):
        return CRMCreateEvent()

    def set_description(self, comments):
        description_element = self.driver.find_element(By.XPATH, "//select[@id='priority']")
        description_element.clear()
        description_element.send_keys(comments)
        pass
