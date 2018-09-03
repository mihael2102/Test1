import pytest

from src.main.python.ui.brand.model.ca_modules.CAModules import CAModules
from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.sign_up.BrandSignUpPrecondition import BrandSignUpPrecondition
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.utils.preconditions.withdraw_ca.CAWithdrawPrecondition import CAWithdrawPrecondition


class TestAngularLoading(BaseTest):

    def test_check_sign_up(self):
        CAWithdrawPrecondition() \
            .add_live_account() \
            .make_deposit()

        account_number = ClientProfilePage().get_client_account()

        account_number = "1237478"

        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)
    #
    #
    #     withdraw_status = CAModules() \
    #         .switch_first_tab_page() \
    #         .open_withdraw_page() \
    #         .perform_withdraw_first_step_request(account_number) \
    #         .perform_withdraw_second_step_request() \
    #         .click_withdraw_history_tab() \
    #         .select_account(account_number) \
    #         .get_status_request()


with open('D:\\automation-newforexqa\\src\\test\\python\\ui\\automation\\implementation\\ca\\js_waiter_for_selenium.txt', 'r') as content_file:
    content = content_file.read()

print(content)