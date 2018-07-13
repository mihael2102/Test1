from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class HelpDeskDetailViewPage(CRMBasePage):
    def __init__(self):
        super().__init__()

    def get_category_status_text(self):
        category = super().wait_load_element("//span[@id='dtlview_Category']")
        Logging().reportDebugStep(self, "Returns category of ticket: " + category.text)
        return category.text

    def get_ticket_status_text(self):
        category = super().wait_load_element("//td[@id='mouseArea_Status']")
        Logging().reportDebugStep(self, "Returns status of ticket: " + category.text)

    def get_subject_tittle(self):
        subject_tittle = super().wait_load_element("//td[@id='mouseArea_Title']")
        new_subject_tittle = re.sub(' ', "", subject_tittle.text)
        Logging().reportDebugStep(self, "The subject is set:  " + new_subject_tittle)
        return new_subject_tittle
