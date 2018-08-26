import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=3)
class SearchingClientsTestCRM(BaseTest):

    def test_make_searching_client_module(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_data_client(TestDataConstants.USER_NAME),
                       self.config.get_data_client(TestDataConstants.CRM_PASSWORD),
                       self.config.get_data_client(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching(self.config.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.CLIENT_STATUS),
                               self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                               self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                           CRMConstants.SHORT_CLIENT_NAME),
                               self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                           TestDataConstants.FIRST_COUNTRY),
                               self.config.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SHORT_FIRST_NAME),
                               self.config.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SHORT_LAST_NAME),
                               self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CITY),
                               self.config.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.BRAND))

        # TODO: verify that only one client was found

        crm_client_profile.perform_scroll_up()
        crm_client_profile = crm_client_profile.open_client_id()

        first_name_crm = crm_client_profile.get_first_name()
        last_name_crm = crm_client_profile.get_last_name()
        email = crm_client_profile.get_email_text()

        assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME) == first_name_crm
        assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.LAST_NAME) == last_name_crm
        assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL) == email
