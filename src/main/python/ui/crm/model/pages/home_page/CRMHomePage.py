from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.auto_assign.AutoAssignPage import AutoAssignPage
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.audit_logs.AuditLogsPage import AuditLogsPage
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage
from src.main.python.ui.crm.model.pages.financial_transactions.FinancialTransactionsPage import \
    FinancialTransactionsPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.modules.my_dashboard.MyDashBoardModule import MyDashBoardModule
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.main.python.ui.crm.model.modules.user_management.UserManagement import UserManagement
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsPage import TradingAccountsPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.affiliates.AffiliatePage import AffiliatePage
from src.main.python.ui.crm.model.pages.dashboard.DashboardPage import DashboardPage
from src.main.python.ui.crm.model.pages.leaderboard.LeaderboardPage import LeaderboardPage
from src.main.python.ui.crm.model.pages.usermanagement.UserManagementPage import UserManagementPage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import datetime
import re


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

    def select_user_management(self):
        sleep(5)
        # if global_var.current_brand_name == "brokerxp":
        #     user_settings = super().wait_element_to_be_clickable("/html/body/table[1]/tbody/tr/td[3]/table/tbody/tr/td[4]/img")
        # else:
        user_settings = super().wait_element_to_be_clickable(
                "/html/body/table[1]/tbody/tr/td[3]/table/tbody/tr/td[3]/img")
        user_settings.click()
        user_management = super().wait_element_to_be_clickable("//a[contains(text(), 'User Management')]")
        try:
            user_management.click()
        except:
            self.driver.execute_script("arguments[0].click();", user_management)
        Logging().reportDebugStep(self, "Go to User Management")
        return UserManagementPage(self.driver)

    def open_more_list_modules(self):
        hover_mouse = ActionChains(self.driver)
        more_list_element = super().wait_element_to_be_clickable("//a[contains(text(),'More')]")
        hover_mouse.move_to_element(more_list_element)
        hover_mouse.perform()
        return CRMHomePage(self.driver)

    def select_documents_module_more_list(self, module):
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
        self.driver.execute_script("arguments[0].click();", task_module)
        # task_module.click()
        Logging().reportDebugStep(self, "Leads module was opened")
        return LeadsModule(self.driver)

    def select_financial_transactions_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[contains(text(), '%s')]" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The financial_transactions_module was selected")
        return FinancialTransactionsPage(self.driver)

    def select_audit_logs_module_more_list(self, module):
        try:
            module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
            module_element.click()
            Logging().reportDebugStep(self, "The audit logs module was opened")
        except TimeoutException:
            Logging().reportDebugStep(self, "There are no module")
        return AuditLogsPage(self.driver)

    def select_auto_assign_module_more_list(self, module):
        try:
            module_element = self.driver.find_element_by_xpath("//a[@name='%s']" % module)
            self.driver.execute_script("arguments[0].click();", module_element)
            Logging().reportDebugStep(self, "The AutoAssign module was opened")
            return AutoAssignPage(self.driver)
        except NoSuchElementException:
            pass
            Logging().reportDebugStep(self, "The AutoAssign module does not exist")
            return False

    def select_service_desk_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "The Service Desk  module was opened")
        return HelpDeskPage(self.driver)

    def select_my_dashboard_module_more_list(self, module):
        try:
            module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
            module_element.click()
            Logging().reportDebugStep(self, "The My Dashboard module was opened")
        except TimeoutException:
            Logging().reportDebugStep(self, "There are no module")
        return MyDashBoardModule(self.driver)

    def select_affiliates_module_more_list(self, module):
        try:
            module_element = super().wait_element_to_be_clickable("//*[@name='%s']" % module)
            module_element.click()
            Logging().reportDebugStep(self, "The Affiliates page was opened")
            # return AffiliateListViewPage(self.driver)
            return AffiliatePage(self.driver)
        except (NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "The Affiliates module does not exist")

    def select_dashboard_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "Dashboard  module was opened")
        return DashboardPage(self.driver)

    def select_leaderboard_module_more_list(self, module):
        module_element = super().wait_element_to_be_clickable("//a[@name='%s']" % module)
        module_element.click()
        Logging().reportDebugStep(self, "Dashboard  module was opened")
        return LeaderboardPage(self.driver)

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
        sleep(2)
        user_settings = super().wait_element_to_be_clickable(
            "/html/body/table[1]/tbody/tr/td[3]/table/tbody/tr/td[3]/img")
        user_settings.click()
        user_management = self.driver.find_element(By.XPATH,
                                    "//ul[@class='dropdown-menu pull-right']//li//a[contains(text(),'%s')]" % settings)
        self.driver.execute_script("arguments[0].click();", user_management)
        Logging().reportDebugStep(self, "The user management was opened")
        return UserManagement(self.driver)

    def open_trading_account_module(self):
        home_page_element = super().wait_element_to_be_clickable(
            "//span[@class='glyphicon glyphicon-Trading Accounts']")
        home_page_element.click()
        Logging().reportDebugStep(self, "The client module was opened")
        return TradingAccountsPage(self.driver)

    def open_crm_configuration(self, module):
        try:
            module_element = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % module)
            self.driver.execute_script("arguments[0].click();", module_element)
            Logging().reportDebugStep(self, "The CRM Configuration module was opened")
        except (TimeoutException, NoSuchElementException):
            Logging().reportDebugStep(self, "There are no module")
        return AuditLogsPage(self.driver)

    def get_current_version(self, module):
        version = ""
        if module == "vtiger":
            current_version = super().wait_load_element("/html/body/table[4]/tbody/tr/td", timeout=45).text
            current_version_number = current_version.split(".")
            version = current_version_number[1] + current_version_number[2]
        elif module == "laravel":
            current_version = super().wait_load_element(
                "/html/body/app-root/app-footer/footer/div", timeout=45).text
            current_version_str = current_version.split(" ")
            # current_version_number = ""
            if global_var.current_brand_name == "ptbanc":
                current_version_number = current_version_str[2].split(".")
            else:
                current_version_number = current_version_str[1].split(".")
            version = current_version_number[0] + current_version_number[1]
        Logging().reportDebugStep(self, "The current sprint version is: " + version)
        return version

    def check_previous_version(self, brand, module):
        path = "C:/version_of/%s.txt" % brand
        f = open(path, "r")  # name of file open in read mode
        lines = f.readlines()  # split file into lines
        if module == "vtiger":
            prev_version = lines[0]
        else:
            prev_version = lines[1]
        Logging().reportDebugStep(self, "The previous " + module + " sprint version is: " + prev_version)
        return prev_version

    def update_version_in_file(self, new_version, old_version, brand):
        path = "C:/version_of/%s.txt" % brand
        with open(path, 'r') as f:
            lines = f.readlines()
        with open(path, 'w') as f:
            for line in lines:
                line = line.replace(str(old_version), str(new_version) + '\n')
                f.write(line)
        Logging().reportDebugStep(self, "The current sprint version is updated to: " + str(new_version))

    def get_day_of_week(self):
        today = datetime.datetime.today().weekday()
        Logging().reportDebugStep(self, "The current day of the week is: " + str(today))
        return today

