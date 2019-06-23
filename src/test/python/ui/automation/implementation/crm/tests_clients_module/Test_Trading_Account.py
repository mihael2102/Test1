import pytest
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import \
    TradingAccountPrecondition
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition


class TradingAccountCrmTest(BaseTest):

    def fill_questioner_new_client(self):
        if (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "gmo"):
            client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
            LeadPrecondition(self.driver, self.config).fill_questioner_new_client(client1[LeadsModuleConstants.EMAIL])
        else:
            Logging().reportDebugStep(self, "Brand doesnt contains questioner")
            return self

    def test_crm_open_trading_account(self):
        TradingAccountPrecondition(self.driver, self.config) \
            .add_demo_account_from_crm()
        confirmation_message = ClientProfilePage(self.driver).get_confirm_message()
        self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_CREATED_SUCCESFULLY_OLD_FOREX)

    def test_crm_edit_trading_account(self):
        TradingAccountPrecondition(self.driver, self.config) \
            .add_demo_account_from_crm()
        ClientProfilePage(self.driver).click_close()
        ClientProfilePage(self.driver).refresh_page()
        time.sleep(7)
        ClientProfilePage(self.driver).refresh_page()
        TradingAccountPrecondition(self.driver, self.config).update_demo_account_from_crm()

        confirmation_message = ClientProfilePage(self.driver).get_confirm_message_body()
        self.assertEqual(confirmation_message, CRMConstants.MT4_ACCOUNT_UPDATED_SUCCESFULLY)
