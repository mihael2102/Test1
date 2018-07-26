import re

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


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
