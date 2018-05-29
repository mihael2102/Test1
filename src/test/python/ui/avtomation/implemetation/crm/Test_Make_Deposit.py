from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.results.actual_result.DepositActualResult import DepositActualResult
from src.main.python.ui.results.expected_result.DepositExpectedResult import DepositExpectedResult
from src.test.python.ui.avtomation.BaseTest import *
from src.test.python.ui.avtomation.utils.preconditions.deposit.CADepositPrecondition import CADepositPrecondition
from src.test.python.utils.TestDataConstants import TestDataConstants


class DepositTestCRM(BaseTest):

    def test_make_deposit(self):
        CADepositPrecondition().add_live_account()
        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_first_client(TestDataConstants.E_MAIL))

        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        amount_initial = CRMClientProfilePage().get_initial_amount()

        total_amount_crm = CRMClientProfilePage() \
            .get_total_amount_text(amount_initial, CRMConstants.AMOUNT_DEPOSIT)

        CRMClientProfilePage() \
            .perform_scroll_up() \
            .open_mt4_actions(CRMConstants.DEPOSIT)

        amount_crm = MT4DepositModule() \
            .make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT, CRMConstants.PAYMENT_METHOD_DEPOSIT,
                          CRMConstants.STATUS_DEPOSIT, CRMConstants.DESCRIPTION_DEPOSIT) \
            .refresh_page() \
            .click_trading_accounts_tab() \
            .get_amount_text(total_amount_crm)

        DepositActualResult().print_actual_result(amount_crm, account_number)

        amount_from_ca = CaManageAccounts() \
            .switch_first_tab_page() \
            .get_amount_element(account_number, amount_crm)

        DepositExpectedResult().print_expected_result(amount_from_ca, account_number)

        assert amount_crm == amount_from_ca
