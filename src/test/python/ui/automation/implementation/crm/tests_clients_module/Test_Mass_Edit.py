import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=7)
class MassEditTestCRM(BaseTest):

    def test_make_mass_edit(self):
        crm_clients_module_page = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .perform_searching(Config.data.get_data_first_client(CRMConstants.CLIENT_STATUS),
                               Config.data.get_data_first_client(CRMConstants.SHORT_E_MAIL),
                               Config.data.get_data_first_client(CRMConstants.SHORT_CLIENT_NAME),
                               Config.data.get_data_first_client(TestDataConstants.FIRST_COUNTRY),
                               Config.data.get_data_first_client(CRMConstants.SHORT_FIRST_NAME),
                               Config.data.get_data_first_client(CRMConstants.SHORT_LAST_NAME),
                               Config.data.get_data_first_client(TestDataConstants.CITY),
                               Config.data.get_data_first_client(CRMConstants.BRAND_NEW_FOREX))

        first_client = crm_clients_module_page.get_first_client_email()
        crm_clients_module_page.came_back_on_previous_page().click_search_button()
        second_client = crm_clients_module_page.get_second_client_email()
        crm_clients_module_page.came_back_on_previous_page().click_search_button()
        third_client = crm_clients_module_page.get_third_client_email()
        crm_clients_module_page.came_back_on_previous_page().click_search_button()

        crm_clients_module_page.select_several_records() \
            .open_mass_edit_module() \
            .perform_mass_edit(Config.data.get_data_mass_edit(MassEditConstants.GENDER_FEMALE),
                               Config.data.get_data_mass_edit(MassEditConstants.ASSIGNED_TO_PANDA),
                               Config.data.get_data_mass_edit(MassEditConstants.CLIENT_SOURCE),
                               Config.data.get_data_mass_edit(MassEditConstants.COMPLIANCE_AGENT),
                               Config.data.get_data_mass_edit(MassEditConstants.COMPLIANCE_NOTES),
                               Config.data.get_data_mass_edit(MassEditConstants.CLIENT_STATUS),
                               Config.data.get_data_mass_edit(MassEditConstants.RETENTION_STATUS),
                               Config.data.get_data_mass_edit(MassEditConstants.DESCRIPTION),
                               Config.data.get_data_mass_edit(MassEditConstants.REFERRAL)) \
            .click_save()

        confirmation_message = crm_clients_module_page.get_confirm_message()
        assert confirmation_message == CRMConstants().MASS_EDIT
        crm_clients_module_page.click_ok()

        crm_client_profile = crm_clients_module_page.refresh() \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client_by_email(first_client)

        assert crm_client_profile.get_gender_text() == Config.data.get_data_mass_edit(
            MassEditConstants.GENDER_FEMALE)
        assert crm_client_profile.get_assigned_to_text() == Config.data.get_data_mass_edit(
            MassEditConstants.ASSIGNED_TO_PANDA)
        assert crm_client_profile.get_client_source_text() == Config.data.get_data_mass_edit(
            MassEditConstants.CLIENT_SOURCE)
        assert crm_client_profile.get_compliance_agent_text() == Config.data.get_data_mass_edit(
            MassEditConstants.COMPLIANCE_AGENT)
        assert crm_client_profile.get_compliance_notes_text() == Config.data.get_data_mass_edit(
            MassEditConstants.COMPLIANCE_NOTES)
        assert crm_client_profile.get_client_status_text() == Config.data.get_data_mass_edit(
            MassEditConstants.CLIENT_STATUS)
        assert crm_client_profile.get_retention_status_text() == Config.data.get_data_mass_edit(
            MassEditConstants.RETENTION_STATUS)
        assert crm_client_profile.get_description_text() == Config.data.get_data_mass_edit(
            MassEditConstants.DESCRIPTION)
        assert crm_client_profile.get_referral_text() == Config.data.get_data_mass_edit(
            MassEditConstants.REFERRAL)
