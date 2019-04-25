import pytest

from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.sign_up.BrandSignUpPrecondition import BrandSignUpPrecondition
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import Login_CA_Precondition
from src.test.python.ui.automation.utils.preconditions.trading_process_ca.Trading_Precondition import Trading_Precondition
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class TradingProcess(BaseTest):

    def test_trade_with_insufficient_funds(self):
        if global_var.current_brand_name != "kontofx" and global_var.current_brand_name != "brokerz" \
                and global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config).trade_with_insufficient_funds()
        else:
            Logging().reportDebugStep(self, "NOT RUNNER")

    def test_open_order_buy_sell(self):
        if global_var.current_brand_name != "kontofx" and global_var.current_brand_name != "brokerz" and global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config).open_order_buy_sell()
        else:
            Logging().reportDebugStep(self, "NOT RUNNER")

    def test_open_order_stop_loss_take_profit(self):
        if global_var.current_brand_name != "kontofx" and global_var.current_brand_name != "brokerz" and global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config).open_order_stop_loss_take_profit()
        else:
            Logging().reportDebugStep(self, "NOT RUNNER")

    def test_edit_order_stop_loss_take_profit(self):
        if global_var.current_brand_name != "kontofx" and global_var.current_brand_name != "brokerz" and global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config).edit_order_stop_loss_take_profit()
        else:
            Logging().reportDebugStep(self, "NOT RUNNER")

    def test_close_order(self):
        if global_var.current_brand_name != "kontofx" and global_var.current_brand_name != "brokerz" and global_var.current_brand_name != "q8":
            Trading_Precondition(self.driver, self.config).close_order()
        else:
            Logging().reportDebugStep(self, "NOT RUNNER")