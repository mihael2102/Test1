from time import sleep

import allure
from datetime import *
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from allure_commons.types import AttachmentType


class HelpDeskDetailViewPage(CRMBasePage):
    def __init__(self):
        super().__init__()

    def get_category_status_text(self):
        category = super().wait_load_element("//span[@id='dtlview_Category']")
        Logging().reportDebugStep(self, "Returns category of ticket: " + category.text)
        return category.text

    def get_ticket_status_text(self):
        status = super().wait_load_element("//td[@id='mouseArea_Status']")
        Logging().reportDebugStep(self, "Returns status of ticket: " + status.text)
        return status.text

    def get_subject_tittle(self):
        subject_tittle = super().wait_load_element("//td[@id='mouseArea_Title']")
        new_subject_tittle = subject_tittle.text.strip()
        Logging().reportDebugStep(self, "The subject is:  " + new_subject_tittle)
        return new_subject_tittle

    def get_account_name(self):
        account_name = super().wait_load_element("//td[contains(text(),'Account Name')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "The subject is:  " + account_name.text)
        return account_name.text

    def get_description_text(self):
        description = super().wait_load_element("//td[contains(text(),'Description')]//following-sibling::td[1]")
        new_description = description.text.strip()
        Logging().reportDebugStep(self, "The description is:  " + new_description)
        return new_description

    def get_assigned_to_text(self):
        assigned = super().wait_load_element("//td[contains(text(),'Assigned To')]//following-sibling::td[1]")
        new_assigned = assigned.text.strip()
        Logging().reportDebugStep(self, "The Assigned To is:  " + new_assigned)
        return new_assigned

    def get_notes_text(self):
        notes = super().wait_load_element("//td[contains(text(),'Notes')]//following-sibling::td[1]")
        new_notes = notes.text.strip()
        Logging().reportDebugStep(self, "The notes is: " + new_notes)
        return new_notes

    def get_priority_text(self):
        priority = super().wait_load_element("//td[contains(text(),'Priority')]//following-sibling::td[1]")
        new_priority = priority.text.strip()
        Logging().reportDebugStep(self, "The priority is:  " + new_priority)
        return new_priority

    def get_title_text(self):
        tittle = super().wait_load_element("//td[contains(text(),'Title')]//following-sibling::td[1]")
        new_tittle = tittle.text.strip()
        Logging().reportDebugStep(self, "The tittle is:  " + new_tittle)
        return new_tittle

    def get_ticket_number_text(self):
        ticket_number = super().wait_load_element("//td[contains(text(),'Ticket No')]//following-sibling::td[1]")
        new_tittle = ticket_number.text.strip()
        Logging().reportDebugStep(self, "The tittle is:  " + new_tittle)
        return new_tittle

    def get_brand_text(self):
        brand_field = super().wait_load_element("//td[contains(text(),'Brand')]//following-sibling::td[1]")
        new_brand_field = brand_field.text.strip()
        Logging().reportDebugStep(self, "The brand is:  " + new_brand_field)
        return new_brand_field

    def perform_screen_shot_searching_tickets(self):
        sleep(3)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/leads_module/leads_screenshot %s.png' % now
        self.driver.get_screenshot_as_file(file_name)
        allure.MASTER_HELPER.attach('screenshot', self.driver.get_screenshot_as_png(),
                                    type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "Screenshot was performed ")
        return HelpDeskDetailViewPage()

    def get_ca_id_text(self):
        ca_id = super().wait_load_element("//td[contains(text(),'Ticket No')]//following-sibling::td[1]")
        new_tittle = ca_id.text.strip()
        Logging().reportDebugStep(self, "The tittle is:  " + new_tittle)
        return new_tittle

    def came_back_on_previous_page(self):
        super().came_back_on_previous_page()
        return HelpDeskDetailViewPage()
