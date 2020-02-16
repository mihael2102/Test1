import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.financial_transactions_ca.WithdrawRequestPreconditionCA import \
    WithdrawRequestPreconditionCA


@pytest.mark.run(order=2)
class TestFinancialTransactionsCA(BaseTest):

    def test_withdraw_request(self):
        WithdrawRequestPreconditionCA(self.driver, self.config).withdraw_request_ca()
