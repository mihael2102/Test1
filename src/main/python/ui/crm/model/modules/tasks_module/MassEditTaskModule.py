from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MassEditTaskModule(CRMBasePage):
    # def __init__(self):
    #     super().__init__()

    def perform_mass_edit(self, status, type, duration):
        self.set_checkbox()
        self.set_event_status(status)
        self.set_event_type(type)
        # self.set_time(date, time)
        self.set_duration(duration)
        # self.set_priority(priority)
        # self.set_assign_to(assign_to)
        # self.set_description(comments)
        self.click_save()
        return MassEditTaskModule()

    def set_event_status(self, status):
        sleep(1)
        event_element = super().wait_load_element("//select[@id='eventstatus']")
        select_status = Select(event_element)
        select_status.select_by_visible_text(status)
        Logging().reportDebugStep(self, "The event status is set " + status)
        return MassEditTaskModule()

    def set_event_type(self, type):
        type_element = self.driver.find_element(By.XPATH, "//select[@id='activitytype']")
        select = Select(type_element)
        select.select_by_visible_text(type)
        Logging().reportDebugStep(self, "The event type is set " + type)
        return MassEditTaskModule()

    def set_duration(self, duration):
        duration_element = self.driver.find_element(By.XPATH, "//select[@id='duration_minutes']")
        select = Select(duration_element)
        select.select_by_visible_text(duration)
        Logging().reportDebugStep(self, "The duration  is set " + duration)
        return MassEditTaskModule()

    def set_priority(self, priority):
        priority_element = super().wait_element_to_be_clickable("//select[@id='priority']")
        select = Select(priority_element)
        select.select_by_visible_text(priority)
        Logging().reportDebugStep(self, "The priority is set " + priority)
        return MassEditTaskModule()

    def set_time(self, date, time):
        time_element = self.driver.find_element(By.XPATH, "//input[@id='date_time_start']")
        time_element.clear()
        time_element.send_keys(date + " " + time)
        Logging().reportDebugStep(self, "The date  is set " + date)
        Logging().reportDebugStep(self, "The time  is set " + time)
        return MassEditTaskModule()

    def set_assign_to(self, assign_to):
        assign_to_element = self.driver.find_element(By.XPATH, "//select[@id='smownerid']")
        select = Select(assign_to_element)
        select.select_by_visible_text(assign_to)
        Logging().reportDebugStep(self, "The assign to is set " + assign_to)
        return MassEditTaskModule()

    def set_description(self, comments):
        description_element = self.driver.find_element(By.XPATH, "//textarea[@id='description']")
        description_element.clear()
        description_element.send_keys(comments)
        Logging().reportDebugStep(self, "The comments is set " + comments)
        return MassEditTaskModule()

    def click_save(self):
        save_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        save_button.click()
        Logging().reportDebugStep(self, "Click the 'save' button ")
        return MassEditTaskModule()

    def set_checkbox(self):
        status_check_box = super().wait_element_to_be_clickable(
            "//label[contains(text(),'Status')]//preceding-sibling::span//input")
        status_check_box.click()

        event_type_check_box = self.driver.find_element(By.XPATH,
                                                        "//label[contains(text(),'Event Type')]//preceding-sibling::span//input")
        event_type_check_box.click()

        time_date_check_box = self.driver.find_element(By.XPATH,
                                                       "//label[contains(text(),'Time/Date')]//preceding-sibling::span//input")
        time_date_check_box.click()

        duration_check_box = self.driver.find_element(By.XPATH,
                                                      "//label[contains(text(),'Duration')]//preceding-sibling::span//input")
        duration_check_box.click()

        priority_check_box = self.driver.find_element(By.XPATH,
                                                      "//label[contains(text(),'Priority')]//preceding-sibling::span//input")
        priority_check_box.click()

        assign_to_check_box = self.driver.find_element(By.XPATH,
                                                       "//label[contains(text(),'Assign to')]//preceding-sibling::span//input")
        assign_to_check_box.click()

        comments_to_check_box = self.driver.find_element(By.XPATH,
                                                         "//label[contains(text(),'Comments')]//preceding-sibling::span//input")
        comments_to_check_box.click()

        return MassEditTaskModule()
