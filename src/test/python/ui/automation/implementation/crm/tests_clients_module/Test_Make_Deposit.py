import pytest

from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.deposit.CADepositPrecondition import CADepositPrecondition
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=13)
class DepositTestCRM(BaseTest):

    def test_make_deposit_crm(self):
        CADepositPrecondition().add_live_account()
        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        amount_initial = crm_client_profile.get_initial_amount()

        total_amount_crm = crm_client_profile.get_total_amount_text(amount_initial, CRMConstants.AMOUNT_DEPOSIT)

        crm_client_profile \
            .perform_scroll_up() \
            .open_mt4_actions(CRMConstants.DEPOSIT)

        MT4DepositModule().make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT,
                                        CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                        CRMConstants.STATUS_DEPOSIT, CRMConstants.DESCRIPTION_DEPOSIT)

        confirmation_message = crm_client_profile.get_confirm_message()
        assert confirmation_message == CRMConstants.DEPOSIT_SUCCESSFULLY

        amount_crm = crm_client_profile.click_ok() \
            .refresh_page() \
            .click_trading_accounts_tab() \
            .get_amount_text(total_amount_crm)

        amount_from_ca = CaManageAccounts() \
            .switch_first_tab_page() \
            .get_amount_element(account_number, amount_crm)

        assert amount_crm == amount_from_ca
