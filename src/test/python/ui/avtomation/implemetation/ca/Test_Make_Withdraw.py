from src.main.python.ui.brand.model.client_area_modules.constats.CaStatusConstants import CaStatusConstants
from src.main.python.ui.brand.model.client_area_modules.withdraw_module.tabs.CaWithdrawHistory import CaWithdrawHistory
from src.main.python.ui.brand.model.ca_modules.CAModules import CAModules
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from src.main.python.ui.results.actual_result.WithdrawActualResult import WithdrawActualResult
from src.test.python.ui.avtomation.BaseTest import *
from src.test.python.ui.avtomation.utils.preconditions.withdraw_ca.CAWithdrawPrecondition import \
    CAWithdrawPrecondition


class WithdrawTestCA(BaseTest):

    def test_make_withdraw_ca(self):
        CAWithdrawPrecondition() \
            .add_live_account() \
            .make_deposit()

        account_number = CRMClientProfilePage().get_client_account()

        withdraw_status = CAModules() \
            .switch_first_tab_page() \
            .open_withdraw_page() \
            .perform_withdraw_first_step_request(account_number) \
            .perform_withdraw_second_step_request() \
            .click_withdraw_history_tab() \
            .select_account(account_number) \
            .get_status_request()

        WithdrawActualResult().print_first_actual_result(withdraw_status, account_number)
        assert withdraw_status == CaStatusConstants().PENDING

        withdraw_cancel_request = CaWithdrawHistory() \
            .click_cancel() \
            .get_status_request()

        WithdrawActualResult().print_second_actual_result(withdraw_cancel_request, account_number)

        assert withdraw_cancel_request == CaStatusConstants().CANCEL_BY_CUSTOMER
