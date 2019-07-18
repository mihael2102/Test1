import pytest
from selenium.common.exceptions import TimeoutException

from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.modules.leads_module.LeadViewInfo import LeadViewInfo
from src.main.python.ui.crm.model.mt4.credit_in.MT4CreditInModule import MT4CreditInModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.leads.LeadDetailViewInfo import LeadDetailViewInfo
from src.main.python.utils.logs.Loging import Logging
from src.test.python.ui.automation.BaseTest import BaseTest
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.implementation.crm.tests_leads_module.Test_Leads_Module import LeadModuleTest
from src.test.python.ui.automation.utils.preconditions.credit_in.Credit_In_Precondition import \
    CreditInPrecondition
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
import time
from selenium.common.exceptions import NoSuchElementException
from time import sleep


@pytest.mark.run(order=1)
class CreditInTestCRM(BaseTest):

    def test_make_credit_in_crm(self):
        CreditInPrecondition(self.driver, self.config).add_live_account().make_credit_in()

        crm_client_profile = ClientProfilePage()

        account_client = crm_client_profile \
            .click_trading_accounts_tab() \
            .get_client_account()

        amount_credit_in_crm = crm_client_profile.get_amount_text(CRMConstants.AMOUNT_CREDIT_IN)

        amount_credit_in_ca = CaManageAccounts() \
            .switch_first_tab_page() \
            .get_amount_element(account_client, amount_credit_in_crm)

        assert amount_credit_in_crm == amount_credit_in_ca

    def test_make_credit_in_from_crm(self):

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        CreditInPrecondition(self.driver, self.config).add_live_account_in_crm()

        # Take number of account
        account_number = ClientProfilePage(self.driver) \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        ClientProfilePage(self.driver).perform_scroll_up()
        ClientProfilePage(self.driver).open_mt4_actions(CRMConstants.CREDIT_IN)
        # MT4DropDown(self.driver).mt4_actions(CRMConstants.CREDIT_IN)

        MT4CreditInModule(self.driver)\
            .make_credit_in(account_number,
                            CRMConstants.AMOUNT_CREDIT_IN,
                            CRMConstants.EXPIRE_DATE.strftime(CRMConstants.FORMAT_DATE),
                            CRMConstants.CREDIT_IN_COMMENT,
                            CRMConstants.CLEARNED_BY) \
            .click_ok() \
            .refresh_page()
        sleep(1)

        # Check the Credit In amount
        ClientProfilePage(self.driver)\
            .perform_scroll_down() \
            .click_trading_accounts_tab() \
            .open_trading_account_page(account_number)
        sleep(2)
        actual_credit = ClientProfilePage(self.driver).get_credit_in_trading_account()
        expected_credit = CRMConstants.AMOUNT_CREDIT_IN
        count = 0
        while actual_credit != expected_credit:
            sleep(1)
            MT4CreditInModule(self.driver).refresh_page()
            sleep(1)
            actual_credit = ClientProfilePage(self.driver).get_credit_in_trading_account()
            count += 1
            if count == 7:
                break

        self.assertEqual(expected_credit, actual_credit, "Wrong credit sum is displayed")
