import pytest

from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.sign_up.BrandSignUpPrecondition import BrandSignUpPrecondition
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=1)
class SignUpTest(BaseTest):

    def test_check_sign_up(self):
        BrandSignUpPrecondition() \
            .perform_first_step() \
            .perform_second_step()

        crm_login_page = CRMLoginPage()
        crm_client_profile = crm_login_page \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_first_client(TestDataConstants.E_MAIL))

        assert crm_client_profile.get_client_status() == "Live"
