import pytest

from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=27)
class ImportLeadTest(BaseTest):

    def test_import_lead(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        import_page = CRMHomePage().open_lead_module() \
            .open_today_lead_tab() \
            .perform_screen_shot_import_lead_module() \
            .open_import_page() \
            .perform_first_step_upload_lead() \
            .click_next_button() \
            .select_source_lead(
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_IMPORT_LEAD,
                                           LeadsModuleConstants.THIRD_LEAD_SOURCE)) \
            .set_source_name(
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_IMPORT_LEAD,
                                           LeadsModuleConstants.THIRD_SOURCE_NAME)) \
            .select_status(
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_IMPORT_LEAD,
                                           LeadsModuleConstants.THIRD_LEAD_STATUS)) \
            .select_assigned_to(
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_IMPORT_LEAD,
                                           LeadsModuleConstants.THIRD_ASSIGNED_TO)) \
            .perform_scroll_down() \
            .click_next_button()

        confirm_import_message = import_page.get_confirm_message_upload_lead()

        assert confirm_import_message == LeadsModuleConstants.CONFIRM_MESSAGE

        CRMHomePage().open_lead_module() \
            .open_today_lead_tab() \
            .get_import_lead(LeadsModuleConstants.LAST_IMPORT_NAME_LEAD) \
            .perform_screen_shot_confirm_import_lead_module() \
            .select_leads() \
            .click_delete_button()
