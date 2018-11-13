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
        try:
            # lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
            # client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD))
            # Create new lead and convert him to new client
            # LeadPrecondition(self.driver, self.config).create_lead(lead1)
            # lead_view_profile_page = LeadViewInfo(self.driver)
            #
            # lead_view_profile_page.open_convert_lead_module() \
            #     .perform_convert_lead(
            #     client1[LeadsModuleConstants.FIRST_NAME],
            #     client1[LeadsModuleConstants.FIRST_LAST_NAME],
            #     client1[LeadsModuleConstants.EMAIL],
            #     client1[LeadsModuleConstants.PHONE],
            #     client1[LeadsModuleConstants.BIRTHDAY],
            #     client1[LeadsModuleConstants.CITIZENSHIP],
            #     client1[LeadsModuleConstants.STREET],
            #     client1[LeadsModuleConstants.POSTAL_CODE],
            #     client1[LeadsModuleConstants.CITY],
            #     client1[LeadsModuleConstants.FIRST_COUNTRY],
            #     client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
            #     client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD],
            #     client1[LeadsModuleConstants.FIRST_REFERRAL],
            #     client1[LeadsModuleConstants.BRAND],
            #     client1[LeadsModuleConstants.FIRST_SOURCE_NAME],
            #     client1[LeadsModuleConstants.PHONE_AREA_CODE])
            #
            # convert_verified = False
            # # Checking that the lead was converted successfully
            # try:
            #     confirmation_message = lead_view_profile_page.get_confirm_message_lead_view_profile()
            #     assert confirmation_message == CRMConstants().CONVERT_SUCCESSFUL_MESSAGE
            #     lead_view_profile_page.click_ok()
            #     convert_verified = True
            # except TimeoutException:
            #     Logging().reportDebugStep(self, "Lead convert message was not picked up")
            # if not convert_verified:
            #     lead_detail_view = LeadDetailViewInfo(self.driver)
            #     lead_detail_view.wait_element_to_be_clickable("//input[@name='Edit']")
            #     self.assertEqual(' yes ', lead_detail_view.get_exists_text(), "Lead is not at exists state. "
            #                                                                   "Client was not created")

            # ADD LIVE ACCOUNT IN CRM
            # Open clients module. Find created client by email and open his profile
            CreditInPrecondition(self.driver, self.config).add_live_account_in_crm()

            # Take number of account
            account_number = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .open_trading_accounts_tab() \
                .get_client_account()

            ClientProfilePage(self.driver).perform_scroll_up()
            MT4DropDown(self.driver).mt4_actions(CRMConstants.CREDIT_IN)

            MT4CreditInModule(self.driver).make_credit_in(account_number, CRMConstants.AMOUNT_CREDIT_IN,
                                               CRMConstants.EXPIRE_DATE.strftime(CRMConstants.FORMAT_DATE),
                                               CRMConstants.CREDIT_IN_COMMENT) \
                .click_ok() \
                .refresh_page()\
                .refresh_page()
            time.sleep(10)

            MT4CreditInModule(self.driver).refresh_page()
            # Check the Credit In amount
            credit_in_amount = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .get_amount_of_credit_in(CRMConstants.AMOUNT_CREDIT_IN)     # Get amount from block 'Trading Accounts'

            self.assertEqual(CRMConstants.AMOUNT_CREDIT_IN, credit_in_amount, "Wrong Credit In amount is displayed")
        except (ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:
                ClientProfilePage(self.driver).Sign_Out()
                # lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
                # client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
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
                MT4DropDown(self.driver).mt4_actions(CRMConstants.CREDIT_IN)

                MT4CreditInModule(self.driver).make_credit_in(account_number, CRMConstants.AMOUNT_CREDIT_IN,
                                                              CRMConstants.EXPIRE_DATE.strftime(CRMConstants.FORMAT_DATE),
                                                              CRMConstants.CREDIT_IN_COMMENT) \
                    .click_ok() \
                    .refresh_page() \
                    .refresh_page()
                time.sleep(10)

                MT4CreditInModule(self.driver).refresh_page()
                # Check the Credit In amount
                credit_in_amount = ClientProfilePage(self.driver) \
                    .perform_scroll_down() \
                    .get_amount_of_credit_in(CRMConstants.AMOUNT_CREDIT_IN)  # Get amount from block 'Trading Accounts'

                self.assertEqual(CRMConstants.AMOUNT_CREDIT_IN, credit_in_amount, "Wrong Credit In amount is displayed")
            except (ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                ClientProfilePage(self.driver).Sign_Out()
                # lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
                # client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
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
                MT4DropDown(self.driver).mt4_actions(CRMConstants.CREDIT_IN)

                MT4CreditInModule(self.driver).make_credit_in(account_number, CRMConstants.AMOUNT_CREDIT_IN,
                                                              CRMConstants.EXPIRE_DATE.strftime(
                                                                  CRMConstants.FORMAT_DATE),
                                                              CRMConstants.CREDIT_IN_COMMENT) \
                    .click_ok() \
                    .refresh_page() \
                    .refresh_page()
                time.sleep(10)

                MT4CreditInModule(self.driver).refresh_page()
                # Check the Credit In amount
                credit_in_amount = ClientProfilePage(self.driver) \
                    .perform_scroll_down() \
                    .get_amount_of_credit_in(CRMConstants.AMOUNT_CREDIT_IN)  # Get amount from block 'Trading Accounts'

                self.assertEqual(CRMConstants.AMOUNT_CREDIT_IN, credit_in_amount, "Wrong Credit In amount is displayed")

