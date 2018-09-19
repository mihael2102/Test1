import pytest

from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.modules.client_modules.client_deposit.CRMClientDeposit import CRMClientDeposit
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import \
    TradingAccountPrecondition


@pytest.mark.run(order=13)
class DepositTestCRM(BaseTest):

    def test_make_deposit_crm(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        amount_initial = crm_client_profile.get_initial_amount()

        total_amount_crm = crm_client_profile.get_total_amount_text(amount_initial, CRMConstants.AMOUNT_DEPOSIT)

        crm_client_profile \
            .perform_scroll_up() \
            .open_mt4_actions(CRMConstants.DEPOSIT)

        MT4DepositModule(self.driver).\
            make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT, CRMConstants.PAYMENT_METHOD_DEPOSIT,
                         CRMConstants.STATUS_DEPOSIT, CRMConstants.DESCRIPTION_DEPOSIT)

        confirmation_message = crm_client_profile.get_confirm_message()
        self.assertEqual(confirmation_message, CRMConstants.DEPOSIT_SUCCESSFULLY)

        # amount_crm = crm_client_profile.click_ok() \
        #     .refresh_page() \
        #     .click_trading_accounts_tab() \
        #     .get_amount_text(total_amount_crm)

    def test_make_deposit_for_client_crm(self):
        TradingAccountPrecondition(self.driver, self.config) \
            .add_live_account_from_crm()

        crm_client_profile = ClientProfilePage(self.driver).close_popup_new_trading_account()

        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        amount_initial = crm_client_profile.get_initial_amount()

        crm_client_profile \
            .perform_scroll_up() \
            .open_deposit_for_client_in_menu()\
            .fill_client_deposit_pop(account_number)

        deposit_successful = CRMClientDeposit(self.driver)\
            .select_payment_method(CaConstants.VISA) \
            .set_card_number("4444444444444448") \
            .set_expiry_date("092020") \
            .set_cvc("123") \
            .set_amount_deposit(CaConstants.AMOUNT_DEPOSIT) \
            .perform_deposit() \
            .get_successful_deposit_message()

        self.assertEqual(CaConstants.SUCCESSFUL_DEPOSIT_MESSAGE, deposit_successful, "Transaction failed")

