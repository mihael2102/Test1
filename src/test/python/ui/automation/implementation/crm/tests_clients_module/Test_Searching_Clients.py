from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


class SearchingClientsTestCRM(BaseTest):

    def test_make_searching_client_module(self):
        crm_client_profile = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.CLIENT_STATUS),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                           CRMConstants.SHORT_CLIENT_NAME),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                           TestDataConstants.SECOND_COUNTRY),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SHORT_FIRST_NAME),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SHORT_LAST_NAME),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CITY),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.BRAND)) \
            .open_client_id()

        first_name_crm = crm_client_profile.get_first_name()
        last_name_crm = crm_client_profile.get_last_name()
        email = crm_client_profile.get_email_text()

        assert Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME) == first_name_crm
        assert Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.LAST_NAME) == last_name_crm
        assert Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL) == email
