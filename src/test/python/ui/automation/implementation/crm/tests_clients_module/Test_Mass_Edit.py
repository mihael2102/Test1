import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=8)
class MassEditTestCRM(BaseTest):

    def test_clients_mass_edit(self):

        crm_clients_module_page = CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching_by_email(CRMConstants.SHORT_EMAIL)\
            .click_search_button()


        first_client = crm_clients_module_page.open_client_id().get_email_text()
        crm_clients_module_page.came_back_on_previous_page().click_search_button()
        crm_clients_module_page.select_three_records_clients_module() \
            .open_mass_edit_module() \
            .perform_mass_edit(self.config.get_data_mass_edit(MassEditConstants.GENDER_FEMALE),
                               self.config.get_data_mass_edit(MassEditConstants.ASSIGNED_TO_PANDA),
                               # self.config.get_data_mass_edit(MassEditConstants.CLIENT_SOURCE),
                               # self.config.get_data_mass_edit(MassEditConstants.COMPLIANCE_AGENT),
                               # self.config.get_data_mass_edit(MassEditConstants.COMPLIANCE_NOTES),
                               # self.config.get_data_mass_edit(MassEditConstants.CLIENT_STATUS),
                               # self.config.get_data_mass_edit(MassEditConstants.RETENTION_STATUS),
                               # self.config.get_data_mass_edit(MassEditConstants.DESCRIPTION),
                               self.config.get_data_mass_edit(MassEditConstants.REFERRAL)) \

        # confirmation_message = crm_clients_module_page.get_confirm_message()
        # assert confirmation_message == CRMConstants.MASS_EDIT
        # crm_clients_module_page.click_ok()

        crm_client_profile = crm_clients_module_page.refresh() \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(first_client)

        assert crm_client_profile.get_gender_text() == self.config.get_data_mass_edit(
            MassEditConstants.GENDER_FEMALE)
        assert crm_client_profile.get_assigned_to_text() == self.config.get_data_mass_edit(
            MassEditConstants.ASSIGNED_TO_PANDA)
        # assert crm_client_profile.get_client_source_text() == self.config.get_data_mass_edit(
        #     MassEditConstants.CLIENT_SOURCE)
        # assert crm_client_profile.get_compliance_agent_text() == Config.data.get_data_mass_edit(
        #     MassEditConstants.COMPLIANCE_AGENT)
        # assert crm_client_profile.get_compliance_notes_text() == Config.data.get_data_mass_edit(
        #     MassEditConstants.COMPLIANCE_NOTES)
        # assert crm_client_profile.get_client_status_text() == Config.data.get_data_mass_edit(
        #     MassEditConstants.CLIENT_STATUS)
        # assert crm_client_profile.get_retention_status_text() == Config.data.get_data_mass_edit(
        #     MassEditConstants.RETENTION_STATUS)
        # assert crm_client_profile.get_description_text() == Config.data.get_data_mass_edit(
        #     MassEditConstants.DESCRIPTION)
        assert crm_client_profile.get_referral_text() == self.config.get_data_mass_edit(
            MassEditConstants.REFERRAL)
