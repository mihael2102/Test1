import pytest

from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.withdraw_module.tabs.CaWithdrawHistory import CaWithdrawHistory
from src.main.python.ui.brand.model.ca_modules.CAModules import CAModules
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.withdraw_ca.CAWithdrawPrecondition import \
    CAWithdrawPrecondition


@pytest.mark.run(order=7)
class WithdrawTestCA(BaseTest):

    def test_make_withdraw_ca(self):
        CAWithdrawPrecondition() \
            .add_live_account() \
            .make_deposit()

        account_number = ClientProfilePage().get_client_account()

        withdraw_status = CAModules() \
            .switch_first_tab_page() \
            .open_withdraw_page() \
            .perform_withdraw_first_step_request(account_number) \
            .perform_withdraw_second_step_request() \
            .click_withdraw_history_tab() \
            .select_account(account_number) \
            .get_status_request()

        assert withdraw_status == CaConstants().PENDING

        withdraw_cancel_request = CaWithdrawHistory() \
            .click_cancel() \
            .get_status_request()

        assert withdraw_cancel_request == CaConstants().CANCEL_BY_CUSTOMER
