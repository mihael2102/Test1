import pytest

from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsInformationPage import \
    TradingAccountsInformationPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import TradingAccountPrecondition


@pytest.mark.run(order=5)
class AddNewAccountTestCA(BaseTest):

    def test_add_live_account_ca(self):

        TradingAccountPrecondition(self.driver, self.config).add_live_account()

    def test_add_demo_account_ca(self):

        TradingAccountPrecondition(self.driver, self.config).add_demo_account()

    def test_verify_accounts_in_crm(self):

        TradingAccountPrecondition(self.driver, self.config).verify_account_in_crm()


    # def test_check_add_live_account_eur_currency(self):
    #     BrandHomePage().open_first_tab_page(self.config.get_value('url_ca')).login() \
    #         .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
    #                     Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
    #         .click_login_button() \
    #         .open_drop_down_menu() \
    #         .select_module(CaConstants.MANAGE_ACCOUNTS)
    #
    #     brand_manage_accounts = CaManageAccounts() \
    #         .open_new_account_button() \
    #         .select_account_currency(
    #         Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_EUR)) \
    #         .create_account_button()
    #
    #     account_id_ca = brand_manage_accounts.get_account_id_text()
    #     eur_currency_ca = brand_manage_accounts.get_account_currency_text()
    #
    #     crm_client_profile = CRMLoginPage() \
    #         .open_second_tab_page(self.config.get_value('url')) \
    #         .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
    #                    self.config.get_value(TestDataConstants.CRM_PASSWORD),
    #                    self.config.get_value(TestDataConstants.OTP_SECRET)) \
    #         .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
    #         .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
    #
    #     account_id_crm = crm_client_profile \
    #         .perform_scroll_down() \
    #         .open_trading_accounts_tab() \
    #         .open_client_account_by_account_id(account_id_ca) \
    #         .get_account_text()
    #
    #     eur_currency_crm = TradingAccountsInformationPage().get_currency_text()
    #
    #     assert account_id_ca == account_id_crm
    #     assert eur_currency_ca == eur_currency_crm
    #
    # def test_check_add_live_account_gbr_currency(self):
    #     BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
    #         .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
    #                     Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
    #         .click_login_button() \
    #         .open_drop_down_menu() \
    #         .select_module(CaConstants.MANAGE_ACCOUNTS)
    #
    #     brand_manage_accounts = CaManageAccounts() \
    #         .open_new_account_button() \
    #         .select_account_currency(
    #         Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_GBR)) \
    #         .create_account_button()
    #
    #     account_id_ca = brand_manage_accounts.get_account_id_text()
    #     gbr_currency_ca = brand_manage_accounts.get_account_currency_text()
    #
    #     crm_client_profile = CRMLoginPage() \
    #         .open_second_tab_page(self.config.get_value('url')) \
    #         .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
    #                    self.config.get_value(TestDataConstants.CRM_PASSWORD),
    #                    self.config.get_value(TestDataConstants.OTP_SECRET)) \
    #         .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
    #         .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
    #
    #     account_id_crm = crm_client_profile \
    #         .perform_scroll_down() \
    #         .open_trading_accounts_tab() \
    #         .open_client_account_by_account_id(account_id_ca) \
    #         .get_account_text()
    #
    #     gbr_currency_crm = TradingAccountsInformationPage().get_currency_text()
    #
    #     assert account_id_ca == account_id_crm
    #     assert gbr_currency_ca == gbr_currency_crm
    #
    # def test_check_add_live_account_cad_currency(self):
    #     BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
    #         .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
    #                     Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
    #         .click_login_button() \
    #         .open_drop_down_menu() \
    #         .select_module(CaConstants.MANAGE_ACCOUNTS)
    #
    #     brand_manage_accounts = CaManageAccounts() \
    #         .open_new_account_button() \
    #         .select_account_currency(
    #         Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_CAD)) \
    #         .create_account_button()
    #
    #     account_id_ca = brand_manage_accounts.get_account_id_text()
    #     cad_currency__ca = brand_manage_accounts.get_account_currency_text()
    #
    #     crm_client_profile = CRMLoginPage() \
    #         .open_second_tab_page(self.config.get_value('url')) \
    #         .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
    #                    self.config.get_value(TestDataConstants.CRM_PASSWORD),
    #                    self.config.get_value(TestDataConstants.OTP_SECRET)) \
    #         .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
    #         .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
    #
    #     account_id_crm = crm_client_profile \
    #         .perform_scroll_down() \
    #         .open_trading_accounts_tab() \
    #         .open_client_account_by_account_id(account_id_ca) \
    #         .get_account_text()
    #
    #     cad_currency_crm = TradingAccountsInformationPage().get_currency_text()
    #
    #     assert account_id_ca == account_id_crm
    #     assert cad_currency__ca == cad_currency_crm
    #
    # def test_check_add_live_account_jpy_currency(self):
    #     BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
    #         .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
    #                     Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
    #         .click_login_button() \
    #         .open_drop_down_menu() \
    #         .select_module(CaConstants.MANAGE_ACCOUNTS)
    #
    #     brand_manage_accounts = CaManageAccounts() \
    #         .open_new_account_button() \
    #         .select_account_currency(
    #         Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_JPY)) \
    #         .create_account_button()
    #
    #     account_id_ca = brand_manage_accounts.get_account_id_text()
    #     jpy_currency__ca = brand_manage_accounts.get_account_currency_text()
    #
    #     crm_client_profile = CRMLoginPage() \
    #         .open_second_tab_page(self.config.get_value('url')) \
    #         .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
    #                    self.config.get_value(TestDataConstants.CRM_PASSWORD),
    #                    self.config.get_value(TestDataConstants.OTP_SECRET)) \
    #         .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
    #         .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
    #
    #     account_id_crm = crm_client_profile \
    #         .perform_scroll_down() \
    #         .open_trading_accounts_tab() \
    #         .open_client_account_by_account_id(account_id_ca) \
    #         .get_account_text()
    #
    #     jpy_currency_crm = TradingAccountsInformationPage().get_currency_text()
    #
    #     assert account_id_ca == account_id_crm
    #     assert jpy_currency__ca == jpy_currency_crm
