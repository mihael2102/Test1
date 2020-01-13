import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.Deposit_Precondition_UI import DepositPreconditionUI


@pytest.mark.run(order=3)
class TestMT4UI(BaseTest):

    def test_deposit_crm_new_ui(self):
        DepositPreconditionUI(self.driver, self.config).deposit_crm_new_ui()
