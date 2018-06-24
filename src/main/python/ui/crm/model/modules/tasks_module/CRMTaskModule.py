from time import sleep

from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.tasks_module.CRMAddEventModule import CRMAddEventModule
from src.main.python.ui.crm.model.modules.tasks_module.CRMCalendarViewModule import CRMCalendarViewModule
from src.main.python.ui.crm.model.modules.tasks_module.CRMEditEventModule import CRMEditEventModule
from src.main.python.utils.logs.Loging import Logging


class CRMTaskModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def get_show_all_tab_text(self):
        super().wait_load_element("//ul[@id='main-tabs']//li[1]")
        tab = self.driver.find_element(By.XPATH, "//ul[@id='main-tabs']//li[1]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[1]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_show_mine_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[2]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[2]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_today_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[3]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[3]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def get_this_week_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[4]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[4]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def open_this_week_tab(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[4]")
        tab.click()
        Logging().reportDebugStep(self, "The this week tab was opened ")
        return CRMTaskModule()

    def get_history_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[5]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[5]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def open_event_module(self):
        event_button = self.driver.find_element(By.XPATH,
                                                "//button[contains(text(),'Add Event')]")
        event_button.click()
        Logging().reportDebugStep(self, "The event  module was opened ")
        return CRMAddEventModule()

    def open_calendar_view_module(self):
        calendar_view_button = self.driver.find_element(By.XPATH,
                                                        "//button[contains(text(),'Calendar View')]")
        calendar_view_button.click()
        Logging().reportDebugStep(self, "The calendar view module was opened")
        return CRMCalendarViewModule()

    def select_several_records_task_module(self):
        first_check_box = super().wait_element_to_be_clickable("//div[@class='table-grid-container']//tr[3]//td[1]")
        first_check_box.click()
        second_check_box = self.driver.find_element(By.XPATH, "//div[@class='table-grid-container']//tr[4]//td[1]")
        second_check_box.click()
        third_check_box = self.driver.find_element(By.XPATH, "//div[@class='table-grid-container']//tr[5]//td[1]")
        third_check_box.click()
        Logging().reportDebugStep(self, "The records were selected")
        return CRMTaskModule()

    def perform_mass_delete(self):
        sleep(3)
        delete_button = super().wait_element_to_be_clickable("//button[contains(text(),'Mass Delete')]")
        delete_button.click()
        delete_button = super().wait_element_to_be_clickable(
            "//div[@class='modal-footer new-modal-footer']//button[contains(text(),'OK')]")
        delete_button.click()
        Logging().reportDebugStep(self, "The mass delete was performed")
        return CRMTaskModule()

    '''
           Returns a task was_updated  message if the user entered a valid password
    '''

    def get_message_task(self):
        confirm_message = super().wait_load_element("//div[@class='toast-message']")
        Logging().reportDebugStep(self, "Returns the message task  : " + confirm_message.text)
        return confirm_message.text

    def click_pencil_button(self):
        sleep(3)
        pencil_button = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow'][1]//span[@class='glyphicon glyphicon-pencil cursor-pointer']")
        pencil_button.click()
        return CRMEditEventModule()
