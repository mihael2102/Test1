from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class SearchingClientsTestCRM(BaseTest):

    def test_make_searching_client_module(self):
        crm_client_profile = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(TestDataConstants.CLIENT_ONE, Config.data.get_data_client(TestDataConstants.USER_NAME),
                       TestDataConstants.CLIENT_ONE, Config.data.get_data_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.FILTER)) \
            .perform_searching(Config.data.get_data_client(CRMConstants.CLIENT_STATUS),
                               Config.data.get_data_client(TestDataConstants.E_MAIL),
                               Config.data.get_data_client(CRMConstants.SHORT_CLIENT_NAME),
                               Config.data.get_data_client(TestDataConstants.FIRST_COUNTRY),
                               Config.data.get_data_client(CRMConstants.SHORT_FIRST_NAME),
                               Config.data.get_data_client(CRMConstants.SHORT_LAST_NAME),
                               Config.data.get_data_client(TestDataConstants.CITY),
                               Config.data.get_data_client(CRMConstants.BRAND)) \
            .open_client_id()

        first_name_crm = crm_client_profile.get_first_name()
        last_name_crm = crm_client_profile.get_last_name()
        email = crm_client_profile.get_email_text()

        assert Config.data.get_data_client(TestDataConstants.FIRST_NAME) == first_name_crm
        assert Config.data.get_data_client(TestDataConstants.LAST_NAME) == last_name_crm
        assert Config.data.get_data_client(TestDataConstants.E_MAIL) == email
