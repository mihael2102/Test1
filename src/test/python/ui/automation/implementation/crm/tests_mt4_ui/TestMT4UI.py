import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4DepositPreconditionUI import \
    MT4DepositPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4CreateTAPreconditionUI import \
    MT4CreateTAPreconditionUI


@pytest.mark.run(order=3)
class TestMT4UI(BaseTest):

    def test_create_demo_trading_account_ui(self):
        MT4CreateTAPreconditionUI(self.driver, self.config).create_demo_trading_account_ui()

    def test_deposit_crm_new_ui(self):
        MT4DepositPreconditionUI(self.driver, self.config).deposit_crm_new_ui()
