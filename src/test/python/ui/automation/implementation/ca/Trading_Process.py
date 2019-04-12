import pytest

from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.sign_up.BrandSignUpPrecondition import BrandSignUpPrecondition
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import Login_CA_Precondition
from src.test.python.ui.automation.utils.preconditions.trading_process_ca.Trading_Precondition import Trading_Precondition

class TradingProcess(BaseTest):

    def test_trade_with_insufficient_funds(self):
        Trading_Precondition(self.driver, self.config).trade_with_insufficient_funds()

    def test_open_order_buy_sell(self):
        Trading_Precondition(self.driver, self.config).open_order_buy_sell()