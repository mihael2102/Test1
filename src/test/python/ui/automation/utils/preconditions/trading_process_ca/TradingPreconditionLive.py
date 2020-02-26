from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


class TradingPreconditionLive(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def open_position_live(self):
        if global_var.current_brand_name == "q8":
            CALoginPage(self.driver)\
                .open_first_tab_page(self.config.get_value('url_ca'))
        else:
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver) \
            .close_campaign_banner() \
            .click_sign_in_btn() \
            .enter_email(self.config.get_value('email_live_acc'))\
            .enter_password(self.config.get_value('password_live_acc'))\
            .click_login()\
            .verify()

        if global_var.current_brand_name == "q8":
            self.driver.switch_to_frame(self.driver.find_element_by_xpath(
                "//iframe[@class='platform__mobile-platform']"))
        elif global_var.current_brand_name == "24option":
            self.driver.switch_to_frame(self.driver.find_element_by_xpath(
                "//iframe[@id='swPandaIframe']"))

        WebTraderPage(self.driver)\
            .open_trading_page()\
            .open_asset_group(TradingConstants.ASSET_GROUP_CRYPTO)\
            .select_asset(var.get_var(self.__class__.__name__)["asset"])\
            .select_volume_in_lot(TradingConstants.VOLUME_IN_LOT_001)\
            .click_buy()\
            .click_invest()\
            .get_msg_succsessfull_order()\
            .close_succsessfull_order_popup()\
            .open_trade_tab(TradingConstants.TRADES_TAB_OPEN_TRADES)\
            .get_id_order()\
            .get_order_created_time()\
            .get_symbol()\
            .get_open_price()

    def verify_open_live_position_crm(self):
        """ Login CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_value('email_live_acc'))

        """ Check if crypto position was opened """
        try:
            assert TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            Logging().reportDebugStep(self, "There is no crypto assets")
            Logging().reportDebugStep(self, "NOT RUNNED")
            assert TradingConstants.IS_ASSET_EXIST == "yes"

        """ Open live account details and get open orders data """
        open_orders_data = ClientProfilePage(self.driver) \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_trading_account_by_number(self.config.get_value('number_live_acc')) \
            .click_display_open_transactions() \
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

    def close_position_live(self):
        """ Log in CA """
        if global_var.current_brand_name == "q8":
            CALoginPage(self.driver)\
                .open_first_tab_page(self.config.get_value('url_ca'))
        else:
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver) \
            .close_campaign_banner() \
            .click_sign_in_btn() \
            .enter_email(self.config.get_value('email_live_acc'))\
            .enter_password(self.config.get_value('password_live_acc'))\
            .click_login()\
            .verify()

        """ Check if crypto position was opened """
        try:
            assert TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            Logging().reportDebugStep(self, "There is no crypto assets")
            Logging().reportDebugStep(self, "NOT RUNNED")
            assert TradingConstants.IS_ASSET_EXIST == "yes"

        if global_var.current_brand_name == "q8":
            self.driver.switch_to_frame(self.driver.find_element_by_xpath(
                "//iframe[@class='platform__mobile-platform']"))
        elif global_var.current_brand_name == "24option":
            self.driver.switch_to_frame(self.driver.find_element_by_xpath(
                "//iframe[@id='swPandaIframe']"))

        WebTraderPage(self.driver) \
            .open_trading_page() \
            .click_close_order() \
            .close_pop_up_close_trade(CRMConstants.YES) \
            .close_succsessfull_order_popup() \
            .open_trade_tab(TradingConstants.TRADES_TAB_TRADE_HISTORY) \
            .get_id_closed_order() \
            .get_closed_order_created_time() \
            .get_closed_order_symbol() \
            .get_closed_order_open_price() \
            .get_closed_order_closed_price() \
            .get_closed_order_closed_time() \
            .get_closed_order_profit()

    def verify_close_live_position_crm(self):
        """ Login CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_value('email_live_acc'))

        """ Check if crypto position was opened """
        try:
            assert TradingConstants.IS_ASSET_EXIST == "yes"
            Logging().reportDebugStep(self, "Position was opened")
        except:
            Logging().reportDebugStep(self, "There is no crypto assets")
            Logging().reportDebugStep(self, "NOT RUNNED")
            assert TradingConstants.IS_ASSET_EXIST == "yes"

        """ Open live account details and get closed orders data """
        close_orders_data = ClientProfilePage(self.driver) \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .open_trading_account_by_number(self.config.get_value('number_live_acc')) \
            .open_closed_transactions_tab() \
            .get_closed_order_data()

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
