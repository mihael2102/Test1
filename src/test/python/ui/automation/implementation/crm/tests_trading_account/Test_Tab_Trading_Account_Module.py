import pytest

from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *


@pytest.mark.run(order=34)
class TradingAccountTest(BaseTest):

    def test_check_tab_trading_account_module(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_trading_account_module()

        show_all_tab_name = task_module.get_show_all_tab_text()
        balance_above_zero_name = task_module.get_balance_above_zero_tab_text()
        balance_below_zero_name = task_module.get_balance_below_zero_tab_text()
        demo_trading_accounts_name = task_module.get_demo_trading_accounts_tab_text()
        live_trading_account_name = task_module.get_live_trading_account_tab_text()

        assert show_all_tab_name == Config.data.get_data_tabs_trading_module(TradingAccountConstants.FIRST_TAB)
        assert balance_above_zero_name == Config.data.get_data_tabs_trading_module(TradingAccountConstants.SECOND_TAB)
        assert balance_below_zero_name == Config.data.get_data_tabs_trading_module(TradingAccountConstants.THIRD_TAB)
        assert demo_trading_accounts_name == Config.data.get_data_tabs_trading_module(
            TradingAccountConstants.FOURTH_TAB)
        assert live_trading_account_name == Config.data.get_data_tabs_trading_module(TradingAccountConstants.FIFTH_TAB)
