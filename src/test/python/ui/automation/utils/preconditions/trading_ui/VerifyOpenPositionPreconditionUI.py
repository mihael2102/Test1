from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage
from src.main.python.ui.ca.model.pages.login.CAPage import CAPage
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.constants.ClientDetailsConstants import ClientDetailsConstants
from src.main.python.ui.crm.model.pages.trading_ui.TradingDetailsPageUI import TradingDetailsPageUI


class VerifyOpenPositionPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def verify_open_position_crm_ui(self):
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
            .find_client_by_email_new_ui(CAConstants.EMAIL_CA)

        """ Check if demo account and crypto position was opened """
        try:
            assert TradingConstants.IS_DEMO_EXIST == "yes" and \
                   TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            if TradingConstants.IS_DEMO_EXIST == "no":
                Logging().reportDebugStep(self, "There is no DEMO account")
                assert TradingConstants.IS_DEMO_EXIST == "yes"
            elif TradingConstants.IS_ASSET_EXIST == "no":
                Logging().reportDebugStep(self, "There is no crypto assets")
                assert TradingConstants.IS_ASSET_EXIST == "yes"

        """ Open demo account details and get open orders data """
        ClientProfilePage(self.driver) \
            .open_tab(ClientDetailsConstants.TRADING_ACCOUNTS_TAB) \
            .open_trading_account_by_number(CAConstants.DEMO_ACCOUNT_NUMBER)
        open_orders_data = TradingDetailsPageUI(self.driver) \
            .display_open_trades()\
            .get_open_orders_data()

        expected_order_id = TradingConstants.ORDER_ID_OPEN.replace('#', '')
        expected_created_time_order = TradingConstants.ORDER_CREATED_TIME.split(' ')
        expected_date = expected_created_time_order[0].split('/')
        expected_date = "20" + expected_date[2] + "-" + expected_date[1] + "-" + expected_date[0]
        expected_time = expected_created_time_order[1]
        expected_symbol = TradingConstants.ORDER_SYMBOL
        expected_open_price = TradingConstants.ORDER_OPEN_PRICE

        assert expected_order_id in open_orders_data
        assert expected_date in open_orders_data
        assert expected_time in open_orders_data
        assert expected_symbol in open_orders_data
        assert expected_open_price in open_orders_data
