import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.credit_out.MT4CreditOutModule import MT4CreditOutModule
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.credit_out.CRMCredit_Out_Precondition import \
    CRMCreditOutPrecondition


@pytest.mark.run(order=13)
class CreditOutTestCRM(BaseTest):

    def test_make_credit_out_crm(self):
        CRMCreditOutPrecondition().add_live_account().make_deposit()
        crm_client_profile = CRMClientProfilePage()
        amount_initial = crm_client_profile.get_initial_amount()

        difference_amount = crm_client_profile \
            .get_difference_amount_text(amount_initial, CRMConstants.AMOUNT_CREDIT_OUT)

        account_number = crm_client_profile.get_client_account()
        crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.CREDIT_OUT)

        MT4CreditOutModule().make_credit_out(account_number, CRMConstants.AMOUNT_CREDIT_OUT,
                                             CRMConstants.CREDIT_OUT_COMMENT) \
            .click_ok() \
            .refresh_page()

        amount_credit_out = crm_client_profile.click_trading_accounts_tab().get_amount_text(difference_amount)

        assert amount_credit_out == difference_amount
