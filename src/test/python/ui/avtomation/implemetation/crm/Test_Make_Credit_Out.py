from src.test.python.ui.avtomation.BaseTest import *
from src.test.python.ui.avtomation.utils.preconditions.credit_out.CRMCredit_Out_Precondition import \
    CRMCreditOutPrecondition


class CreditInTestCRM(BaseTest):

    def make_credit_out_crm(self):
        CRMCreditOutPrecondition() \
            .add_live_account()
