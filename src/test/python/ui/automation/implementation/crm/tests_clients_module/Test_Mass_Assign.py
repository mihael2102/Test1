import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=10)
class MassAssignTestCRM(BaseTest):

    def test_mass_assign(self):
        crm_client_profile = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.CLIENT_STATUS),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SHORT_E_MAIL),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                           CRMConstants.SHORT_CLIENT_NAME),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                           TestDataConstants.FIRST_COUNTRY),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SHORT_FIRST_NAME),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SHORT_LAST_NAME),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CITY),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.BRAND))

        crm_client_profile.select_three_records_clients_module() \
            .open_mass_assign_module() \
            .search_user(MassEditConstants.USER_ONE) \
            .enter_check_box() \
            .click_save()

        confirmation_message = crm_client_profile.get_confirm_message()
        assert confirmation_message == CRMConstants().MASS_ASSIGN_MESSAGE
        crm_client_profile.click_ok()
