import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.filter_ui.FilterClientsPreconditionUI import \
    FilterClientsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4CreateTAPreconditionUI import \
    MT4CreateTAPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4WithdrawPreconditionUI import MT4WithdrawPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4CreditInPreconditionUI import MT4CreditInPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4TransferPreconditionUI import MT4TransferPreconditionUI
from src.test.python.ui.automation.utils.preconditions.mt4_ui.MT4CreditOutPreconditionUI import \
    MT4CreditOutPreconditionUI


@pytest.mark.run(order=3)
class TestFiltersUI(BaseTest):

    def test_filter_clients_ui(self):
        FilterClientsPreconditionUI(self.driver, self.config).create_filter_clients_ui()
