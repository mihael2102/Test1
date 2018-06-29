from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.leads_module.CreateLeadsModule import CreateLeadsModule
from src.main.python.utils.logs.Loging import Logging


class LeadsModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def open_create_lead_module(self):
        task_module = super().wait_load_element("//td[@class='moduleName']//button[1]")
        task_module.click()
        Logging().reportDebugStep(self, "Create leads module is opened")
        return CreateLeadsModule()

    def click_delete_button(self):
        task_module = super().wait_load_element("//input[@name='Delete']")
        task_module.click()
        Logging().reportDebugStep(self, "The delete pop-up is displayed")
        return CreateLeadsModule()
