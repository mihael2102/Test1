import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import \
    TradingAccountPrecondition
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage

class TradingAccountCrmTest(BaseTest):

    def test_crm_open_trading_account(self):
        try:
            TradingAccountPrecondition(self.driver, self.config) \
                .add_demo_account_from_crm()
            confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
            self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:

                ClientProfilePage(self.driver).Sign_Out()

                TradingAccountPrecondition(self.driver, self.config) \
                    .add_demo_account_from_crm()
                confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)
            except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                ClientProfilePage(self.driver).Sign_Out()

                TradingAccountPrecondition(self.driver, self.config) \
                    .add_demo_account_from_crm()
                confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)

    def test_crm_open_live_trading_account(self):
        TradingAccountPrecondition(self.driver, self.config) \
            .add_live_account_from_crm()
        confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
        self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)

    def test_crm_edit_trading_account(self):
        try:
            TradingAccountPrecondition(self.driver, self.config) \
                .add_demo_account_from_crm()

            # Close pop up and update popup
            ClientProfilePage(self.driver).close_popup_new_trading_account()
            TradingAccountPrecondition(self.driver, self.config).update_demo_account_from_crm()

            confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
            self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY)
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:

                ClientProfilePage(self.driver).Sign_Out()
                TradingAccountPrecondition(self.driver, self.config) \
                    .add_demo_account_from_crm()

                # Close pop up and update popup
                ClientProfilePage(self.driver).close_popup_new_trading_account()
                TradingAccountPrecondition(self.driver, self.config).update_demo_account_from_crm()

                confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY)
            except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                ClientProfilePage(self.driver).Sign_Out()
                TradingAccountPrecondition(self.driver, self.config) \
                    .add_demo_account_from_crm()

                # Close pop up and update popup
                ClientProfilePage(self.driver).close_popup_new_trading_account()
                TradingAccountPrecondition(self.driver, self.config).update_demo_account_from_crm()

                confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY)





