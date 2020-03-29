from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage
from src.main.python.ui.ca.model.pages.login.CAPage import CAPage
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.trading_ui.TradingDetailsPageUI import TradingDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.pages.trading_ui.TradingModulePageUI import TradingModulePageUI


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
                                   CAConstants.EMAIL_CA)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Check if demo account and crypto position was opened """
        try:
            assert TradingConstants.IS_DEMO_EXIST == "yes" and \
                   TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            if TradingConstants.IS_DEMO_EXIST == "no":
                Logging().reportDebugStep(self, "There is no DEMO account")
                Logging().reportDebugStep(self, "NOT RUNNED")
                assert TradingConstants.IS_DEMO_EXIST == "yes"
            elif TradingConstants.IS_ASSET_EXIST == "no":
                Logging().reportDebugStep(self, "There is no crypto assets")
                Logging().reportDebugStep(self, "NOT RUNNED")
                assert TradingConstants.IS_ASSET_EXIST == "yes"

        """ Open demo account details and get open orders data """
        ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        TradingModulePageUI(self.driver)\
            .click_on_ta_number(CAConstants.DEMO_ACCOUNT_NUMBER)
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
