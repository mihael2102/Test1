from src.main.python.ui.crm.model.constants.AuditLogsConstants import AuditLogsConstants
from src.main.python.ui.crm.model.constants.ReportConstants import ReportConstants, ManagementReportConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *


class ReportModuleTest(BaseTest):

    def test_check_import_reports(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        reports_module = CRMHomePage().open_more_list_modules() \
            .select_report_module_more_list(ReportConstants.REPORTS_MODULE)

        audit_log_module = CRMHomePage().open_second_tab_page(Config.url_crm) \
            .open_more_list_modules() \
            .select_audit_logs_module_more_list(AuditLogsConstants.AUDIT_LOGS_MODULE)

        reports_module.switch_first_tab_page() \
            .open_performance_report_by_date_page(
            Config.data.get_data_management_report_module(ManagementReportConstants.FIRST_MANAGEMENT_REPORT)) \
            .perform_export_to_excel()

        audit_log_module.switch_second_tab_page()

        assert audit_log_module.get_performance_text(
            Config.data.get_data_management_report_module(ManagementReportConstants.FIRST_MANAGEMENT_EXPORT))
