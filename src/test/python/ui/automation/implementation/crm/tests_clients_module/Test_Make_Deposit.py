import pytest
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.modules.client_modules.client_deposit.CRMClientDeposit import CRMClientDeposit
from src.main.python.ui.crm.model.modules.leads_module.LeadViewInfo import LeadViewInfo
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.leads.LeadDetailViewInfo import LeadDetailViewInfo
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import \
    TradingAccountPrecondition
from selenium.common.exceptions import NoSuchElementException

@pytest.mark.run(order=13)
class DepositTestCRM(BaseTest):

    def test_make_deposit_crm(self):
        try:
            # lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
            client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD))
            # # Create new lead and convert him to new client
            #  LeadPrecondition(self.driver, self.config).create_lead(lead1)
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
            CRMHomePage(self.driver).open_client_module()\
                                    .select_filter(self.config.get_value(
                                                                TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                                    .find_client_by_email(client1[LeadsModuleConstants.EMAIL])

            # Create LIVE account for client using MT4 Actions
            crm_client_profile = ClientProfilePage(self.driver)
            crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

            if (global_var.current_brand_name == "royal_cfds") or (global_var.current_brand_name == "newforexstaging"):
                MT4CreateAccountModule(self.driver) \
                    .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                    .click_ok()

            elif (global_var.current_brand_name == "q8"):
                MT4CreateAccountModule(self.driver)\
                    .create_account_with_platform(
                    self.config.get_value(TestDataConstants.TRADING_PLATFORMS, TestDataConstants.TRADING_PLATFORM_MT4),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                    .click_ok()

            elif (global_var.current_brand_name == "axa_markets"):
                MT4CreateAccountModule(self.driver)\
                    .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE_400)) \
                    .click_ok()

            elif (global_var.current_brand_name == "xtraderfx") or (global_var.current_brand_name == "optionstars") or (global_var.current_brand_name == "gxfx") or (global_var.current_brand_name == "b-traderfx"):
                MT4CreateAccountModule(self.driver)\
                    .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY_EUR),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_EUR),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                    .click_ok()

            else:
                MT4CreateAccountModule(self.driver) \
                    .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE))\
                    .click_ok()

            # Get account number to make deposit in future
            account_number = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .open_trading_accounts_tab() \
                .get_client_account()

            # Make deposit for account number using MT4 Actions
            crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.DEPOSIT)

            MT4DepositModule(self.driver).make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
                                                       CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                                       CRMConstants.STATUS_DEPOSIT, CRMConstants.DESCRIPTION_DEPOSIT)

            # Check confirmation message
            confirmation_message = crm_client_profile.get_confirm_message()
            self.assertEqual(confirmation_message, CRMConstants.DEPOSIT_SUCCESSFULLY)

            # Close popup
            crm_client_profile.click_ok()\
                              .refresh_page()

            deposit_amount_text = crm_client_profile.click_trading_accounts_tab() \
                                                    .get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)

            self.assertEqual(
                        CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT, deposit_amount_text, "Wrong deposit sum is displayed")

        except (ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:
                ClientProfilePage(self.driver).Sign_Out()
                # lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
                client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
                CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD))
                # # Create new lead and convert him to new client
                #  LeadPrecondition(self.driver, self.config).create_lead(lead1)
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
                CRMHomePage(self.driver).open_client_module() \
                    .select_filter(self.config.get_value(
                    TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                    .find_client_by_email(client1[LeadsModuleConstants.EMAIL])

                # Create LIVE account for client using MT4 Actions
                crm_client_profile = ClientProfilePage(self.driver)
                crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

                if (global_var.current_brand_name == "royal_cfds"):
                    MT4CreateAccountModule(self.driver) \
                        .create_account(
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_GROUP_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                        .click_ok()

                elif (global_var.current_brand_name == "q8"):
                    MT4CreateAccountModule(self.driver) \
                        .create_account_with_platform(
                        self.config.get_value(TestDataConstants.TRADING_PLATFORMS, TestDataConstants.TRADING_PLATFORM_MT4),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_GROUP_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                        .click_ok()

                elif (global_var.current_brand_name == "axa_markets"):
                    MT4CreateAccountModule(self.driver) \
                        .create_account(
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_GROUP_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE_400)) \
                        .click_ok()

                elif (global_var.current_brand_name == "xtraderfx") or (global_var.current_brand_name == "gxfx") or (global_var.current_brand_name == "b-traderfx"):
                    MT4CreateAccountModule(self.driver) \
                        .create_account(
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY_EUR),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_EUR),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                        .click_ok()

                else:
                    MT4CreateAccountModule(self.driver) \
                        .create_account(
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_GROUP_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_LEVERAGE_LIVE)) \
                        .click_ok()

                # Get account number to make deposit in future
                account_number = ClientProfilePage(self.driver) \
                    .perform_scroll_down() \
                    .open_trading_accounts_tab() \
                    .get_client_account()

                # Make deposit for account number using MT4 Actions
                crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.DEPOSIT)

                MT4DepositModule(self.driver).make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
                                                           CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                                           CRMConstants.STATUS_DEPOSIT, CRMConstants.DESCRIPTION_DEPOSIT)

                # Check confirmation message
                confirmation_message = crm_client_profile.get_confirm_message()
                self.assertEqual(confirmation_message, CRMConstants.DEPOSIT_SUCCESSFULLY)

                # Close popup
                crm_client_profile.click_ok() \
                    .refresh_page()

                deposit_amount_text = crm_client_profile.click_trading_accounts_tab() \
                    .get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)

                self.assertEqual(
                    CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT, deposit_amount_text, "Wrong deposit sum is displayed")

            except (ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                ClientProfilePage(self.driver).Sign_Out()
                # lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
                client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
                CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD))
                # # Create new lead and convert him to new client
                #  LeadPrecondition(self.driver, self.config).create_lead(lead1)
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
                CRMHomePage(self.driver).open_client_module() \
                    .select_filter(self.config.get_value(
                    TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                    .find_client_by_email(client1[LeadsModuleConstants.EMAIL])

                # Create LIVE account for client using MT4 Actions
                crm_client_profile = ClientProfilePage(self.driver)
                crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

                if (global_var.current_brand_name == "royal_cfds") or (global_var.current_brand_name == "newforexstaging"):
                    MT4CreateAccountModule(self.driver) \
                        .create_account(
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_GROUP_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                        .click_ok()

                elif (global_var.current_brand_name == "q8"):
                    MT4CreateAccountModule(self.driver) \
                        .create_account_with_platform(
                        self.config.get_value(TestDataConstants.TRADING_PLATFORMS,
                                              TestDataConstants.TRADING_PLATFORM_MT4),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_GROUP_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                        .click_ok()

                elif (global_var.current_brand_name == "axa_markets"):
                    MT4CreateAccountModule(self.driver) \
                        .create_account(
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_GROUP_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1,
                                              TestDataConstants.TRADING_LEVERAGE_400)) \
                        .click_ok()

                elif (global_var.current_brand_name == "xtraderfx"):
                    MT4CreateAccountModule(self.driver) \
                        .create_account(
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1,
                                              TestDataConstants.TRADING_CURRENCY_EUR),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_EUR),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                        .click_ok()

                else:
                    MT4CreateAccountModule(self.driver) \
                        .create_account(
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_SERVER_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_CURRENCY_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_GROUP_LIVE),
                        self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                              TestDataConstants.TRADING_LEVERAGE_LIVE)) \
                        .click_ok()

                # Get account number to make deposit in future
                account_number = ClientProfilePage(self.driver) \
                    .perform_scroll_down() \
                    .open_trading_accounts_tab() \
                    .get_client_account()

                # Make deposit for account number using MT4 Actions
                crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.DEPOSIT)

                MT4DepositModule(self.driver).make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
                                                           CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                                           CRMConstants.STATUS_DEPOSIT,
                                                           CRMConstants.DESCRIPTION_DEPOSIT)

                # Check confirmation message
                confirmation_message = crm_client_profile.get_confirm_message()
                self.assertEqual(confirmation_message, CRMConstants.DEPOSIT_SUCCESSFULLY)

                # Close popup
                crm_client_profile.click_ok() \
                    .refresh_page()

                deposit_amount_text = crm_client_profile.click_trading_accounts_tab() \
                    .get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)

                self.assertEqual(
                    CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT, deposit_amount_text, "Wrong deposit sum is displayed")

    def test_make_deposit_for_client_crm(self):
        # lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
        # client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
        #
        # # Create new lead and convert him to new client
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
        #
        # # ADD LIVE ACCOUNT IN CRM
        # # Open clients module. Find created client by email and open his profile
        # CRMHomePage(self.driver).open_client_module() \
        #     .select_filter(self.config.get_value(
        #     TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
        #     .find_client_by_email(client1[LeadsModuleConstants.EMAIL])
        #
        # # Create LIVE account for client using MT4 Actions
        # crm_client_profile = ClientProfilePage(self.driver)
        # crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)
        #
        # MT4CreateAccountModule(self.driver) \
        #     .create_account(
        #     self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
        #     self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
        #     self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
        #     self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE)) \
        #     .click_ok()
        try:
            crm_client_profile = CRMLoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD),
                           self.config.get_value(TestDataConstants.OTP_SECRET)) \
                .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

            # Get account number to make deposit in future. And get initial amount
            account_number = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .open_trading_accounts_tab() \
                .get_client_account()

            # Use when you need to compare amount before and after deposit
            # amount_initial = crm_client_profile.get_initial_amount()

            crm_client_profile \
                .perform_scroll_up() \
                .open_deposit_for_client_in_menu() \
                .fill_client_deposit_pop(account_number)

            # Check that CLIENT DEPOSIT CONFIRMATION page is closed and popup is still displayed
            self.assertTrue(CRMClientDeposit(self.driver).is_client_deposit_confirmation_page_not_displayed(),
                            "CLIENT DEPOSIT CONFIRMATION page is still displayed. But Payment Frame is expected")

            self.assertEqual(CRMConstants.TITLE_OF_CLIENT_DEPOSIT_POPUP,
                             CRMClientDeposit(self.driver).client_deposit_popup_title_text(),
                             "Client deposit popup is not displayed, but should")
        except (ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:
                ClientProfilePage(self.driver).Sign_Out()
                crm_client_profile = CRMLoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD),
                               self.config.get_value(TestDataConstants.OTP_SECRET)) \
                    .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                    .find_client_by_email(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

                # Get account number to make deposit in future. And get initial amount
                account_number = ClientProfilePage(self.driver) \
                    .perform_scroll_down() \
                    .open_trading_accounts_tab() \
                    .get_client_account()

                # Use when you need to compare amount before and after deposit
                # amount_initial = crm_client_profile.get_initial_amount()

                crm_client_profile \
                    .perform_scroll_up() \
                    .open_deposit_for_client_in_menu() \
                    .fill_client_deposit_pop(account_number)

                # Check that CLIENT DEPOSIT CONFIRMATION page is closed and popup is still displayed
                self.assertTrue(CRMClientDeposit(self.driver).is_client_deposit_confirmation_page_not_displayed(),
                                "CLIENT DEPOSIT CONFIRMATION page is still displayed. But Payment Frame is expected")

                self.assertEqual(CRMConstants.TITLE_OF_CLIENT_DEPOSIT_POPUP,
                                 CRMClientDeposit(self.driver).client_deposit_popup_title_text(),
                                 "Client deposit popup is not displayed, but should")

            # deposit_successful = CRMClientDeposit(self.driver)\
            #     .select_payment_method(CaConstants.VISA) \
            #     .set_card_number("4444444444444448") \
            #     .set_expiry_date("092020") \
            #     .set_cvc("123") \
            #     .set_amount_deposit(CaConstants.AMOUNT_DEPOSIT) \
            #     .perform_deposit() \
            #     .get_successful_deposit_message()
            #
            # self.assertEqual(CaConstants.SUCCESSFUL_DEPOSIT_MESSAGE, deposit_successful, "Transaction failed")
            except (ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                ClientProfilePage(self.driver).Sign_Out()
                crm_client_profile = CRMLoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD),
                               self.config.get_value(TestDataConstants.OTP_SECRET)) \
                    .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                    .find_client_by_email(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

                # Get account number to make deposit in future. And get initial amount
                account_number = ClientProfilePage(self.driver) \
                    .perform_scroll_down() \
                    .open_trading_accounts_tab() \
                    .get_client_account()

                # Use when you need to compare amount before and after deposit
                # amount_initial = crm_client_profile.get_initial_amount()

                crm_client_profile \
                    .perform_scroll_up() \
                    .open_deposit_for_client_in_menu() \
                    .fill_client_deposit_pop(account_number)

                # Check that CLIENT DEPOSIT CONFIRMATION page is closed and popup is still displayed
                self.assertTrue(CRMClientDeposit(self.driver).is_client_deposit_confirmation_page_not_displayed(),
                                "CLIENT DEPOSIT CONFIRMATION page is still displayed. But Payment Frame is expected")

                self.assertEqual(CRMConstants.TITLE_OF_CLIENT_DEPOSIT_POPUP,
                                 CRMClientDeposit(self.driver).client_deposit_popup_title_text(),
                                 "Client deposit popup is not displayed, but should")

            # deposit_successful = CRMClientDeposit(self.driver)\
            #     .select_payment_method(CaConstants.VISA) \
            #     .set_card_number("4444444444444448") \
            #     .set_expiry_date("092020") \
            #     .set_cvc("123") \
            #     .set_amount_deposit(CaConstants.AMOUNT_DEPOSIT) \
            #     .perform_deposit() \
            #     .get_successful_deposit_message()
            #
            # self.assertEqual(CaConstants.SUCCESSFUL_DEPOSIT_MESSAGE, deposit_successful, "Transaction failed")
