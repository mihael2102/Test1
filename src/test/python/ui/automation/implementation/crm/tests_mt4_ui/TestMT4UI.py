import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4DepositPreconditionUI import \
    MT4DepositPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4CreateTAPreconditionUI import \
    MT4CreateTAPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4WithdrawPreconditionUI import MT4WithdrawPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4CreditInPreconditionUI import MT4CreditInPreconditionUI


@pytest.mark.run(order=3)
class TestMT4UI(BaseTest):

    def test_create_demo_trading_account_ui(self):
        MT4CreateTAPreconditionUI(self.driver, self.config).create_demo_trading_account_ui()

    def test_deposit_crm_ui(self):
        MT4DepositPreconditionUI(self.driver, self.config).deposit_crm_ui()

    def test_withdraw_crm_ui(self):
        MT4WithdrawPreconditionUI(self.driver, self.config).withdraw_crm_ui()

    def test_credit_in_crm_ui(self):
        MT4CreditInPreconditionUI(self.driver, self.config).credit_in_crm_ui()
