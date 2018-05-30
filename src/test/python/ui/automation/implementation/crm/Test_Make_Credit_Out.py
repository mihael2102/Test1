from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.credit_out.CRMCredit_Out_Precondition import \
    CRMCreditOutPrecondition


class CreditInTestCRM(BaseTest):

    def make_credit_out_crm(self):
        CRMCreditOutPrecondition() \
            .add_live_account()
