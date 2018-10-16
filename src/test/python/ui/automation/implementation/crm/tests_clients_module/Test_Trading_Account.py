import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import \
    TradingAccountPrecondition
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage

class TradingAccountCrmTest(BaseTest):

    def test_crm_open_trading_account(self):
        TradingAccountPrecondition(self.driver, self.config) \
            .add_demo_account_from_crm()
        confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
        self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY_OLD_FOREX)

    def test_crm_edit_trading_account(self):
        TradingAccountPrecondition(self.driver, self.config) \
            .add_demo_account_from_crm()
        ClientProfilePage(self.driver).click_close()

        # Close pop up and update popup
        # ClientProfilePage(self.driver).close_popup_new_trading_account()
        TradingAccountPrecondition(self.driver, self.config).update_demo_account_from_crm()

        confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
        self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY)





