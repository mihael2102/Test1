import pytest
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.constants.MT4ModuleConstants import MT4ModuleConstants
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
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.test.python.ui.automation.utils.preconditions.credit_in.Credit_In_Precondition import \
    CreditInPrecondition
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsInformationPage import \
    TradingAccountsInformationPage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import NoSuchElementException
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from time import sleep
import time


@pytest.mark.run(order=1)
class CreditInTestCRM(BaseTest):

    def test_make_credit_in_from_crm(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CreditInPrecondition(self.driver, self.config)\
            .add_live_account_in_crm()\
            .click_ok()

        # Take number of account
        account_number = ClientProfilePage(self.driver)\
            .perform_scroll_down()\
            .open_trading_accounts_tab()\
            .get_client_account()

        if global_var.current_brand_name == "trade99":
            ClientProfilePage(self.driver)\
                .perform_scroll_up()\
                .open_mt4_actions(CRMConstants.CREDIT_IN2)
            MT4CreditInModule(self.driver)\
                .make_credit_in(account_number,
                                CRMConstants.AMOUNT_CREDIT_IN_BTC,
                                CRMConstants.EXPIRE_DATE.strftime(CRMConstants.FORMAT_DATE),
                                CRMConstants.CREDIT_IN_COMMENT) \
                .click_ok() \
                .refresh_page()
        else:
            ClientProfilePage(self.driver)\
                .perform_scroll_up().open_mt4_actions(CRMConstants.CREDIT_IN)

            MT4CreditInModule(self.driver)\
                .make_credit_in(account_number,
                                CRMConstants.AMOUNT_CREDIT_IN,
                                CRMConstants.EXPIRE_DATE.strftime(CRMConstants.FORMAT_DATE),
                                CRMConstants.CREDIT_IN_COMMENT)\
                .click_ok()\
                .refresh_page()
        time.sleep(3)
        MT4CreditInModule(self.driver).refresh_page()
        # Check the Credit In amount
        credit_in_amount = ClientProfilePage(self.driver)\
            .perform_scroll_down()\
            .get_amount_of_credit_in()     # Get amount from block 'Trading Accounts'

        counter = 0
        if global_var.current_brand_name == "trade99":
            expected_credit = CRMConstants.AMOUNT_CREDIT_IN_BTC
        else:
            expected_credit = CRMConstants.AMOUNT_CREDIT_IN

        while expected_credit != credit_in_amount:
            MT4CreditInModule(self.driver).refresh_page()
            credit_in_amount = ClientProfilePage(self.driver) \
                .perform_scroll_down() \
                .get_amount_of_credit_in()
            counter += 1
            if counter == 7:
                break

        assert expected_credit == credit_in_amount

    def test_credit_in_crm_new_ui(self):
        self.config.get_value(TestDataConstants.CLIENT_ONE)
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        CreditInPrecondition(self.driver, self.config) \
            .add_live_account_in_crm_new_ui() \
            .click_ok()

        # Get account number to make credit in
        account_number = ClientProfilePage(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS) \
            .get_ta_number()

        MT4ModuleConstants.ACCOUNT_NUMBER_CREDIT = account_number

        # Make Credit in
        MT4DropDown(self.driver) \
            .open_mt4_module_newui(CRMConstants.CREATE_MT_CREDIT_IN)

        if global_var.current_brand_name == "trade99":
            MT4CreditInModule(self.driver) \
                .make_credit_in_new_ui(account_number,
                                       CRMConstants.AMOUNT_CREDIT_IN_BTC,
                                       MT4ModuleConstants.CREDIT_IN_EXPIRE_DAY,
                                       MT4ModuleConstants.CREDIT_IN_EXPIRE_MONTH,
                                       MT4ModuleConstants.CREDIT_IN_EXPIRE_YEAR,
                                       MT4ModuleConstants.CREDIT_IN_GARANTED_BY,
                                       MT4ModuleConstants.CREDIT_IN_COMMENT)
        else:
            MT4CreditInModule(self.driver) \
                .make_credit_in_new_ui(account_number,
                                       CRMConstants.AMOUNT_CREDIT_IN,
                                       MT4ModuleConstants.CREDIT_IN_EXPIRE_DAY,
                                       MT4ModuleConstants.CREDIT_IN_EXPIRE_MONTH,
                                       MT4ModuleConstants.CREDIT_IN_EXPIRE_YEAR,
                                       MT4ModuleConstants.CREDIT_IN_GARANTED_BY,
                                       MT4ModuleConstants.CREDIT_IN_COMMENT)

        # Check confirmation message
        MT4CreateAccountModule(self.driver) \
            .verify_success_message()
        CRMHomePage(self.driver) \
            .click_ok()

        # Check the balance updated
        ClientProfilePage(self.driver) \
            .refresh_page() \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS) \
            .open_trading_account_by_number(account_number)

        MT4CreditInModule(self.driver)\
            .refresh_page()
        # Check the Credit In amount
        credit_in_amount = TradingAccountsInformationPage(self.driver) \
            .get_credit_text()

        if credit_in_amount[0] != 0:
            credit_in_amount = credit_in_amount.split('.')[0]

        if global_var.current_brand_name == "trade99":
            expected_credit = CRMConstants.AMOUNT_CREDIT_IN_BTC
        else:
            expected_credit = CRMConstants.AMOUNT_CREDIT_IN.split('.')[0]

        counter = 0
        while expected_credit != credit_in_amount:
            MT4CreditInModule(self.driver)\
                .refresh_page()
            credit_in_amount = TradingAccountsInformationPage(self.driver) \
                .get_credit_text()
            if credit_in_amount[0] != 0:
                credit_in_amount = credit_in_amount.split('.')[0]
            counter += 1
            if counter == 7:
                break

        assert expected_credit == credit_in_amount

        """ Verify data in info tag Credit was updated """
        credit_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_CREDIT)
        if global_var.current_brand_name == "trade99":
            assert CRMConstants.AMOUNT_CREDIT_IN_BTC in credit_tag
        else:
            assert CRMConstants.AMOUNT_CREDIT_IN.split('.')[0] in credit_tag

        """ Verify data in info tag Equity, Free Margin were updated """
        equity_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_EQUITY)
        free_margin_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_FREE_MARGIN)
        if global_var.current_brand_name == "trade99":
            expected_equity = (float(CRMConstants.AMOUNT_DEPOSIT_BTC) -
                               float(CRMConstants.AMOUNT_WITHDRAW_BTC)) + \
                              float(CRMConstants.AMOUNT_CREDIT_IN_BTC)
            assert str(expected_equity) in equity_tag
            assert str(expected_equity) in free_margin_tag
        else:
            expected_equity = (int(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split('.')[0]) -
                               int(CRMConstants.AMOUNT_WITHDRAW)) + \
                               int(CRMConstants.AMOUNT_CREDIT_IN.split('.')[0])
            assert str(expected_equity) in equity_tag
            assert str(expected_equity) in free_margin_tag

    def test_make_credit_in_crm(self):
        pass
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
