from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.main.python.ui.crm.model.modules.tasks_module.SendEmailModuleActions import SendEmailModuleActions
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.tasks_module.CallModule import PhoneActionsModule
from src.main.python.ui.crm.model.modules.tasks_module.MassSMSModule import MassSMSModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC


class MyDashBoardModule(CRMBasePage):
    # def __init__(self) -> None:
    #     super().__init__()

    def open_show_all_tab(self):
        sleep(1)
        tab = super().wait_element_to_be_clickable("//ul[@id='main-tabs']//li[1]")
        tab.click()
        Logging().reportDebugStep(self, "The this week tab was opened ")
        return MyDashBoardModule()

    def find_event_by_subject(self, subject):
        sleep(2)
        subject_field = super().wait_element_to_be_clickable("//tr[@class='tableFilters']//td[15]//input")
        subject_field.clear()
        subject_field.send_keys(subject)
        Logging().reportDebugStep(self, "The subject was set: " + subject)
        sleep(3)
        return MyDashBoardModule()

    def open_phone_actions(self):
        sleep(2)
        first_check_box = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow'][1]//div[3]")
        first_check_box.click()
        Logging().reportDebugStep(self, "The call phone module was opened: ")
        return PhoneActionsModule()

    def open_email_actions_section(self):
        first_check_box = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow'][1]//td[18]//div[1]")
        first_check_box.click()
        Logging().reportDebugStep(self, "The sms module was opened")
        return SendEmailModuleActions()

    '''
       Returns a task was_updated  message if the user entered a valid password
    '''

    def get_confirm_message_task_module(self):
        sleep(2)
        confirm_message = super().wait_load_element("//div[@class='toast-message']")
        Logging().reportDebugStep(self, "Returns the message task  : " + confirm_message.text)
        return confirm_message.text

    def open_sms_module_my_dashboard(self):
        sleep(3)
        first_check_box = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//tr[@class='tableRow']//div[2]")))
        first_check_box.click()
        Logging().reportDebugStep(self, "The sms module was opened: ")
        return MassSMSModule()

    def perform_scroll_down(self):
        super().wait_element_to_be_clickable("//tr[@class='tableRow'][1]//div[3]")
        super().perform_scroll_down()
        return MyDashBoardModule()

    def open_call_module_my_dashboard(self):
        first_check_box = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow'][1]//div[3]")
        first_check_box.click()
        Logging().reportDebugStep(self, "The call phone module was opened: ")
        return PhoneActionsModule()

    def came_back_on_previous_page(self):
        super().came_back_on_previous_page()
        Logging().reportDebugStep(self, "came back on previous page was performed")
        return MyDashBoardModule()

    def open_first_client_profile(self):
        sleep(3)
        client_link = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow']//td[6]")
        client_link.click()
        Logging().reportDebugStep(self, "The first client profile is opened")
        return ClientProfilePage()
