import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.fin_transactions_ui.\
    FinTransactionsSearchingColumnsPreconditionUI import FinTransactionsSearchingColumnsPreconditionUI


@pytest.mark.run(order=3)
class TestFinTransactionsModuleUI(BaseTest):

    def test_fin_transactions_searching_columns_ui(self):
        FinTransactionsSearchingColumnsPreconditionUI(self.driver, self.config).fin_transactions_searching_columns_ui()
