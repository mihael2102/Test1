from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.leads_pages.EditLeadsProfilePage import EditLeadsProfilePage
from src.main.python.utils.logs.Loging import Logging


class LeadViewInfo(CRMBasePage):

    def __init__(self) -> None:
        super().__init__()

    def click_delete_button(self):
        task_module = super().wait_load_element("//input[@name='Delete']")
        task_module.click()
        Logging().reportDebugStep(self, "The delete pop-up is displayed")
        return LeadViewInfo()

    def edit_lead_profile(self):
        task_module = super().wait_load_element("//input[@name='Delete']")
        task_module.click()
        Logging().reportDebugStep(self, "The delete pop-up is displayed")
        return EditLeadsProfilePage()
