import pytest

from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.credit_out.Credit_Out_Precondition import \
    CreditOutPrecondition


@pytest.mark.run(order=2)
class CreditOutTestCRM(BaseTest):

    def test_make_credit_out_crm(self):
        CreditOutPrecondition(self.driver, self.config).credit_out_crm()

