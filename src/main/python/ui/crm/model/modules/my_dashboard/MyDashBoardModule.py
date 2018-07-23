from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.tasks_module.CallModule import PhoneActionsModule
from src.main.python.ui.crm.model.modules.tasks_module.MassSMSModule import MassSMSModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging


class MyDashBoardModule(CRMBasePage):
    def __init__(self) -> None:
        super().__init__()

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

    def open_sms_module_my_dashboard(self):
        first_check_box = super().wait_element_to_be_clickable(
            "//tr[@class='tableRow']//div[2]")
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
            "//div[@class='table-grid-container']//tr[3]//td[6]")
        client_link.click()
        Logging().reportDebugStep(self, "The first client profile is opened")
        return ClientProfilePage()
