import pytest

from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.pages.trading_accounts_information.TradingAccountsInformationPage import \
    TradingAccountsInformationPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=5)
class AddDemoAccountsTestCA(BaseTest):

    def test_check_add_demo_account_usd_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        brand_accounts_module = CaManageAccounts() \
            .open_demo_button() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_USD)) \
            .set_initial_deposit(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.INITIAL_DEPOSIT_FIRST)) \
            .create_account_button()

        account_id_ca = brand_accounts_module.get_account_id_text()
        usd_currency_ca = brand_accounts_module.get_account_currency_text()
        balance_ca = brand_accounts_module.get_deposit_balance()

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

        trading_accounts_info = TradingAccountsInformationPage()

        usd_currency_crm = trading_accounts_info.get_currency_text()
        balance_crm = trading_accounts_info.get_balance_text()

        assert account_id_ca == account_id_crm
        assert usd_currency_ca == usd_currency_crm
        assert balance_ca == balance_crm

    def test_check_add_demo_account_eur_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        brand_accounts_module = CaManageAccounts() \
            .open_demo_button() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_EUR)) \
            .set_initial_deposit(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.INITIAL_DEPOSIT_SECOND)) \
            .create_account_button()

        account_id_ca = brand_accounts_module.get_account_id_text()
        eur_currency_ca = brand_accounts_module.get_account_currency_text()
        balance_ca = brand_accounts_module.get_deposit_balance()

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

        trading_accounts_info = TradingAccountsInformationPage()

        eur_currency_crm = trading_accounts_info.get_currency_text()
        balance_crm = trading_accounts_info.get_balance_text()

        assert account_id_ca == account_id_crm
        assert eur_currency_ca == eur_currency_crm
        assert balance_ca == balance_crm

    def test_check_add_demo_account_gbr_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        brand_accounts_module = CaManageAccounts() \
            .open_demo_button() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_GBR)) \
            .set_initial_deposit(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.INITIAL_DEPOSIT_THIRD)) \
            .create_account_button()

        account_id_ca = brand_accounts_module.get_account_id_text()
        gbr_currency_ca = brand_accounts_module.get_account_currency_text()
        balance_ca = brand_accounts_module.get_deposit_balance()

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

        trading_accounts_info = TradingAccountsInformationPage()

        gbr_currency_crm = trading_accounts_info.get_currency_text()
        balance_crm = trading_accounts_info.get_balance_text()

        assert account_id_ca == account_id_crm
        assert gbr_currency_ca == gbr_currency_crm
        assert balance_ca == balance_crm

    def test_check_add_demo_account_cad_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        brand_accounts_module = CaManageAccounts() \
            .open_demo_button() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_CAD)) \
            .set_initial_deposit(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.INITIAL_DEPOSIT_FOURTH)) \
            .create_account_button()

        account_id_ca = brand_accounts_module.get_account_id_text()
        cad_currency_ca = brand_accounts_module.get_account_currency_text()
        balance_ca = brand_accounts_module.get_deposit_balance()

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

        trading_accounts_info = TradingAccountsInformationPage()
        cad_currency_crm = trading_accounts_info.get_currency_text()
        balance_crm = trading_accounts_info.get_balance_text()

        assert account_id_ca == account_id_crm
        assert cad_currency_ca == cad_currency_crm
        assert balance_ca == balance_crm
