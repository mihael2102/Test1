from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import \
    TradingAccountPrecondition


class TradingAccountTest(BaseTest):

    def test_check_tab_trading_account_module(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        trading_accounts_module = CRMHomePage().open_trading_account_module()

        show_all_tab_name = trading_accounts_module.get_show_all_tab_text()
        balance_above_zero_name = trading_accounts_module.get_balance_above_zero_tab_text()
        balance_below_zero_name = trading_accounts_module.get_balance_below_zero_tab_text()
        demo_trading_accounts_name = trading_accounts_module.get_demo_trading_accounts_tab_text()
        live_trading_account_name = trading_accounts_module.get_live_trading_account_tab_text()

        assert show_all_tab_name == Config.data.get_data_tabs_trading_module(TradingAccountConstants.FIRST_TAB)
        assert balance_above_zero_name == Config.data.get_data_tabs_trading_module(TradingAccountConstants.SECOND_TAB)
        assert balance_below_zero_name == Config.data.get_data_tabs_trading_module(TradingAccountConstants.THIRD_TAB)
        assert demo_trading_accounts_name == Config.data.get_data_tabs_trading_module(
            TradingAccountConstants.FOURTH_TAB)
        assert live_trading_account_name == Config.data.get_data_tabs_trading_module(TradingAccountConstants.FIFTH_TAB)

    def test_searching_trading_account_module(self):
        # TradingAccountPrecondition().make_deposit()
        crm_client_profile = CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        client_account_detail_view = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_client_account()

        trading_account = client_account_detail_view.get_account_text()
        server_text = client_account_detail_view.get_server_to_text()
        # brand_text = client_account_detail_view.get_brand_text()
        currency_text = client_account_detail_view.get_currency_text()
        balance_text = client_account_detail_view.get_balance_text()
        equity_text = client_account_detail_view.get_equity_text()
        assigned_text = client_account_detail_view.get_assigned_to_text()

        trading_accounts_module = CRMHomePage().open_trading_account_module() \
            .select_filter(Config.data.get_data_columns_trading_module(TradingAccountConstants.FILTER_NAME)) \
            .perform_searching_trading_account(trading_account, server_text, currency_text,
                                               balance_text, equity_text, assigned_text) \
            .open_client_login(trading_account)

        assert trading_accounts_module.get_account_text() == trading_account
        assert trading_accounts_module.get_server_to_text() == server_text
        assert trading_accounts_module.get_currency_text() == currency_text
        assert trading_accounts_module.get_balance_text() == balance_text
        assert trading_accounts_module.get_equity_text() == equity_text
        assert trading_accounts_module.get_assigned_to_text() == assigned_text
