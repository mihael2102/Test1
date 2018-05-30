from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.withdraw.MT4WithdrawModule import MT4WithdrawModule
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from src.main.python.ui.results.expected_result.DepositExpectedResult import DepositExpectedResult
from src.test.python.ui.avtomation.BaseTest import *
from src.test.python.ui.avtomation.utils.preconditions.withdraw_crm.CRMWithdrawPrecondition import \
    CRMWithdrawPrecondition


class WithdrawTestCRM(BaseTest):

    def test_make_withdraw_crm(self):
        CRMWithdrawPrecondition().add_live_account().make_deposit()

        crm_client_profile = CRMClientProfilePage()

        account = crm_client_profile.get_client_account()

        amount_initial = crm_client_profile.get_initial_amount()

        total_amount_withdraw_crm = CRMClientProfilePage() \
            .get_total_amount_withdraw_text(amount_initial, CRMConstants.AMOUNT_WITHDRAW)

        crm_client_profile.perform_scroll_up() \
            .open_mt4_actions(CRMConstants.WITHDRAW)

        MT4WithdrawModule().make_withdraw(
            account, CRMConstants.AMOUNT_WITHDRAW, CRMConstants.PAYMENT_METHOD_WITHDRAW, CRMConstants.STATUS_WITHDRAW,
            CRMConstants.DESCRIPTION_WITHDRAW)

        confirmation_message = crm_client_profile.get_confirm_message()
        assert confirmation_message == CRMConstants.WITHDRAW_SUCCESSFULLY

        amount_withdraw_crm = crm_client_profile.click_ok() \
            .refresh_page() \
            .click_trading_accounts_tab() \
            .get_amount_text(total_amount_withdraw_crm)

        assert amount_withdraw_crm == total_amount_withdraw_crm

        amount_from_ca = CaManageAccounts() \
            .switch_first_tab_page() \
            .get_amount_element(account, amount_withdraw_crm)

        DepositExpectedResult().print_expected_result(amount_from_ca, account)

        assert amount_withdraw_crm == amount_from_ca
