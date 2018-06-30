from time import sleep

from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.tasks_module.AddEventModule import AddEventModule
from src.main.python.ui.crm.model.modules.tasks_module.CalendarViewModule import CalendarViewModule
from src.main.python.ui.crm.model.modules.tasks_module.CallModule import CallTaskModule
from src.main.python.ui.crm.model.modules.tasks_module.EditEventModule import EditEventModule
from src.main.python.ui.crm.model.modules.tasks_module.MassEditTaskModule import MassEditTaskModule
from src.main.python.ui.crm.model.modules.tasks_module.MassSMSModule import MassSMSModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from datetime import *
import allure
from allure.constants import AttachmentType
from src.main.python.utils.config import Config


class TaskModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    '''
        Open the second tabs of crm page
        :parameter url crm page url  
    '''

    def open_second_tab_page(self, url):
        super().open_second_tab_page(url)
        Logging().reportDebugStep(self, "Open second tabs page: " + url + '\n')
        return TaskModule()

    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return TaskModule()

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

    def open_show_all_tab(self):
        sleep(1)
        tab = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[1]")
        tab.click()
        Logging().reportDebugStep(self, "The this week tab was opened ")
        return TaskModule()

    def open_sms_module(self):
        first_check_box = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow']//div[2]")
        first_check_box.click()
        Logging().reportDebugStep(self, "The sms module was opened: ")
        return MassSMSModule()

    def open_mass_edit_task(self):
        mass_edit_module = super().wait_element_to_be_clickable("//button[contains(text(),'Mass Edit')]")
        mass_edit_module.click()
        return MassEditTaskModule()

    def get_history_tab_text(self):
        tab = self.driver.find_element(By.XPATH,
                                       "//ul[@id='main-tabs']//li[5]")
        tab.click()
        sleep(1)
        tab_text = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[5]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def open_add_event_module(self):
        sleep(3)
        event_button = super().wait_element_to_be_clickable("//button[contains(text(),'Add Event')]")
        event_button.click()
        Logging().reportDebugStep(self, "The event  module was opened ")
        return AddEventModule()

    def open_calendar_view_module(self):
        calendar_view_button = self.driver.find_element(By.XPATH,
                                                        "//button[contains(text(),'Calendar View')]")
        calendar_view_button.click()
        Logging().reportDebugStep(self, "The calendar view module was opened")
        return CalendarViewModule()

    def select_several_records_task_module(self):
        sleep(1)
        first_check_box = super().wait_element_to_be_clickable("//div[@class='table-grid-container']//tr[3]//td[1]")
        first_check_box.click()
        second_check_box = self.driver.find_element(By.XPATH, "//div[@class='table-grid-container']//tr[4]//td[1]")
        second_check_box.click()
        third_check_box = self.driver.find_element(By.XPATH, "//div[@class='table-grid-container']//tr[5]//td[1]")
        third_check_box.click()
        Logging().reportDebugStep(self, "The records were selected")
        return TaskModule()

    def perform_mass_delete(self):
        sleep(3)
        delete_button = super().wait_element_to_be_clickable("//button[contains(text(),'Mass Delete')]")
        delete_button.click()
        delete_button = super().wait_element_to_be_clickable(
            "//div[@class='modal-footer new-modal-footer']//button[contains(text(),'OK')]")
        delete_button.click()
        Logging().reportDebugStep(self, "The mass delete was performed")
        return TaskModule()

    def open_mass_sms_module(self):
        event_button = self.driver.find_element(By.XPATH,
                                                "//button[contains(text(),'Mass SMS')]")
        event_button.click()
        Logging().reportDebugStep(self, "The event  module was opened ")
        return MassSMSModule()

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
        return EditEventModule()

    def click_ok(self):
        super().click_ok()
        Logging().reportDebugStep(self, "Message sent successfully")
        return MassSMSModule()

    def open_first_client_profile(self):
        sleep(3)
        client_link = super().wait_element_to_be_clickable(
            "//div[@class='table-grid-container']//tr[3]//td[6]")
        client_link.click()
        Logging().reportDebugStep(self, "The first client profile is opened")
        return ClientProfilePage()

    def open_second_client_profile(self):
        sleep(3)
        client_link = super().wait_element_to_be_clickable(
            "//div[@class='table-grid-container']//tr[4]//td[6]")
        client_link.click()
        Logging().reportDebugStep(self, "The second client profile was opened ")
        return ClientProfilePage()

    def open_third_client_profile(self):
        sleep(3)
        client_link = super().wait_element_to_be_clickable(
            "//div[@class='table-grid-container']//tr[5]//td[6]")
        client_link.click()
        Logging().reportDebugStep(self, "The third client profile was opened ")
        return ClientProfilePage()

    def perform_screen_shot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/task_module/tasks_screenshot %s.png' % now
        Config.browser.get_screenshot_as_file(file_name)
        allure.MASTER_HELPER.attach('passed_screenshot', Config.browser.get_screenshot_as_png(),
                                    type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed ")
        return CalendarViewModule()

    def find_event_by_subject(self, subject):
        sleep(2)
        subject_field = super().wait_element_to_be_clickable("//tr[@class='tableFilters']//td[15]//input")
        subject_field.clear()
        subject_field.send_keys(subject)
        Logging().reportDebugStep(self, "The subject was set: " + subject)
        sleep(3)
        return TaskModule()

    def open_call_module(self):
        first_check_box = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow'][1]//div[3]")
        first_check_box.click()
        Logging().reportDebugStep(self, "The call phone module was opened: ")
        return CallTaskModule()
