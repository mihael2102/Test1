import pytest

from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.transfer_funds.CATransferFundsPrecondition import \
    CATransferFundsPrecondition


@pytest.mark.run(order=7)
class TransferFundsTestCA(BaseTest):

    def test_make_transfer_funds(self):
        CATransferFundsPrecondition() \
            .add_two_eur_currencies() \
            .make_deposit()

        client_profile = ClientProfilePage()
        first_transfer_account = client_profile.get_client_account()
        second_transfer_account = client_profile.get_second_client_account()

        CaManageAccounts().switch_first_tab_page() \
            .open_transfer_between_accounts_button() \
            .choose_transfer_from_account(first_transfer_account) \
            .choose_transfer_to_account(second_transfer_account) \
            .set_amount(second_transfer_account, CaConstants.AMOUNT) \
            .confirm_check_box() \
            .make_transfer_button() \
            .refreshing_wait()

        amount_first_transfer_account_ca = CaManageAccounts().get_amount_by_account_text(first_transfer_account)

        assert CaConstants.AMOUNT == amount_first_transfer_account_ca
