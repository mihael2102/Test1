import pytest

from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.deposit.CADeposit import CADeposit
from src.main.python.ui.brand.model.client_area_modules.deposit.CASuccessFailedDeposit import CASuccessFailedDeposit
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import BaseTest
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=7)
class DepositTestCa(BaseTest):
    # TEST WAS DISABLED UNTIL DEPOSIT TRANSACTIONS WOULD BE CONFIGURED
    # def test_make_success_deposit_from_ca(self):
    #     BrandHomePage().open_first_tab_page(Config.url_client_area) \
    #         .login() \
    #         .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
    #                     Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
    #         .click_login_button() \
    #         .open_drop_down_menu() \
    #         .select_module(CaConstants.DEPOSIT)
    #
    #     deposit_successful = CADeposit().select_payment_method(CaConstants.VISA) \
    #         .set_amount_deposit(CaConstants.AMOUNT_DEPOSIT) \
    #         .click_deposit_button() \
    #         .set_card_number(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CREDIT_CARD)) \
    #         .set_expiry_date(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.EXPIRY_DATE)) \
    #         .set_expiry_year(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.EXPIRY_YEAR)) \
    #         .set_cvc(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CVC)) \
    #         .perform_deposit() \
    #         .get_successful_deposit_message()
    #
    #     amount_successful = CASuccessFailedDeposit().get_amount_text()
    #
    #     assert deposit_successful == CaConstants.SUCCESSFUL_DEPOSIT_MESSAGE
    #     assert amount_successful == CaConstants.SUCCESSFUL_AMOUNT_MESSAGE

    def test_make_failed_deposit_from_ca(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area) \
            .login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.DEPOSIT)

        "This test should be passed in case of absense of connection between CA and CRM but with valid credit card info"
        deposit_failed = CADeposit().select_payment_method(CaConstants.VISA) \
            .set_amount_deposit(CaConstants.AMOUNT_DEPOSIT) \
            .click_deposit_button() \
            .set_card_number(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CREDIT_CARD)) \
            .set_expiry_date(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.EXPIRY_DATE)) \
            .set_expiry_year(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.EXPIRY_YEAR)) \
            .set_cvc(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CVC)) \
            .perform_deposit() \
            .get_failed_deposit_message()

        # Check text of failed message
        assert CaConstants.FAILED_DEPOSIT_MESSAGE == deposit_failed

        # Check status and sun of failed deposit in CRM
        crm_page = CRMLoginPage()
        crm_client_page = crm_page \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .open_client_module_clients_module() \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL)) \

        crm_client_page.perform_scroll("1800")
        crm_client_page.open_financial_transactions_tab()
        crm_amount_text = crm_client_page.get_financial_transaction_text()
        crm_transaction_approval_state_failed = crm_client_page.get_transaction_approval_state()

        assert CaConstants.AMOUNT_DEPOSIT == crm_amount_text
        assert CaConstants.TRANSACTION_APPROVAL_STATE_FAILED == crm_transaction_approval_state_failed

