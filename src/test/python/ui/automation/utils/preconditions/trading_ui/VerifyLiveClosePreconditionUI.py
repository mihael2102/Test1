from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.trading_ui.TradingDetailsConstantsUI import TradingDetailsConstantsUI
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskEditPage import HelpDeskEditPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.constants.ClientDetailsConstants import ClientDetailsConstants
from src.main.python.ui.crm.model.pages.trading_ui.TradingDetailsPageUI import TradingDetailsPageUI
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants


class VerifyLiveClosePreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def verify_close_live_position_crm_ui(self):
        """ Login CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))
        CRMHomePage(self.driver) \
            .open_client_module_new_ui() \
            .select_filter_new_ui(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email_new_ui(self.config.get_value('email_live_acc'))

        """ Check if crypto position was opened """
        try:
            assert TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            Logging().reportDebugStep(self, "There is no crypto assets")
            assert TradingConstants.IS_ASSET_EXIST == "yes"

        """ Open live account details and get closed orders data """
        ClientProfilePage(self.driver) \
            .open_tab(ClientDetailsConstants.TRADING_ACCOUNTS_TAB) \
            .open_trading_account_by_number(self.config.get_value('number_live_acc'))
        GlobalDetailsPageUI(self.driver) \
            .open_tab_ui(TradingDetailsConstantsUI.TAB_CLOSED_TRANSACTIONS)

        close_orders_data = TradingDetailsPageUI(self.driver) \
            .get_closed_orders_data_ui()

        """ Verify data of closed trade: """
        expected_order_id = TradingConstants.ORDER_ID_CLOSED.replace('#', '')
        expected_created_time_order = TradingConstants.CLOSED_ORDER_CREATED_TIME.split(' ')
        expected_date = expected_created_time_order[0].split('/')
        expected_date = expected_date[2] + "-" + expected_date[1] + "-" + expected_date[0]
        expected_time = expected_created_time_order[1]
        expected_symbol = TradingConstants.CLOSED_ORDER_SYMBOL
        expected_open_price = TradingConstants.CLOSED_ORDER_OPEN_PRICE
        while expected_open_price.endswith('0'):
            expected_open_price = expected_open_price[:-1]
        expected_closed_time_order = TradingConstants.CLOSED_ORDER_CLOSED_TIME.split(' ')
        expected_closed_order_date = expected_closed_time_order[0].split('/')
        expected_closed_order_date = expected_closed_order_date[2] + "-" + expected_closed_order_date[1] + "-" \
                                     + expected_closed_order_date[0]
        expected_closed_order_time = expected_closed_time_order[1]
        expected_closed_price = TradingConstants.CLOSED_ORDER_CLOSED_PRICE
        while expected_closed_price.endswith('0'):
            expected_closed_price = expected_closed_price[:-1]
        expected_profit = TradingConstants.CLOSED_ORDER_PROFIT.replace('€', '')
        expected_profit = expected_profit.replace('BTC: ', '')
        expected_profit = expected_profit.replace('$', '')

        assert expected_order_id in close_orders_data
        assert expected_date in close_orders_data
        assert expected_time in close_orders_data
        assert expected_symbol in close_orders_data
        assert expected_open_price in close_orders_data
        assert expected_closed_order_date in close_orders_data
        assert expected_closed_order_time in close_orders_data
        assert expected_closed_price in close_orders_data
        assert expected_profit in close_orders_data
