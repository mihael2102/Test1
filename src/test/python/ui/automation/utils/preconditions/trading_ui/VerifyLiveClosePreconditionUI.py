from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.trading_ui.TradingDetailsConstantsUI import TradingDetailsConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.trading_ui.TradingDetailsPageUI import TradingDetailsPageUI
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.pages.trading_ui.TradingModulePageUI import TradingModulePageUI


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
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module and find created client by email """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   self.config.get_value('email_live_acc'))
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(row='1')

        """ Check if crypto position was opened """
        try:
            assert TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            Logging().reportDebugStep(self, "There is no crypto assets")
            Logging().reportDebugStep(self, "NOT RUNNED")
            assert TradingConstants.IS_ASSET_EXIST == "yes"

        """ Open live account details """
        ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        TradingModulePageUI(self.driver) \
            .click_on_ta_number(self.config.get_value('number_live_acc'))
        GlobalDetailsPageUI(self.driver) \
            .open_tab(TradingDetailsConstantsUI.TAB_CLOSED_TRANSACTIONS)

        """ Get last record number from Closed Trades table """
        record_number = GlobalModulePageUI(self.driver)\
            .get_last_record_number()
        record_number = str(int(record_number) - 1)

        """ Get last closed order data """
        close_orders_data = TradingDetailsPageUI(self.driver) \
            .get_closed_orders_data_ui(record_number)

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
        expected_profit = expected_profit.replace('₮', '')
        while expected_profit.endswith('0'):
            expected_profit = expected_profit[:-1]

        assert expected_order_id in close_orders_data
        assert expected_date in close_orders_data
        assert expected_time in close_orders_data
        assert expected_symbol in close_orders_data
        assert expected_open_price in close_orders_data
        assert expected_closed_order_date in close_orders_data
        assert expected_closed_order_time in close_orders_data
        assert expected_closed_price in close_orders_data
        assert expected_profit in close_orders_data
