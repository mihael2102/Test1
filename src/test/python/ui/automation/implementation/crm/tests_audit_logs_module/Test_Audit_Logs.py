import pytest

from src.main.python.ui.crm.model.constants.AuditLogsConstants import AuditLogsConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=29)
class AuditLogs(BaseTest):

    def test_check_tab_audit_logs_module(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        audit_logs_module = CRMHomePage().open_more_list_modules() \
            .select_audit_logs_module_more_list(AuditLogsConstants.AUDIT_LOGS_MODULE)

        all_tab_name = audit_logs_module.get_all_tab_text()

        assert all_tab_name == Config.data.get_data_audit_logs_info(AuditLogsConstants.FIRST_TAB)
        audit_logs_module.open_calendar_view().perform_screen_shot()

        today_tab_text = audit_logs_module.get_today_tab_text()

        assert today_tab_text == Config.data.get_data_audit_logs_info(AuditLogsConstants.SECOND_TAB)
        audit_logs_module.open_calendar_view().perform_screen_shot()

        week_tab_text = audit_logs_module.get_week_tab_text()

        assert week_tab_text == Config.data.get_data_audit_logs_info(AuditLogsConstants.THIRD_TAB)
        audit_logs_module.open_calendar_view().perform_screen_shot()

        month_tab_text = audit_logs_module.get_month_tab_text()

        assert month_tab_text == Config.data.get_data_audit_logs_info(AuditLogsConstants.FOURTH_TAB)
        audit_logs_module.open_calendar_view().perform_screen_shot()

    def test_check_searching_module(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        audit_logs_module = CRMHomePage().open_more_list_modules() \
            .select_audit_logs_module_more_list(AuditLogsConstants.AUDIT_LOGS_MODULE)

        audit_logs_module.perform_searching(Config.data.get_data_audit_logs_info(AuditLogsConstants.FIRST_MODULE),
                                            Config.data.get_data_audit_logs_info(AuditLogsConstants.FIRST_ACTION),
                                            Config.data.get_data_audit_logs_info(AuditLogsConstants.FIRST_USER),
                                            Config.data.get_data_audit_logs_info(AuditLogsConstants.FIRST_EMAIL),
                                            Config.data.get_data_audit_logs_info(AuditLogsConstants.FIRST_ID_RECORD),
                                            Config.data.get_data_audit_logs_info(AuditLogsConstants.FIRST_USER_AGENT))

        audit_logs_module.perform_screen_shot()
