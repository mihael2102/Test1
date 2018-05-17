from scr.main.python.ui.brand.model.client_area_modules.ca_constats.CaStatusConstants import CaStatusConstants
from scr.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from scr.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from scr.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from scr.main.python.ui.crm.model.pages.trading_accounts_information.CRMTradingAccountsInformationPage import \
    CRMTradingAccountsInformationPage
from scr.main.python.ui.results.actual_result.AddNewLiveAccountActualResult import AddNewLiveAccountActualResult
from scr.main.python.ui.results.expected_result.AddNewLiveAccountExpectedResult import AddNewLiveAccountExpectedResult
from scr.test.python.ui.avtomation.BaseTest import *
from scr.test.python.utils.TestDataConstants import TestDataConstants


class AddNewLiveAccount(BaseTest):

    def test_check_add_live_account_eur_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.MANAGE_ACCOUNTS)

        brand_manage_accounts = CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(Config.data.get_data_first_client(TestDataConstants.ACCOUNT_CURRENCY_EUR)) \
            .create_account_button()

        account_id_ca = brand_manage_accounts.get_account_id_text()
        eur_currency_ca = brand_manage_accounts.get_account_currency_text()

        AddNewLiveAccountActualResult().print_actual_result(account_id_ca, eur_currency_ca)

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                         Config.data.get_data_first_client(TestDataConstants.FIRST_NAME))

        account_id_crm = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_client_account(account_id_ca) \
            .get_account_text()

        eur_currency_crm = CRMTradingAccountsInformationPage().get_currency_text()
        AddNewLiveAccountExpectedResult().print_expected_result(account_id_crm, eur_currency_crm)

        assert account_id_ca == account_id_crm
        assert eur_currency_ca == eur_currency_crm

    def test_check_add_live_account_gbr_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.MANAGE_ACCOUNTS)

        brand_manage_accounts = CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(Config.data.get_data_first_client(TestDataConstants.ACCOUNT_CURRENCY_GBR)) \
            .create_account_button()

        account_id_ca = brand_manage_accounts.get_account_id_text()
        gbr_currency_ca = brand_manage_accounts.get_account_currency_text()

        AddNewLiveAccountActualResult().print_actual_result(account_id_ca, gbr_currency_ca)

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                         Config.data.get_data_first_client(TestDataConstants.FIRST_NAME))

        account_id_crm = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_client_account(account_id_ca) \
            .get_account_text()

        gbr_currency_crm = CRMTradingAccountsInformationPage().get_currency_text()
        AddNewLiveAccountExpectedResult().print_expected_result(account_id_crm, gbr_currency_crm)

        assert account_id_ca == account_id_crm
        assert gbr_currency_ca == gbr_currency_crm

    def test_check_add_live_account_cad_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.MANAGE_ACCOUNTS)

        brand_manage_accounts = CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(Config.data.get_data_first_client(TestDataConstants.ACCOUNT_CURRENCY_CAD)) \
            .create_account_button()

        account_id_ca = brand_manage_accounts.get_account_id_text()
        cad_currency__ca = brand_manage_accounts.get_account_currency_text()

        AddNewLiveAccountActualResult().print_actual_result(account_id_ca, cad_currency__ca)

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                         Config.data.get_data_first_client(TestDataConstants.FIRST_NAME))

        account_id_crm = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_client_account(account_id_ca) \
            .get_account_text()

        cad_currency_crm = CRMTradingAccountsInformationPage().get_currency_text()
        AddNewLiveAccountExpectedResult().print_expected_result(account_id_crm, cad_currency_crm)

        assert account_id_ca == account_id_crm
        assert cad_currency__ca == cad_currency_crm

    def test_check_add_live_account_jpy_currency(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.MANAGE_ACCOUNTS)

        brand_manage_accounts = CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(Config.data.get_data_first_client(TestDataConstants.ACCOUNT_CURRENCY_JPY)) \
            .create_account_button()

        account_id_ca = brand_manage_accounts.get_account_id_text()
        jpy_currency__ca = brand_manage_accounts.get_account_currency_text()

        AddNewLiveAccountActualResult().print_actual_result(account_id_ca, jpy_currency__ca)

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                         Config.data.get_data_first_client(TestDataConstants.FIRST_NAME))

        account_id_crm = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_client_account(account_id_ca) \
            .get_account_text()

        jpy_currency_crm = CRMTradingAccountsInformationPage().get_currency_text()
        AddNewLiveAccountExpectedResult().print_expected_result(account_id_crm, jpy_currency_crm)
        assert account_id_ca == account_id_crm
        assert jpy_currency__ca == jpy_currency_crm
