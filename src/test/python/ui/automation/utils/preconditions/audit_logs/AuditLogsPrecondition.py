from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.pages.audit_logs.AuditLogsPage import AuditLogsPage
from src.main.python.ui.crm.model.constants.AuditLogsConstants import AuditLogsConstants


class AuditLogsPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def check_audit_logs_loading(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver)\
            .open_more_list_modules()\
            .select_audit_logs_module_more_list(CRMConstants.AUDITLOGS_MODULE)\
            .check_audit_logs_loaded()

    def searching_by_columns(self):
        """ Login to CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Audit Logs module """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_AUDIT_LOGS)

        """ Searching by columns """
        AuditLogsPage(self.driver)\
            .searching_by_2_columns(AuditLogsConstants.MODULE_USERS,
                                    AuditLogsConstants.ACTION_OTP_LOGIN)\
            .audit_logs_data_checker(AuditLogsConstants.MODULE_USERS)\
            .audit_logs_data_checker(AuditLogsConstants.ACTION_OTP_LOGIN)\
            .refresh_page()
        AuditLogsPage(self.driver)\
            .searching_by_2_columns(AuditLogsConstants.MODULE_TRANSACTIONS,
                                    AuditLogsConstants.ACTION_EXPORT)\
            .audit_logs_data_checker(AuditLogsConstants.MODULE_TRANSACTIONS)\
            .audit_logs_data_checker(AuditLogsConstants.ACTION_EXPORT)\
            .refresh_page()
        AuditLogsPage(self.driver) \
            .searching_by_2_columns(AuditLogsConstants.MODULE_LEADS,
                                    AuditLogsConstants.ACTION_SAVE) \
            .audit_logs_data_checker(AuditLogsConstants.MODULE_LEADS) \
            .audit_logs_data_checker(AuditLogsConstants.ACTION_SAVE) \
            .refresh_page()
        AuditLogsPage(self.driver) \
            .searching_by_2_columns(AuditLogsConstants.MODULE_LEADS,
                                    AuditLogsConstants.ACTION_DETAIL_VIEW) \
            .audit_logs_data_checker(AuditLogsConstants.MODULE_LEADS) \
            .audit_logs_data_checker(AuditLogsConstants.ACTION_DETAIL_VIEW) \
            .refresh_page()
        AuditLogsPage(self.driver) \
            .searching_by_2_columns(AuditLogsConstants.MODULE_LEADS,
                                    AuditLogsConstants.ACTION_EDIT_VIEW) \
            .audit_logs_data_checker(AuditLogsConstants.MODULE_LEADS) \
            .audit_logs_data_checker(AuditLogsConstants.ACTION_EDIT_VIEW)
