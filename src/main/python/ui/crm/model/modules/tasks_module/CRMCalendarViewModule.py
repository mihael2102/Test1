from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.tasks_module.CRMAddEventModule import CRMAddEventModule
from datetime import *
import allure
from allure.constants import AttachmentType
from src.main.python.utils.config import Config
from src.main.python.utils.logs.Loging import Logging


class CRMCalendarViewModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def add_new_task(self):
        add_new_task_button = super().wait_element_to_be_clickable("//button[contains(text(),'Add New Task')]")
        add_new_task_button.click()
        Logging().reportDebugStep(self, "The add new task module was opened")
        return CRMAddEventModule()

    def click_calendar_display(self, hour):
        calendar_scroll = super().wait_element_to_be_clickable("//tr[@data-time='%s:00:00']" % hour)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", calendar_scroll)

        Logging().reportDebugStep(self, "Scroll down has been performed ")

        return CRMCalendarViewModule()

    def perform_screen_shot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/results/screenshots/task_module/tasks_screenshot %s.png' % now
        Config.browser.get_screenshot_as_file(file_name)
        allure.MASTER_HELPER.attach('failed_screenshot', Config.browser.get_screenshot_as_png(),
                                    type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed ")
        return CRMCalendarViewModule()

    def close_calendar_view(self):
        close_button = super().wait_element_to_be_clickable("//button[contains(text(),'Close')]")
        close_button.click()
        Logging().reportDebugStep(self, "The calendar view module was closed")
        return CRMCalendarViewModule()
