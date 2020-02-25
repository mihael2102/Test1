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
from src.main.python.ui.crm.model.constants.MT4ModuleConstants import MT4ModuleConstants
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.side_bar.SidebarModules import SidebarModules
from src.main.python.ui.ca.model.constants.questionnaire.QuesDualixConstants import QuesDualixConstants
from src.main.python.ui.ca.model.constants.questionnaire.QuesStrattonConstants import QuesStrattonConstants
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


@pytest.mark.run(order=13)
class DepositTestCRM(BaseTest):

    def test_make_deposit_crm(self):
        lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
        client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url'))\
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        # ADD LIVE ACCOUNT IN CRM
        # Open clients module. Find created client by email and open his profile
        CRMHomePage(self.driver)\
            .open_client_module()\
            .select_filter(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        if global_var.current_brand_name == "confixfinancial" or \
                global_var.current_brand_name == "marketrip":
            ClientsPage(self.driver) \
                .find_client_by_email(lead1[LeadsModuleConstants.EMAIL])
        else:
            ClientsPage(self.driver) \
                .find_client_by_email(client1[LeadsModuleConstants.EMAIL])

        # Fill Questionnaire
        if global_var.current_brand_name == "dualix":
            SidebarModules(self.driver)\
                .open_view_edit_questionnaire() \
                .select_item_pick_list(QuesDualixConstants.LIST_1, QuesDualixConstants.ITEM_1) \
                .select_item_pick_list(QuesDualixConstants.LIST_2, QuesDualixConstants.ITEM_2) \
                .select_item_pick_list(QuesDualixConstants.LIST_3, QuesDualixConstants.ITEM_3) \
                .select_item_pick_list(QuesDualixConstants.LIST_4, QuesDualixConstants.ITEM_4) \
                .select_item_pick_list(QuesDualixConstants.LIST_5, QuesDualixConstants.ITEM_5) \
                .select_item_pick_list(QuesDualixConstants.LIST_6, QuesDualixConstants.ITEM_6) \
                .open_section(QuesDualixConstants.SECTION_KNOWLEDGE) \
                .select_item_pick_list(QuesDualixConstants.LIST_7, QuesDualixConstants.ITEM_7) \
                .select_item_pick_list(QuesDualixConstants.LIST_8, QuesDualixConstants.ITEM_8) \
                .select_item_pick_list(QuesDualixConstants.LIST_9, QuesDualixConstants.ITEM_9) \
                .select_item_pick_list(QuesDualixConstants.LIST_10, QuesDualixConstants.ITEM_10) \
                .select_item_pick_list(QuesDualixConstants.LIST_11, QuesDualixConstants.ITEM_11) \
                .select_item_pick_list(QuesDualixConstants.LIST_12, QuesDualixConstants.ITEM_12) \
                .select_item_pick_list(QuesDualixConstants.LIST_13, QuesDualixConstants.ITEM_13) \
                .select_item_pick_list(QuesDualixConstants.LIST_14, QuesDualixConstants.ITEM_14) \
                .select_item_pick_list(QuesDualixConstants.LIST_15, QuesDualixConstants.ITEM_15) \
                .select_item_pick_list(QuesDualixConstants.LIST_16, QuesDualixConstants.ITEM_16) \
                .select_item_pick_list(QuesDualixConstants.LIST_17, QuesDualixConstants.ITEM_17) \
                .select_item_pick_list(QuesDualixConstants.LIST_18, QuesDualixConstants.ITEM_18) \
                .select_item_pick_list(QuesDualixConstants.LIST_19, QuesDualixConstants.ITEM_19) \
                .select_item_pick_list(QuesDualixConstants.LIST_20, QuesDualixConstants.ITEM_20) \
                .select_item_pick_list(QuesDualixConstants.LIST_21, QuesDualixConstants.ITEM_21) \
                .select_item_pick_list(QuesDualixConstants.LIST_22, QuesDualixConstants.ITEM_22) \
                .select_item_pick_list(QuesDualixConstants.LIST_23, QuesDualixConstants.ITEM_23_CRM) \
                .open_section(QuesDualixConstants.SECTION_PERS_PROFILE) \
                .select_item_pick_list(QuesDualixConstants.LIST_24, QuesDualixConstants.ITEM_24) \
                .set_text_field(QuesDualixConstants.FIELD_1, QuesDualixConstants.SSN) \
                .select_item_pick_list(QuesDualixConstants.LIST_25, QuesDualixConstants.ITEM_25) \
                .set_text_field(QuesDualixConstants.FIELD_2, QuesDualixConstants.ID) \
                .set_text_field(QuesDualixConstants.FIELD_3, QuesDualixConstants.COMPANY_NAME) \
                .click_save_btn() \
                .get_success_message() \
                .click_ok() \
                .refresh_page()
        if global_var.current_brand_name == "strattonmarkets-eu":
            SidebarModules(self.driver)\
                .open_view_edit_questionnaire() \
                .select_item_pick_list(QuesStrattonConstants.LIST_1, QuesStrattonConstants.EMPLOYMENT_STATUS_STUDENT) \
                .select_item_pick_list(QuesStrattonConstants.LIST_2, QuesStrattonConstants.EDUCATION_LEVEL_NO_EDUCATION) \
                .select_item_pick_list(QuesStrattonConstants.LIST_3, QuesStrattonConstants.POLITICALLY_EXPOSED_PERSON_NO) \
                .select_item_pick_list(QuesStrattonConstants.LIST_4, QuesStrattonConstants.TOTAL_ANNUAL_INCOME_OVER_700) \
                .select_item_pick_list(QuesStrattonConstants.LIST_5, QuesStrattonConstants.APPROXIMATE_NET_WEALTH_OVER_700) \
                .select_item_pick_list(QuesStrattonConstants.LIST_6, QuesStrattonConstants.EXPECTED_DEPOSIT_OVER_350) \
                .select_item_pick_list(QuesStrattonConstants.LIST_7, QuesStrattonConstants.SOURCE_TRADING_FUNDS_EMPLOYMENT) \
                .select_item_pick_list(QuesStrattonConstants.LIST_8, QuesStrattonConstants.WHY_WANT_TRADE_SPECULATIVE) \
                .select_item_pick_list(QuesStrattonConstants.LIST_9, QuesStrattonConstants.REACT_ON_LOSSES_NO_BIG_DEAL) \
                .open_section(QuesStrattonConstants.SECTION_KNOWLEDGE) \
                .select_item_pick_list(QuesStrattonConstants.LIST_10, QuesStrattonConstants.INSTRUMENTS_TRADED_BEFORE_BOTH_ABOVE) \
                .select_item_pick_list(QuesStrattonConstants.LIST_10_1, QuesStrattonConstants.AVERAGE_FREQUENCY_20) \
                .select_item_pick_list(QuesStrattonConstants.LIST_10_2, QuesStrattonConstants.TRADE_SIZE_MORE_10000) \
                .select_item_pick_list(QuesStrattonConstants.LIST_10_3, QuesStrattonConstants.COMMON_LEVEL_ABOVE_30) \
                .select_item_pick_list(QuesStrattonConstants.LIST_11, QuesStrattonConstants.IF_APPLICABLE_BOTH_ABOVE) \
                .select_item_pick_list(QuesStrattonConstants.LIST_12, QuesStrattonConstants.REGARDING_CFD_RETAIL) \
                .select_item_pick_list(QuesStrattonConstants.LIST_13, QuesStrattonConstants.FACTOR_AFFECT_PRICES_EMPLOYEE_LAYOFFS_RETAIL) \
                .select_item_pick_list(QuesStrattonConstants.LIST_14, QuesStrattonConstants.WHERE_CLOSE_BMW_POSITION_RETAIL) \
                .select_item_pick_list(QuesStrattonConstants.LIST_15, QuesStrattonConstants.REQUIRED_MARGIN_1000) \
                .select_item_pick_list(QuesStrattonConstants.LIST_16, QuesStrattonConstants.LOSS_AMOUNT_450) \
                .open_section(QuesStrattonConstants.SECTION_PERS_PROFILE) \
                .select_item_pick_list(QuesStrattonConstants.LIST_18, QuesStrattonConstants.COUNTRY_TAX) \
                .set_text_field(QuesStrattonConstants.FIELD_1, QuesStrattonConstants.SSN_TIN) \
                .select_item_pick_list(QuesStrattonConstants.LIST_19, QuesStrattonConstants.US) \
                .set_text_field(QuesStrattonConstants.FIELD_2, QuesStrattonConstants.NAT_ID) \
                .set_text_field(QuesStrattonConstants.FIELD_3, QuesStrattonConstants.COMPANY_NAME) \
                .click_save_btn() \
                .get_success_message() \
                .click_ok() \
                .refresh_page()

        # Create LIVE account for client using MT4 Actions
        crm_client_profile = ClientProfilePage(self.driver)
        crm_client_profile.check_create_mt_user_btn()
        crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

        if global_var.current_brand_name == "q8":
            MT4CreateAccountModule(self.driver)\
                .create_account_with_platform(
                self.config.get_value(TestDataConstants.TRADING_PLATFORMS, TestDataConstants.TRADING_PLATFORM_MT4),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200)) \
                .click_ok()
        else:
            MT4CreateAccountModule(self.driver) \
                .create_account(
                    var.get_var(self.__class__.__name__)["live_acc_server"],
                    var.get_var(self.__class__.__name__)["live_acc_currency"],
                    var.get_var(self.__class__.__name__)["live_acc_group"],
                    var.get_var(self.__class__.__name__)["live_acc_leverage"]) \
                .click_ok()

        # Get account number to make deposit in future
        account_number = ClientProfilePage(self.driver) \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        # Make deposit for account number using MT4 Actions
        crm_client_profile.perform_scroll_up()
        if global_var.current_brand_name == "trade99":
            crm_client_profile.open_mt4_actions(CRMConstants.DEPOSIT2)
        else:
            crm_client_profile.open_mt4_actions(CRMConstants.DEPOSIT)

        if global_var.current_brand_name == "trade99":
            MT4DepositModule(self.driver)\
                .make_deposit(account_number,
                              CRMConstants.AMOUNT_DEPOSIT_BTC,
                              CRMConstants.PAYMENT_METHOD_DEPOSIT,
                              CRMConstants.STATUS_DEPOSIT,
                              CRMConstants.DESCRIPTION_DEPOSIT)
        else:
            MT4DepositModule(self.driver)\
                .make_deposit(account_number,
                              CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
                              CRMConstants.PAYMENT_METHOD_DEPOSIT,
                              CRMConstants.STATUS_DEPOSIT,
                              CRMConstants.DESCRIPTION_DEPOSIT)

        # Check confirmation message
        confirmation_message = crm_client_profile.get_confirm_message()
        try:
            self.assertEqual(confirmation_message, CRMConstants.DEPOSIT_SUCCESSFULLY)
        except:
            self.assertEqual(confirmation_message, CRMConstants.DEPOSIT_SUCCESSFULLY_2)

        # Close popup
        crm_client_profile\
            .click_ok()\
            .refresh_page()

        if global_var.current_brand_name == "trade99":
            deposit_amount_text = crm_client_profile\
                .click_trading_accounts_tab() \
                .get_amount_text(CRMConstants.AMOUNT_DEPOSIT_BTC)
            self.assertEqual(
                CRMConstants.AMOUNT_DEPOSIT_BTC, deposit_amount_text,
                "Wrong deposit sum is displayed")
        else:
            deposit_amount_text = crm_client_profile\
                .click_trading_accounts_tab() \
                .get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)
            self.assertEqual(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT, deposit_amount_text,
                             "Wrong deposit sum is displayed")

    def test_make_deposit_for_client_crm(self):
        crm_client_profile = CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url'))\
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))\
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))\
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
