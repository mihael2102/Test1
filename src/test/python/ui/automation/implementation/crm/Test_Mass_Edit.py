from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class MassEditTestCRM(BaseTest):

    def test_make_mass_edit(self):
        crm_client_profile = CRMLoginPage() \
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

        crm_client_profile.select_several_records()


