from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.leads_pages.CreateLeadsProfilePage import CreateLeadsProfilePage

from src.main.python.utils.logs.Loging import Logging


class LeadsModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def open_create_lead_module(self):
        task_module = super().wait_load_element("//td[@class='moduleName']//button[1]")
        task_module.click()
        Logging().reportDebugStep(self, "Create leads module is opened")
        return CreateLeadsProfilePage()


