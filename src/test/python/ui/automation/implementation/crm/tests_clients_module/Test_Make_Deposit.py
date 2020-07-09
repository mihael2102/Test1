import pytest
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
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
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.run(order=13)
class DepositTestCRM(BaseTest):

    def test_make_deposit_crm(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        if (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "gmo"):
            ClientsPage(self.driver) \
                .find_client_by_fname(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME))
        else:
            ClientsPage(self.driver) \
                .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        # Create LIVE account for client using MT4 Actions
        crm_client_profile = ClientProfilePage(self.driver)
        crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

        if global_var.current_brand_name == "finmarket":
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value
                (TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE_OLD_FOREX),
                self.config.get_value
                (TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                self.config.get_value
                (TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE_FINMARKET),
                self.config.get_value
                (TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE))\
                .click_close()

        elif global_var.current_brand_name == "itrader" or global_var.current_brand_name == "gmo":
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                      TestDataConstants.TRADING_SERVER_LIVE_OLD_FOREX),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                CRMConstants.TRADING_LEVERAGE_ITRADER) \
                .click_close()
        else:
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                      TestDataConstants.TRADING_SERVER_LIVE_OLD_FOREX),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value
                (TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE)) \
                .click_close()
        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()
        # Make deposit for account number using MT4 Actions
        crm_client_profile.perform_scroll_up()
        # MT4DropDown(self.driver).mt4_actions(CRMConstants.DEPOSIT)
        crm_client_profile.open_mt4_actions(CRMConstants.DEPOSIT)
        if global_var.current_brand_name == "kayafx" or global_var.current_brand_name == "forex_staging":
            MT4DepositModule(self.driver).make_deposit_kaya(account_number, CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
                                                            CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                                            CRMConstants.DESCRIPTION_DEPOSIT,
                                                            CRMConstants.CLEARNED_BY)
        else:
            MT4DepositModule(self.driver).make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
                                                       CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                                       CRMConstants.DESCRIPTION_DEPOSIT)
        # Check confirmation message
        confirmation_message = crm_client_profile.get_confirm_message()
        if global_var.current_brand_name == "fxpmarkets":
            self.assertEqual(confirmation_message, CRMConstants.DEPOSIT_SUCCESSFULL_OLD_FOREX_FXP)
        elif global_var.current_brand_name == "forex_staging":
            sleep(2)
            pass
        else:
            self.assertEqual(confirmation_message, CRMConstants.DEPOSIT_SUCCESSFULL_OLD_FOREX)

        # Close popup
        crm_client_profile.click_ok()\
                          .refresh_page()

        crm_client_profile.click_trading_accounts_tab() \
                          .open_trading_account_page(account_number)

        balance = ClientProfilePage(self.driver).get_balance_in_trading_account()
        actual_balance = (balance.split('.'))[0]
        expected_balance = CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT

        # Check the balance was updated
        count = 0
        while actual_balance != expected_balance:
            sleep(2)
            CRMHomePage(self.driver).refresh_page()
            sleep(5)
            balance = ClientProfilePage(self.driver).get_balance_in_trading_account()
            actual_balance = (balance.split('.'))[0]
            count += 1
            if count == 7:
                break
        self.assertEqual(expected_balance, actual_balance, "Wrong deposit sum is displayed")

    def test_make_deposit_for_client_crm(self):
        # Tests precondition: test_perform_convert_lead, fill_questioner_new_client, test_crm_open_trading_account
        # CRM Login
        crm_client_profile = CRMLoginPage(self.driver) \
             .open_first_tab_page(self.config.get_value('url')) \
             .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                        self.config.get_value(TestDataConstants.CRM_PASSWORD),
                        self.config.get_value(TestDataConstants.OTP_SECRET)) \
             .select_filter(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        if (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "gmo"):
            ClientsPage(self.driver) \
                .find_client_by_fname(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME))
        else:
            ClientsPage(self.driver) \
                .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        # Get account number to make deposit in future. And get initial amount
        account_number = ClientProfilePage(self.driver)\
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        # amount_initial = crm_client_profile.get_initial_amount()

        crm_client_profile \
            .perform_scroll_up()
        ClientProfilePage(self.driver) \
            .open_deposit_for_client_in_menu()\
            .fill_client_deposit_pop(account_number)

        # Check that CLIENT DEPOSIT CONFIRMATION page is closed and popup is still displayed
        self.assertTrue(CRMClientDeposit(self.driver).is_client_deposit_confirmation_page_not_displayed(),
                        "CLIENT DEPOSIT CONFIRMATION page is still displayed. But Payment Frame is expected")
        self.assertEqual(CRMConstants.TITLE_OF_CLIENT_DEPOSIT_POPUP,
                         CRMClientDeposit(self.driver).client_deposit_popup_title_text(),
                         "Client deposit popup is not displayed, but should")
