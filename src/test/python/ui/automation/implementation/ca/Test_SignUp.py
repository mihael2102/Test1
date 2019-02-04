import pytest

from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.sign_up.BrandSignUpPrecondition import BrandSignUpPrecondition
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import Login_CA_Precondition

@pytest.mark.run(order=2)
class SignUpTest(BaseTest):

    def test_check_sign_up(self):

        Login_CA_Precondition(self.driver, self.config).sign_up_ca()

    def test_registred_client_exist_in_crm(self):
        Login_CA_Precondition(self.driver, self.config).client_exist_in_crm()

        # BrandSignUpPrecondition() \
        #     .perform_first_step() \
        #     .perform_second_step()
        #
        # crm_login_page = CRMLoginPage()
        # crm_client_profile = crm_login_page \
        #     .open_second_tab_page(Config.url_crm) \
        #     .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
        #                self.config.get_value(TestDataConstants.CRM_PASSWORD),
        #                self.config.get_value(TestDataConstants.OTP_SECRET)) \
        #     .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
        #     .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
        #
        # assert crm_client_profile.get_live_status_client() == "Live"
