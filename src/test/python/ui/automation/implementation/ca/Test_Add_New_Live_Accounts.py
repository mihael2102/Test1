import pytest

from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.pages.trading_accounts_information.TradingAccountsInformationPage import \
    TradingAccountsInformationPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=4)
class AddNewLiveAccountTestCA(BaseTest):

    def test_check_add_live_account_eur_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        brand_manage_accounts = CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_EUR)) \
            .create_account_button()

        account_id_ca = brand_manage_accounts.get_account_id_text()
        eur_currency_ca = brand_manage_accounts.get_account_currency_text()

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        account_id_crm = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_client_account(account_id_ca) \
            .get_account_text()

        eur_currency_crm = TradingAccountsInformationPage().get_currency_text()

        assert account_id_ca == account_id_crm
        assert eur_currency_ca == eur_currency_crm

    def test_check_add_live_account_gbr_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        brand_manage_accounts = CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_GBR)) \
            .create_account_button()

        account_id_ca = brand_manage_accounts.get_account_id_text()
        gbr_currency_ca = brand_manage_accounts.get_account_currency_text()

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        account_id_crm = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_client_account(account_id_ca) \
            .get_account_text()

        gbr_currency_crm = TradingAccountsInformationPage().get_currency_text()

        assert account_id_ca == account_id_crm
        assert gbr_currency_ca == gbr_currency_crm

    def test_check_add_live_account_cad_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        brand_manage_accounts = CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_CAD)) \
            .create_account_button()

        account_id_ca = brand_manage_accounts.get_account_id_text()
        cad_currency__ca = brand_manage_accounts.get_account_currency_text()

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        account_id_crm = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_client_account(account_id_ca) \
            .get_account_text()

        cad_currency_crm = TradingAccountsInformationPage().get_currency_text()

        assert account_id_ca == account_id_crm
        assert cad_currency__ca == cad_currency_crm

    def test_check_add_live_account_jpy_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        brand_manage_accounts = CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_JPY)) \
            .create_account_button()

        account_id_ca = brand_manage_accounts.get_account_id_text()
        jpy_currency__ca = brand_manage_accounts.get_account_currency_text()

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        account_id_crm = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_client_account(account_id_ca) \
            .get_account_text()

        jpy_currency_crm = TradingAccountsInformationPage().get_currency_text()

        assert account_id_ca == account_id_crm
        assert jpy_currency__ca == jpy_currency_crm
