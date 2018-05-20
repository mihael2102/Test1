from src.main.python.ui.brand.model.client_area_modules.ca_constats.CaStatusConstants import CaStatusConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from src.main.python.ui.results.actual_result.TransferFundsActualResult import TransferFundsActualResult
from src.main.python.ui.results.expected_result.TransferFundsExpectedResult import TransferFundsExpectedResult
from src.test.python.ui.avtomation.BaseTest import *
from src.test.python.ui.avtomation.utils.preconditions.transfer_funds.BrandTransferFundsPrecondition import \
    BrandTransferFundsPrecondition
from src.test.python.utils.TestDataConstants import TestDataConstants


class TransferFunds(BaseTest):

    def test_make_transfer_funds(self):
        BrandTransferFundsPrecondition() \
            .add_two_eur_currencies() \
            .make_deposit()

        first_transfer_account = CRMClientProfilePage().get_client_account()
        second_transfer_account = CRMClientProfilePage().get_second_client_account()

        CaManageAccounts().switch_first_tab_page() \
            .open_transfer_between_accounts_button() \
            .choose_transfer_from_account(first_transfer_account) \
            .choose_transfer_to_account(second_transfer_account) \
            .set_amount(second_transfer_account,TestDataConstants.AMOUNT) \
            .confirm_check_box() \
            .make_transfer_button()\
            .refreshing_wait()

        TransferFundsActualResult().print_actual_result(first_transfer_account, TestDataConstants.AMOUNT,
                                                        second_transfer_account)

        amount_first_transfer_account_ca = CaManageAccounts().get_amount_by_account_text(first_transfer_account)

        TransferFundsExpectedResult().print_expected_result(first_transfer_account, TestDataConstants.AMOUNT,
                                                            second_transfer_account)

        assert TestDataConstants.AMOUNT == amount_first_transfer_account_ca
