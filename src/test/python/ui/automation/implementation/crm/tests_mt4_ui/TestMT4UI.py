import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4DepositPreconditionUI import \
    MT4DepositPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4CreateTAPreconditionUI import \
    MT4CreateTAPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4WithdrawPreconditionUI import MT4WithdrawPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4CreditInPreconditionUI import MT4CreditInPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4TransferPreconditionUI import MT4TransferPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4UpdateUserPreconditionUI import \
    MT4UpdateUserPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4CreditOutPreconditionUI import \
    MT4CreditOutPreconditionUI


@pytest.mark.run(order=3)
class TestMT4UI(BaseTest):

    def test_create_demo_ta_ui(self):
        MT4CreateTAPreconditionUI(self.driver, self.config).create_demo_trading_account_ui()

    def test_update_mt_user_ui(self):
        MT4UpdateUserPreconditionUI(self.driver, self.config).update_user_crm_ui()

    def test_deposit_crm_ui(self):
        MT4DepositPreconditionUI(self.driver, self.config).deposit_crm_ui()

    def test_withdraw_crm_ui(self):
        MT4WithdrawPreconditionUI(self.driver, self.config).withdraw_crm_ui()

    def test_credit_in_crm_ui(self):
        MT4CreditInPreconditionUI(self.driver, self.config).credit_in_crm_ui()

    def test_credit_out_crm_ui(self):
        MT4CreditOutPreconditionUI(self.driver, self.config).credit_out_crm_ui()

    def test_transfer_crm_ui(self):
        MT4TransferPreconditionUI(self.driver, self.config).transfer_crm_ui()
