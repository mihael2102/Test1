import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=10)
class MassAssignTestCRM(BaseTest):

    def test_mass_assign(self):
        crm_client_profile = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.FILTER)) \
            .perform_searching(Config.data.get_data_client(CRMConstants.CLIENT_STATUS),
                               Config.data.get_data_client(CRMConstants.SHORT_E_MAIL),
                               Config.data.get_data_client(CRMConstants.SHORT_CLIENT_NAME),
                               Config.data.get_data_client(TestDataConstants.FIRST_COUNTRY),
                               Config.data.get_data_client(CRMConstants.SHORT_FIRST_NAME),
                               Config.data.get_data_client(CRMConstants.SHORT_LAST_NAME),
                               Config.data.get_data_client(TestDataConstants.CITY),
                               Config.data.get_data_client(CRMConstants.BRAND_NEW_FOREX))

        crm_client_profile.select_three_records_clients_module() \
            .open_mass_assign_module() \
            .search_user(MassEditConstants.USER_ONE) \
            .enter_check_box() \
            .click_save()

        confirmation_message = crm_client_profile.get_confirm_message()
        assert confirmation_message == CRMConstants().MASS_ASSIGN_MESSAGE
        crm_client_profile.click_ok()
