import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.password.MT4CheckPasswordModule import MT4CheckPasswordModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=4)
class CheckPasswordTestCRM(BaseTest):

    def test_check_password_crm(self):
        crm_client_profile = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.E_MAIL))

        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.CHECK_PASSWORD)

        MT4CheckPasswordModule().select_account(account_number) \
            .enter_password(Config.data.get_data_client(TestDataConstants.PASSWORD)) \
            .click_check_button()

        message = crm_client_profile.get_confirm_message()
        crm_client_profile.click_ok()

        assert message == CRMConstants.PASSWORD_MESSAGE
