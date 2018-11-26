from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.modules.campaigns_module.AddCampaignsModule import AddCampaignsModule
from src.main.python.ui.crm.model.pages.auto_assign.AutoAssignPage import AutoAssignPage
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.audit_logs.AuditLogsPage import AuditLogsPage
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.financial_transactions.FinancialTransactionsPage import \
    FinancialTransactionsPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.modules.my_dashboard.MyDashBoardModule import MyDashBoardModule
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.modules.user_management.UserManagement import UserManagement
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsPage import TradingAccountsPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.affiliates.AffiliatePage import AffiliatePage

class CRMHomePage(CRMBasePage):

    ''' 
         Open the task module 
         return Help Desk instance
     '''

    def open_task_module(self):
        task_module = super().wait_element_to_be_clickable("//span[@class='glyphicon glyphicon-Tasks']")
        task_module.click()
        Logging().reportDebugStep(self, "Task module is opened")
        self.wait_crm_loading_to_finish()
        return TasksPage(self.driver)

    def open_more_list_modules(self):
        hover_mouse = ActionChains(self.driver)
        more_list_element = super().wait_element_to_be_clickable("//a[contains(text(),'More')]")
        hover_mouse.move_to_element(more_list_element)
        hover_mouse.perform()
        return CRMHomePage(self.driver)

    def select_document_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The document module was opened")
        return DocumentsPage(self.driver)

    def select_campaigns_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The campaigns module was opened")
        return CampaignsPage(self.driver)

    def open_lead_module(self):
        task_module = super().wait_load_element("//span[@class='glyphicon glyphicon-Leads']")
        task_module.click()
        Logging().reportDebugStep(self, "Leads module was opened")
        return LeadsModule(self.driver)

    def select_financial_transactions_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[contains(text(), '%s')]" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The financial_transactions_module was selected")
        return FinancialTransactionsPage(self.driver)

    def select_audit_logs_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The audit logs module was opened")
        return AuditLogsPage(self.driver)

    def select_auto_assign_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The audit logs module was opened")
        return AutoAssignPage(self.driver)

    def select_service_desk_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The Service Desk  module was opened")
        return HelpDeskPage(self.driver)

    def select_my_dashboard_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The my dashboard  module was opened")
        return MyDashBoardModule(self.driver)

    def select_affiliates_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//*[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The Affiliates page was opened")
        # return AffiliateListViewPage(self.driver)
        return AffiliatePage(self.driver)

    def refresh_page(self):
        super().refresh_page()
        return CRMHomePage(self.driver)

    def open_help_desk_page(self):
        help_desc_module = super().wait_load_element("//a[contains(text(), 'Help Desk')]")
        help_desc_module.click()
        Logging().reportDebugStep(self, "Open  help desk module ")
        return HelpDeskPage(self.driver)

    def open_client_module(self):
        sleep(2)
        home_page_element = self.wait_visible_of_element("//span[@class='glyphicon glyphicon-Clients']")
        home_page_element.click()
        Logging().reportDebugStep(self, "The client module was opened")
        return ClientsPage(self.driver)

    def open_financial_transactions_module(self):
        home_page_element = super().wait_element_to_be_clickable(
            "//span[@class='glyphicon glyphicon-Financial Transactions']")
        home_page_element.click()
        Logging().reportDebugStep(self, "The financial transactions was opened")
        return FinancialTransactionsPage(self.driver)

    def open_user_management_module(self, settings):
        module_element = super().wait_element_to_be_clickable("//table[@class='user_settings']//td[4]")
        user_management = self.driver.find_element(By.XPATH,
                                                   "//ul[@class='dropdown-menu pull-right']//li//a[contains(text(),'%s')]" % settings)
        hoverer = ActionChains(self.driver).move_to_element(module_element).click(user_management)
        hoverer.perform()
        Logging().reportDebugStep(self, "The user management was opened")
        return UserManagement(self.driver)

    def open_trading_account_module(self):
        home_page_element = super().wait_element_to_be_clickable(
            "//span[@class='glyphicon glyphicon-Trading Accounts']")
        home_page_element.click()
        Logging().reportDebugStep(self, "The client module was opened")
        return TradingAccountsPage(self.driver)
