from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.tasks_module.AddEventModule import AddEventModule
from datetime import *
import allure
from src.main.python.utils.config import Config
from src.main.python.utils.logs.Loging import Logging


class CalendarViewModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def add_new_task(self):
        add_new_task_button = super().wait_element_to_be_clickable("//button[contains(text(),'Add New Task')]")
        add_new_task_button.click()
        Logging().reportDebugStep(self, "The add new task module was opened")
        return AddEventModule()

    def click_calendar_display(self, hour):
        calendar_scroll = super().wait_element_to_be_clickable("//tr[@data-time='%s:00:00']" % hour)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", calendar_scroll)

        Logging().reportDebugStep(self, "Scroll down has been performed ")

        return CalendarViewModule()

    def perform_screen_shot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/task_module/tasks_screenshot %s.png' % now
        Config.browser.get_screenshot_as_file(file_name)
        allure.attach('failed_screenshot', Config.browser.get_screenshot_as_png(),
                      type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed ")
        return CalendarViewModule()

    def close_calendar_view(self):
        close_button = super().wait_element_to_be_clickable("//button[contains(text(),'Close')]")
        close_button.click()
        Logging().reportDebugStep(self, "The calendar view module was closed")
        return CalendarViewModule()

    def open_month_tab(self):
        month_tab_button = super().wait_element_to_be_clickable("//button[contains(text(),'Month')]")
        month_tab_button.click()
        Logging().reportDebugStep(self, "The Month tab was opened")
        return CalendarViewModule()

    def open_week_tab(self):
        week_tab_button = super().wait_element_to_be_clickable("//button[contains(text(),'Week')]")
        week_tab_button.click()
        Logging().reportDebugStep(self, "The Week tab was opened")
        return CalendarViewModule()

    def open_day_tab(self):
        day_tab_button = super().wait_element_to_be_clickable("//button[contains(text(),'Day')]")
        day_tab_button.click()
        Logging().reportDebugStep(self, "The Day tab was opened")
        return CalendarViewModule()

    def get_sunday_text(self):
        sunday_tab_button = super().wait_element_to_be_clickable("//div[@class='fc-row fc-widget-header']//th[1]")
        Logging().reportDebugStep(self, "The first day is : " + sunday_tab_button.text)
        return sunday_tab_button.text

    def get_monday_text(self):
        monday_tab_button = self.driver.find_element(By.XPATH, "//div[@class='fc-row fc-widget-header']//th[2]")
        Logging().reportDebugStep(self, "The second day is : " + monday_tab_button.text)
        return monday_tab_button.text

    def get_current_date(self):
        current_day = self.driver.find_element(By.XPATH, "//div[@class='fc-center'] ")
        Logging().reportDebugStep(self, "The current today day is : " + current_day.text)
        return current_day.text

    def get_day_of_week(self):
        day_of_week = self.driver.find_element(By.XPATH,
                                               "//div[@class='fc-row fc-widget-header']//th[2]//span")
        Logging().reportDebugStep(self, "The day of week day is : " + day_of_week.text)
        return day_of_week.text

    def get_tuesday_text(self):
        tuesday_tab_button = self.driver.find_element(By.XPATH, "//div[@class='fc-row fc-widget-header']//th[3]")
        Logging().reportDebugStep(self, "The third day is : " + tuesday_tab_button.text)
        return tuesday_tab_button.text

    def get_wednesday_text(self):
        wednesday_tab_button = self.driver.find_element(By.XPATH, "//div[@class='fc-row fc-widget-header']//th[4]")
        Logging().reportDebugStep(self, "The fourth day is : " + wednesday_tab_button.text)
        return wednesday_tab_button.text

    def get_thursday_text(self):
        thursday_tab_button = self.driver.find_element(By.XPATH, "//div[@class='fc-row fc-widget-header']//th[5]")
        Logging().reportDebugStep(self, "The fifth day is : " + thursday_tab_button.text)
        return thursday_tab_button.text

    def get_friday_text(self):
        friday_tab_button = self.driver.find_element(By.XPATH, "//div[@class='fc-row fc-widget-header']//th[6]")
        Logging().reportDebugStep(self, "The sixth day is : " + friday_tab_button.text)
        return friday_tab_button.text

    def get_saturday_text(self):
        saturday_tab_button = self.driver.find_element(By.XPATH, "//div[@class='fc-row fc-widget-header']//th[7]")
        Logging().reportDebugStep(self, "The seventh day is : " + saturday_tab_button.text)
        return saturday_tab_button.text
