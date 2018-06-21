from src.main.python.ui.brand.model.client_area_modules.account_details.CaAccountDetails import CaAccountDetails
from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.forms.login.BrandLoginForm import BrandLoginForm
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.brand.model.pages.trading_platform.BrandTradingPlatformPage import BrandTradingPlatformPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants

class ChangePasswordTestCA(BaseTest):

    def test_change_password_from_ca(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.ACCOUNT_DETAILS)

        client_details_page = CaAccountDetails().open_change_password_tab() \
            .perform_change_password(Config.data.get_data_first_client(TestDataConstants.PASSWORD),
                                     Config.data.get_data_first_client(TestDataConstants.NEW_PASSWORD))

        password_changed_message = client_details_page.get_password_changed()

        assert password_changed_message == CaConstants.PASSWORD_SUCCESSFUL_CHANGED

        client_details_page.refreshing_wait().close_client_area_pop_up()

        BrandTradingPlatformPage().open_drop_down_menu() \
            .select_module(CaConstants.SIGN_OUT)

        invalid_login_message = BrandHomePage().login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button_with_invalid_password() \
            .get_invalid_login_message()

        assert invalid_login_message == CaConstants.INVALID_LOGIN_MESSAGE

        BrandLoginForm().set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                                    Config.data.get_data_first_client(TestDataConstants.NEW_PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.ACCOUNT_DETAILS)

        password_changed_message = CaAccountDetails().open_change_password_tab() \
            .perform_change_password(Config.data.get_data_first_client(TestDataConstants.NEW_PASSWORD),
                                     Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .get_password_changed()

        assert password_changed_message == CaConstants.PASSWORD_SUCCESSFUL_CHANGED
