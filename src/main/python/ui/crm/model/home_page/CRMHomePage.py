from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.audit_logs_module.AuditLogsModule import AuditLogsModule
from src.main.python.ui.crm.model.modules.document_module.DocumentModule import DocumentModule
from src.main.python.ui.crm.model.modules.affiliates_modules.AffiliateModule import
from src.main.python.ui.crm.model.modules.financial_transactions_module.FinancialTransactionsModule import \
    FinancialTransactionsModule
from src.main.python.ui.crm.model.modules.help_desk.HelpDeskModule import HelpDeskModule
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.modules.my_dashboard_module.MyDashBoardModule import MyDashBoardModule
from src.main.python.ui.crm.model.modules.tasks_module.TaskModule import TaskModule
from src.main.python.ui.crm.model.modules.affiliates_modules.AffiliateModule import AffiliateModule
from src.main.python.ui.crm.model.modules.user_management.UserManagement import UserManagement
from src.main.python.utils.logs.Loging import Logging


class CRMHomePage(CRMBasePage):

    def __init__(self):
        super().__init__()

    ''' 
         Open the task module 
         return Help Desk instance
     '''

    def open_task_module(self):
        task_module = super().wait_load_element("//span[@class='glyphicon glyphicon-Tasks']")
        task_module.click()
        Logging().reportDebugStep(self, "Task module is opened")
        return TaskModule()

    def open_more_list_modules(self):
        hover_mouse = ActionChains(self.driver)
        more_list_element = super().wait_element_to_be_clickable("//a[contains(text(),'More')]")
        hover_mouse.move_to_element(more_list_element)
        hover_mouse.perform()
        return CRMHomePage()

    def select_document_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The document module was opened")
        return DocumentModule()

    def open_lead_module(self):
        task_module = super().wait_load_element("//span[@class='glyphicon glyphicon-Leads']")
        task_module.click()
        Logging().reportDebugStep(self, "Leads module is opened")
        return LeadsModule()

    def select_financial_transactions_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        return FinancialTransactionsModule()

    def select_audit_logs_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The audit logs module was opened")
        return AuditLogsModule()

    def select_service_desk_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The Service Desk  module was opened")
        return HelpDeskModule()

    def select_my_dashboard_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The my dashboard  module was opened")
        return MyDashBoardModule()

    def select_affiliates_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//*[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The Affiliates module was opened")
        return AffiliateModule()

    def refresh_page(self):
        super().refresh_page()
        return CRMHomePage()

    def open_client_module(self):
        home_page_element = super().wait_element_to_be_clickable("//span[@class='glyphicon glyphicon-Clients']")
        home_page_element.click()
        Logging().reportDebugStep(self, "The client module was opened")
        return CRMHomePage()

    def open_financial_transactions_module(self):
        home_page_element = super().wait_element_to_be_clickable(
            "//span[@class='glyphicon glyphicon-Financial Transactions']")
        home_page_element.click()
        Logging().reportDebugStep(self, "The financial transactions was opened")
        return FinancialTransactionsModule()

    def open_user_management_module(self, settings):
        module_element = super().wait_element_to_be_clickable("//table[@class='user_settings']//td[3]")
        user_management = self.driver.find_element(By.XPATH,
                                                   "//ul[@class='dropdown-menu pull-right']//li//a[contains(text(),'%s')]" % settings)
        hoverer = ActionChains(self.driver).move_to_element(module_element).click(user_management)
        hoverer.perform()
        Logging().reportDebugStep(self, "The user management was opened")
        return UserManagement()
