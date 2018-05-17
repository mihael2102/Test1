from scr.main.python.ui.brand.model.client_area_modules.account_details.CaAccountDetails import CaAccountDetails
from scr.main.python.ui.brand.model.client_area_modules.ca_constats.CaStatusConstants import CaStatusConstants
from scr.main.python.ui.brand.model.forms.login.BrandLoginForm import BrandLoginForm
from scr.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from scr.main.python.ui.brand.model.pages.trading_platform.BrandTradingPlatformPage import BrandTradingPlatformPageBrand
from scr.test.python.ui.avtomation.BaseTest import *
from scr.test.python.utils.TestDataConstants import TestDataConstants


class ChangePasswordFromCA(BaseTest):

    def test_change_password_from_ca(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.ACCOUNT_DETAILS)

        CaAccountDetails().open_change_password_tab() \
            .perform_change_password(Config.data.get_data_first_client(TestDataConstants.PASSWORD)
                                     , Config.data.get_data_first_client(TestDataConstants.NEW_PASSWORD)) \
            .refreshing_wait() \
            .close_client_area_pop_up() \

        BrandTradingPlatformPageBrand().open_drop_down_menu() \
            .select_module(CaStatusConstants.SIGN_OUT)

        invalid_login_message = BrandHomePage().login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button_with_invalid_password() \
            .get_invalid_login_message()

        assert invalid_login_message == CaStatusConstants.INVALID_LOGIN_MESSAGE

        BrandLoginForm().set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                                    Config.data.get_data_first_client(TestDataConstants.NEW_PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.ACCOUNT_DETAILS)

        password_changed = CaAccountDetails().open_change_password_tab() \
            .perform_change_password(Config.data.get_data_first_client(TestDataConstants.NEW_PASSWORD)
                                     , Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .get_password_changed()

        assert password_changed == CaStatusConstants.PASSWORD_SUCCESSFUL_CHANGED
