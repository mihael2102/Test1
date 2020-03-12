import pytest
from src.test.python.ui.automation.utils.preconditions.trading_ui.VerifyLiveOpenPositionPreconditionUI import \
    VerifyLiveOpenPositionPreconditionUI
from src.test.python.ui.automation.utils.preconditions.trading_ui.VerifyLiveClosePreconditionUI import \
    VerifyLiveClosePreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.trading_ui.VerifyClosePositionPreconditionUI import \
    VerifyClosePositionPreconditionUI
from src.test.python.ui.automation.utils.preconditions.trading_process_ca.Trading_Precondition import Trading_Precondition
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.test.python.ui.automation.utils.preconditions.trading_process_ca.TradingPreconditionLive import \
    TradingPreconditionLive
from src.test.python.ui.automation.utils.preconditions.trading_ui.VerifyOpenPositionPreconditionUI import \
    VerifyOpenPositionPreconditionUI
from src.test.python.ui.automation.utils.preconditions.trading_process_ca.CryptoQuotesPreconditionCA import \
    CryptoQuotesPreconditionCA
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage


class TradingProcess(BaseTest):

    def test_crypto_quotes(self):
        CryptoQuotesPreconditionCA(self.driver, self.config).verify_crypto_quotes_ca()

    def test_trading_process_open_position_ca(self):
        Trading_Precondition(self.driver, self.config).trading_process_open_position_ca()

    def test_verify_open_position_crm(self):
        Trading_Precondition(self.driver, self.config).verify_open_position_crm()

    def test_verify_open_position_crm_ui(self):
        VerifyOpenPositionPreconditionUI(self.driver, self.config).verify_open_position_crm_ui()

    def test_trading_process_close_position_ca(self):
        Trading_Precondition(self.driver, self.config).trading_process_close_position_ca()

    def test_verify_close_position_crm(self):
        Trading_Precondition(self.driver, self.config).verify_close_position_crm()

    def test_verify_close_position_crm_ui(self):
        VerifyClosePositionPreconditionUI(self.driver, self.config).verify_close_position_crm_ui()

    def test_open_position_live(self):
        day = CRMHomePage(self.driver).get_day_of_week()
        if day == 6 and global_var.current_brand_name == "q8":
            CALoginPage(self.driver) \
                .not_runned_test()
        else:
            TradingPreconditionLive(self.driver, self.config).open_position_live()

    def test_verify_live_open_position_crm(self):
        day = CRMHomePage(self.driver).get_day_of_week()
        if day == 6 and global_var.current_brand_name == "q8":
            CALoginPage(self.driver) \
                .not_runned_test()
        else:
            TradingPreconditionLive(self.driver, self.config).verify_open_live_position_crm()

    def test_verify_live_open_position_crm_ui(self):
        VerifyLiveOpenPositionPreconditionUI(self.driver, self.config).verify_open_live_position_crm_ui()

    def test_close_position_live(self):
        day = CRMHomePage(self.driver).get_day_of_week()
        if day == 6 and global_var.current_brand_name == "q8":
            CALoginPage(self.driver) \
                .not_runned_test()
        else:
            TradingPreconditionLive(self.driver, self.config).close_position_live()

    def test_verify_live_close_position_crm(self):
        day = CRMHomePage(self.driver).get_day_of_week()
        if day == 3 and global_var.current_brand_name == "q8":
            CALoginPage(self.driver) \
                .not_runned_test()
        else:
            TradingPreconditionLive(self.driver, self.config).verify_close_live_position_crm()

    def test_verify_live_close_position_crm_ui(self):
        VerifyLiveClosePreconditionUI(self.driver, self.config).verify_close_live_position_crm_ui()

    def test_trade_with_insufficient_funds(self):
        if global_var.current_brand_name != "kontofx" and \
           global_var.current_brand_name != "brokerz" and \
           global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config)\
                .trade_with_insufficient_funds()
        else:
            Logging().reportDebugStep(self, "NOT RUNNED")

    def test_open_order_buy_sell(self):
        if global_var.current_brand_name != "kontofx" and \
           global_var.current_brand_name != "brokerz" and \
           global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config)\
                .open_order_buy_sell()
        else:
            Logging().reportDebugStep(self, "NOT RUNNED")

    def test_open_order_stop_loss_take_profit(self):
        if global_var.current_brand_name != "kontofx" and \
           global_var.current_brand_name != "brokerz" and \
           global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config)\
                .open_order_stop_loss_take_profit()
        else:
            Logging().reportDebugStep(self, "NOT RUNNED")

    def test_edit_order_stop_loss_take_profit(self):
        if global_var.current_brand_name != "kontofx" and \
           global_var.current_brand_name != "brokerz" and \
           global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config)\
                .edit_order_stop_loss_take_profit()
        else:
            Logging().reportDebugStep(self, "NOT RUNNED")

    def test_close_order(self):
        if global_var.current_brand_name != "kontofx" and \
           global_var.current_brand_name != "brokerz" and \
           global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config)\
                .close_order()
        else:
            Logging().reportDebugStep(self, "NOT RUNNED")
