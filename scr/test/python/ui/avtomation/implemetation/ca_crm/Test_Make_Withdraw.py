from scr.main.python.ui.brand.model.client_area_modules.ca_constats.CaStatusConstants import CaStatusConstants
from scr.main.python.ui.brand.model.client_area_modules.withdraw_module.tabs.CaWithdrawHistory import CaWithdrawHistory
from scr.main.python.ui.brand.model.ca_modules.CAModules import CAModules
from scr.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from scr.test.python.ui.avtomation.BaseTest import *
from scr.test.python.ui.avtomation.utils.preconditions.withdraw.BrandWithdrawPrecondition import \
    BrandWithdrawPrecondition


class Withdraw(BaseTest):

    def test_make_withdraw(self):
        BrandWithdrawPrecondition() \
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

        assert withdraw_status == CaStatusConstants().PENDING

        withdraw_cancel_request = CaWithdrawHistory() \
            .click_cancel() \
            .get_status_request()

        assert withdraw_cancel_request == CaStatusConstants().CANCEL_BY_CUSTOMER
