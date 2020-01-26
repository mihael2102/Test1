from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.audit_logs_ui.AuditLogsModuleConstantsUI import \
    AuditLogsModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI


class AuditLogsSearchingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def audit_logs_searching_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                new_design=0,
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Audit Logs module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_AUDIT_LOGS)

        """ Searching by columns """
        GlobalTablePageUI(self.driver) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_MODULE,
                                      data=AuditLogsModuleConstantsUI.MODULE_USERS) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_ACTION,
                                      data=AuditLogsModuleConstantsUI.ACTION_OTP_LOGIN) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.MODULE_USERS) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.DATA_OTP_LOGIN) \
            .refresh_page()

        GlobalTablePageUI(self.driver) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_MODULE,
                                      data=AuditLogsModuleConstantsUI.MODULE_TRANSACTIONS) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_ACTION,
                                      data=AuditLogsModuleConstantsUI.ACTION_EXPORT) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.DATA_TRANSACTIONS) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.ACTION_EXPORT) \
            .refresh_page()

        GlobalTablePageUI(self.driver) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_MODULE,
                                      data=AuditLogsModuleConstantsUI.MODULE_LEADS) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_ACTION,
                                      data=AuditLogsModuleConstantsUI.ACTION_SAVE) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.MODULE_LEADS) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.ACTION_SAVE) \
            .refresh_page()

        GlobalTablePageUI(self.driver) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_MODULE,
                                      data=AuditLogsModuleConstantsUI.MODULE_LEADS) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_ACTION,
                                      data=AuditLogsModuleConstantsUI.ACTION_DETAIL_VIEW) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.MODULE_LEADS) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.DATA_DETAIL_VIEW) \
            .refresh_page()

        GlobalTablePageUI(self.driver) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_MODULE,
                                      data=AuditLogsModuleConstantsUI.MODULE_LEADS) \
            .select_data_column_field(column=AuditLogsModuleConstantsUI.COLUMN_ACTION,
                                      data=AuditLogsModuleConstantsUI.ACTION_EDIT_VIEW) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.MODULE_LEADS) \
            .global_data_checker_new_ui(AuditLogsModuleConstantsUI.DATA_EDIT_VIEW)
