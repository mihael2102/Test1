from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.side_bar.SidebarModules import SidebarModules
from src.main.python.ui.crm.model.modules.leads_module.ConvertLeadModule import ConvertLeadModule
from src.main.python.ui.crm.model.pages.leads.EditLeadsProfilePage import EditLeadsProfilePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class LeadViewInfo(CRMBasePage):

    def click_delete_button(self):
        task_module = super().wait_load_element("//input[@name='Delete']")
        task_module.click()
        Logging().reportDebugStep(self, "The delete pop-up is displayed")
        return LeadViewInfo(self.driver)

    def edit_lead_profile(self):
        task_module = super().wait_load_element("//input[@name='Delete']")
        task_module.click()
        Logging().reportDebugStep(self, "The delete pop-up is displayed")
        return EditLeadsProfilePage(self.driver)

    def open_convert_lead_module(self):
        SidebarModules(self.driver).open_sidebar_if_exists()
        sleep(2)
        task_module = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["convert_lead_module"])
        task_module.click()
        Logging().reportDebugStep(self, "The convert lead module was opened")
        return ConvertLeadModule(self.driver)

    '''
        Returns a confirmation  message if the user entered a valid password
    '''

    def get_confirm_message_lead_view_profile(self):
        confirm_message = self.wait_load_element("//div[contains(@class, 'bootstrap-dialog-message')]")
        Logging().reportDebugStep(self, "Returns a confirmation message: " + confirm_message.text)
        return confirm_message.text

    def click_ok(self):
        super().click_ok()
        return ConvertLeadModule(self.driver)
