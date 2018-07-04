from selenium.webdriver import ActionChains
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.audit_logs_module.AuditLogsModule import AuditLogsModule
from src.main.python.ui.crm.model.modules.document_module.DocumentModule import DocumentModule
from src.main.python.ui.crm.model.modules.financial_transactions_module.FinancialTransactionsModule import \
    FinancialTransactionsModule
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.modules.my_dashboard_module.MyDashBoardModule import MyDashBoardModule
from src.main.python.ui.crm.model.modules.tasks_module.TaskModule import TaskModule
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

    def select_my_dashboard_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The my dashboard  module was opened")
        return MyDashBoardModule()

    def refresh_page(self):
        super().refresh_page()
        return CRMHomePage()

    def open_home_page(self):
        home_page_element = super().wait_element_to_be_clickable("//a//img[@src='themes/panda/images/Home.PNG']")
        home_page_element.click()
        Logging().reportDebugStep(self, "The home page was opened")
        return CRMHomePage()

