from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.leads_module.ConvertLeadModule import ConvertLeadModule
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

    def open_convert_lead_module(self):
        task_module = super().wait_load_element("//div[@id='sidebar']//tr[3]//a")
        task_module.click()
        Logging().reportDebugStep(self, "The convert lead module was opened")
        return ConvertLeadModule()

    '''
        Returns a confirmation  message if the user entered a valid password
    '''

    def get_confirm_message_lead_view_profile(self):
        confirm_message = super().wait_load_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "Returns a confirmation message: " + confirm_message.text)
        return confirm_message.text

    def click_ok(self):
        super().click_ok()
        return ConvertLeadModule()
