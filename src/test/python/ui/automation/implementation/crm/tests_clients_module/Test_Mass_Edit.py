import pytest
from src.main.python.ui.crm.model.constants.EditClientConstants import EditClientConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.client_profile.ClientProfileUpdate import ClientProfileUpdate
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.DragonConstants import DragonConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage


@pytest.mark.run(order=8)
class MassEditTestCRM(BaseTest):

    def setUp(self):
        super(MassEditTestCRM, self).setUp()
        self.lead1 = self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)
        self.lead2 = self.load_lead_from_config(LeadsModuleConstants.SECOND_LEAD_INFO)
        self.client1 = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def test_clients_mass_edit(self):
        crm_clients_module_page = CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching_by_email(CRMConstants.SHORT_EMAIL)

        first_client = crm_clients_module_page.open_client_id().get_email_text()
        crm_clients_module_page.came_back_on_previous_page()
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))
        ClientsPage(self.driver) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching_by_email(CRMConstants.SHORT_EMAIL)
        crm_clients_module_page\
            .select_three_records_clients_module() \
            .open_mass_edit_module() \
            .perform_mass_edit(self.config.get_data_mass_edit(MassEditConstants.ASSIGNED_TO_PANDA),
                               self.config.get_data_mass_edit(MassEditConstants.CLIENT_SOURCE)) \

        crm_client_profile = crm_clients_module_page.refresh() \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(first_client)

        assert crm_client_profile.get_assigned_to_text() == self.config.get_data_mass_edit(
            MassEditConstants.ASSIGNED_TO_PANDA)
        assert crm_client_profile.get_client_source_text() == self.config.get_data_mass_edit(
            MassEditConstants.CLIENT_SOURCE)

    def test_update_client_details(self):
        # Login to CRM, find client:
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        # Edit client:
        ClientProfileUpdate(self.driver) \
            .click_edit_client_button() \
            .edit_first_name(EditClientConstants.FIRST_NAME_UPDATE) \
            .edit_city(EditClientConstants.CITY_UPDATE) \
            .edit_country(EditClientConstants.COUNTRY_UPDATE) \
            .click_save()

        # Verify First Name field was updated:
        assert ClientProfilePage(self.driver).get_first_name() == EditClientConstants.FIRST_NAME_UPDATE

        # Verify City field was updated:
        ClientProfilePage(self.driver).open_address_information()
        assert ClientProfilePage(self.driver).get_city_text() == EditClientConstants.CITY_UPDATE

        # Verify Country field was updated:
        assert ClientProfilePage(self.driver).get_country_text() == EditClientConstants.COUNTRY_UPDATE

        # Verify other fields was not changed:
        assert ClientProfilePage(self.driver).get_last_name() == self.client1[LeadsModuleConstants.FIRST_LAST_NAME]
        try:
            assert ClientProfilePage(self.driver).get_email_text() == self.client1[LeadsModuleConstants.EMAIL]
        except:
            assert ClientProfilePage(self.driver).get_email_text() == DragonConstants.EMAIL_VALID_DETAIL_VIEW
        phone = ClientProfilePage(self.driver).get_phone_text()
        phone = phone.replace(' ', '').replace('+', '')
        if phone:
            try:
                assert self.client1[LeadsModuleConstants.PHONE] in phone
            except:
                assert DragonConstants.PHONE_NUMBER_HIDDEN in phone
