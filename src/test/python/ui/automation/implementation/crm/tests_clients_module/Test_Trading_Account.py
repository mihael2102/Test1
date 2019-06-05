import pytest
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import \
    TradingAccountPrecondition
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class TradingAccountCrmTest(BaseTest):

    def test_crm_open_trading_account(self):
        try:
            TradingAccountPrecondition(self.driver, self.config) \
                .add_demo_account_from_crm()
            confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
            try:
                if global_var.current_brand_name == "trade99":
                    self.assertEqual(confirmation_message, CRMConstants.TRADING_ACCOUNT_CREATED_SUCCESFULLY)
                else:
                    self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)
            except:
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY_2)
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:

                ClientProfilePage(self.driver).Sign_Out()

                TradingAccountPrecondition(self.driver, self.config) \
                    .add_demo_account_from_crm()
                confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
                try:
                    self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)
                except:
                    self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY_2)
            except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                ClientProfilePage(self.driver).Sign_Out()

                TradingAccountPrecondition(self.driver, self.config) \
                    .add_demo_account_from_crm()
                confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
                try:
                    self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)
                except:
                    self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY_2)

    def test_crm_open_live_trading_account(self):
        TradingAccountPrecondition(self.driver, self.config) \
            .add_live_account_from_crm()
        confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
        try:
            self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)
        except:
            self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY_2)

    def test_crm_open_demo_mt5(self):
        if (global_var.current_brand_name == "q8"):
            TradingAccountPrecondition(self.driver, self.config) \
                .add_mt5_demo_account_from_crm()
            confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
            try:
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)
            except:
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY_2)
        else:
            return self

    def test_crm_open_live_mt5(self):
        if (global_var.current_brand_name == "q8"):
            TradingAccountPrecondition(self.driver, self.config) \
                .add_live_mt5_from_crm()
            confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
            try:
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY)
            except:
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY_2)
        else:
            Logging().reportDebugStep(self, "module does not exist")
            return self

    def test_crm_edit_trading_account(self):
        try:
            TradingAccountPrecondition(self.driver, self.config) \
                .add_demo_account_from_crm()

            # Close pop up and update popup

            ClientProfilePage(self.driver).close_popup_new_trading_account()
            TradingAccountPrecondition(self.driver, self.config).update_demo_account_from_crm()

            confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
            try:
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY)
            except:
                self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY_2)
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:

                ClientProfilePage(self.driver).Sign_Out()
                TradingAccountPrecondition(self.driver, self.config) \
                    .add_demo_account_from_crm()

                # Close pop up and update popup
                ClientProfilePage(self.driver).close_popup_new_trading_account()
                TradingAccountPrecondition(self.driver, self.config).update_demo_account_from_crm()

                confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
                try:
                    self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY)
                except:
                    self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY_2)
            except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                ClientProfilePage(self.driver).Sign_Out()
                TradingAccountPrecondition(self.driver, self.config) \
                    .add_demo_account_from_crm()

                # Close pop up and update popup
                ClientProfilePage(self.driver).close_popup_new_trading_account()
                TradingAccountPrecondition(self.driver, self.config).update_demo_account_from_crm()

                confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
                try:
                    self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY)
                except:
                    self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY_2)





