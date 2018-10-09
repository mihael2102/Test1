import pytest
from selenium.common.exceptions import NoSuchElementException

import src.main.python.utils.data.globals.Globals as global_var

from src.main.python.ui.crm.model.constants.FinancialTransactionsModuleConstants import \
    FinancialTransactionsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=27)
class TabFinancialTransaction(BaseTest):

    def test_check_all_tab_from_financial_transactions(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        financial_transaction_module = CRMHomePage(self.driver).open_more_list_modules() \
            .select_financial_transactions_module_more_list(
            FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)

        all_tab_name = financial_transaction_module.get_all_tab_text()
        credit_in_tab_name = financial_transaction_module.get_credit_in_tab_text()
        credit_out_name = financial_transaction_module.get_credit_out_tab_text()
        demo_accounts_name = financial_transaction_module.get_demo_accounts_transactions_tab_text()
        deposit_name = financial_transaction_module.get_deposits_tab_text()
        withdraw = financial_transaction_module.get_withdraw_tab_text()

        assert all_tab_name == self.config.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.FIRST_TAB)
        assert credit_in_tab_name == self.config.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.SECOND_TAB)
        assert credit_out_name == self.config.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.THIRD_TAB)
        assert demo_accounts_name == self.config.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.FOURTH_TAB)
        assert deposit_name == self.config.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.FIFTH_TAB)
        assert withdraw == self.config.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.SIX_TAB)

    def test_check_searching_by_column(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_data_client(TestDataConstants.USER_NAME),
                       self.config.get_data_client(TestDataConstants.CRM_PASSWORD),
                       self.config.get_data_client(TestDataConstants.OTP_SECRET))

        financial_transaction_list_page = CRMHomePage(self.driver) \
                                                .select_financial_transactions_module_more_list(
                                                    FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)

        # Get data of 3rd transaction (transaction's info will be changed when registration via CA starts to work)
        transaction_number = financial_transaction_list_page.get_transaction_id_by_position_from_list()
        client_name = financial_transaction_list_page.get_client_name_by_position_from_list()
        transaction_type_text = financial_transaction_list_page.get_transaction_type_by_position_from_list()
        try:
            modified_time = financial_transaction_list_page.get_modified_time_by_position_from_list()[:10] + " - " + \
                                            financial_transaction_list_page.get_modified_time_by_position_from_list()[:10]
            # trading_account = financial_transaction_list_page.get_trading_account_by_position_from_list()
        except NoSuchElementException:
            pass

        # TIME and Trading Account columns are absent on some brands: 'mpcrypto'.
        # So we skip this column during searching in this case.
        # Details of checking please see in search method below
        transaction_number_from_its_details_page = financial_transaction_list_page\
                                            .perform_searching_trading_account_via_filters(transaction_number,
                                                                                           client_name,
                                                                                           transaction_type_text,
                                                                                           modified_time)\
                                            .open_first_financial_transaction_in_list()\
                                            .get_transaction_number_text()

        self.assertEqual(transaction_number, transaction_number_from_its_details_page,
                                            "Wrong financial transaction was found. They have diffent transaction ID")

        # CRMLoginPage().open_first_tab_page(Config.url_crm) \
        #     .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
        #                self.config.get_value(TestDataConstants.CRM_PASSWORD),
        #                self.config.get_value(TestDataConstants.OTP_SECRET))

        # financial_transaction_information = CRMHomePage().open_more_list_modules() \
        #     .select_financial_transactions_module_more_list(
        #     FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE) \
        #     .open_first_transactions()
        #
        # trading_account = financial_transaction_information.get_trading_account_text()
        # login = financial_transaction_information.get_login_text()
        # client = financial_transaction_information.get_client_text()
        # amount = financial_transaction_information.get_amount_text()
        # currency = financial_transaction_information.get_currency_text()
        # transaction_type = financial_transaction_information.get_transaction_type_text()
        # transaction_numbe = financial_transaction_information.get_transaction_number_text()
        # assigned_to = financial_transaction_information.get_assigned_to_text()
        # get_brand = financial_transaction_information.get_brand_text()
        # modified_time = financial_transaction_information.get_modified_time()
        # crm_id = financial_transaction_information.get_crm_id()

    def test_check_search_via_button(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_data_client(TestDataConstants.USER_NAME),
                       self.config.get_data_client(TestDataConstants.CRM_PASSWORD),
                       self.config.get_data_client(TestDataConstants.OTP_SECRET))
        # Open module
        financial_transaction_list_page = CRMHomePage(self.driver) \
            .open_more_list_modules() \
            .select_financial_transactions_module_more_list(
            FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)

        # Collect data for searching
        transaction_number = financial_transaction_list_page.get_transaction_id_by_position_from_list()
        client_name = financial_transaction_list_page.get_client_name_by_position_from_list()
        transaction_type_text = financial_transaction_list_page.get_transaction_type_by_position_from_list()
        modified_time = financial_transaction_list_page.get_modified_time_by_position_from_list()
        # trading_account = financial_transaction_list_page.get_trading_account_by_position_from_list()

        # Open search form
        financial_transaction_list_page.open_search_form()
        # Search for transaction Id
        transaction_id_after_searching = financial_transaction_list_page.search_for_transaction_id(transaction_number)\
                                                                            .get_transaction_id_by_position_from_list(1)
        self.assertEqual(transaction_number, transaction_id_after_searching, "Wrong transaction ID was found")

        # Search for client name. Search form is opened
        client_name_after_searching = financial_transaction_list_page.search_for_client_name(client_name).get_client_name_by_position_from_list(1)
        self.assertEqual(client_name, client_name_after_searching, "Wrong client name was found")

        # Search for transaction type. Search form is opened
        transaction_type_after_searching = financial_transaction_list_page.search_for_transaction_type(
            transaction_type_text).get_transaction_type_by_position_from_list(1)
        self.assertEqual(transaction_type_text, transaction_type_after_searching, "Wrong transaction type was found")

        # Search for modified time. Search form is opened
        is_modified_time_found = financial_transaction_list_page.search_for_modified_time(modified_time)\
                                                                .is_modified_time_in_search_results(modified_time)
        self.assertTrue(is_modified_time_found, "Wrong modified time was found")

        # Search for trading account. Search form is opened
        # trading_account_after_searching = financial_transaction_list_page.search_for_trading_account(trading_account).get_trading_account_by_position_from_list(1)
        # self.assertEqual(trading_account,trading_account_after_searching, "Wrong modified time was found")
