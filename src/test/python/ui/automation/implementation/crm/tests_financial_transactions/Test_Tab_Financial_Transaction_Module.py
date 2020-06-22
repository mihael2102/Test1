import pytest
from selenium.common.exceptions import NoSuchElementException

import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

from src.main.python.ui.crm.model.constants.FinancialTransactionsModuleConstants import \
    FinancialTransactionsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.financial_transactions.FinancialTransactionsPage import FinancialTransactionsPage
from selenium.common.exceptions import WebDriverException
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
import glob
import os
import csv
import xlrd


@pytest.mark.run(order=27)
class TabFinancialTransaction(BaseTest):

    def test_check_all_tab_from_financial_transactions(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        financial_transaction_module = CRMHomePage(self.driver)\
            .open_more_list_modules() \
            .select_financial_transactions_module_more_list(
                FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)

        all_tab_name = financial_transaction_module\
            .get_all_tab_text()
        credit_in_tab_name = financial_transaction_module\
            .get_credit_in_tab_text()
        credit_out_name = financial_transaction_module\
            .get_credit_out_tab_text()

        demo_accounts_name = financial_transaction_module\
            .get_demo_accounts_transactions_tab_text()
        deposit_name = financial_transaction_module\
            .get_deposits_tab_text()
        withdraw = financial_transaction_module\
            .get_withdraw_tab_text()

        assert all_tab_name == self.config.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.FIRST_TAB)
        assert credit_in_tab_name == self.config.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.SECOND_TAB)
        assert credit_out_name == self.config.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.THIRD_TAB)
        if global_var.current_brand_name != "newrichmarkets":
            assert demo_accounts_name == self.config.get_data_financial_transactions_info(
                FinancialTransactionsModuleConstants.FOURTH_TAB)
            assert deposit_name == self.config.get_data_financial_transactions_info(
                FinancialTransactionsModuleConstants.FIFTH_TAB)
            assert withdraw == self.config.get_data_financial_transactions_info(
                FinancialTransactionsModuleConstants.SIX_TAB)

    def test_check_searching_by_column(self):
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_data_client(TestDataConstants.USER_NAME),
                       self.config.get_data_client(TestDataConstants.CRM_PASSWORD),
                       self.config.get_data_client(TestDataConstants.OTP_SECRET))

        financial_transaction_list_page = CRMHomePage(self.driver)\
            .select_financial_transactions_module_more_list(
                FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE) \
            .perform_searching_trading_account_via_filters(
                client_name=FinancialTransactionsModuleConstants.CLIENT_TEST)

        # Get data of 3rd transaction (transaction's info will be changed when registration via CA starts to work):
        transaction_number = financial_transaction_list_page\
            .get_transaction_id_by_position_from_list()
        client_name = financial_transaction_list_page\
            .get_client_name_by_position_from_list()
        transaction_type_text = financial_transaction_list_page\
            .get_transaction_type_by_position_from_list()

        # Check that column exists:
        try:
            modified_time = financial_transaction_list_page.get_modified_time_by_position_from_list()[:10] + " - " + \
                                        financial_transaction_list_page.get_modified_time_by_position_from_list()[:10]
        except NoSuchElementException:
            modified_time = None

        transaction_number_from_its_details_page = financial_transaction_list_page\
            .perform_searching_trading_account_via_filters(transaction_number,
                                                           client_name,
                                                           transaction_type_text,
                                                           modified_time)\
            .open_first_financial_transaction_in_list()\
            .get_transaction_number_text()

        self.assertEqual(transaction_number, transaction_number_from_its_details_page,
                         "Wrong financial transaction was found. They have diffent transaction ID")

    def test_check_search_via_button(self):
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_data_client(TestDataConstants.USER_NAME),
                       self.config.get_data_client(TestDataConstants.CRM_PASSWORD),
                       self.config.get_data_client(TestDataConstants.OTP_SECRET))
        # Open module
        financial_transaction_list_page = CRMHomePage(self.driver) \
            .open_more_list_modules() \
            .select_financial_transactions_module_more_list(
                FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE) \
            .perform_searching_trading_account_via_filters(
                client_name=FinancialTransactionsModuleConstants.CLIENT_TEST)

        # Collect data for searching
        transaction_number = financial_transaction_list_page\
            .get_transaction_id_by_position_from_list()
        client_name = financial_transaction_list_page\
            .get_client_name_by_position_from_list()
        transaction_type_text = financial_transaction_list_page\
            .get_transaction_type_by_position_from_list()
        modified_time = financial_transaction_list_page\
            .get_modified_time_by_position_from_list()
        # trading_account = financial_transaction_list_page.get_trading_account_by_position_from_list()

        # Open search form
        financial_transaction_list_page\
            .open_search_form() \
            .open_advanced_search()
        # Search for transaction Id
        transaction_id_after_searching = financial_transaction_list_page\
            .search_for_transaction_id(transaction_number)\
            .get_transaction_id_by_position_from_list(1)
        self.assertEqual(transaction_number, transaction_id_after_searching, "Wrong transaction ID was found")

        # Search for client name. Search form is opened
        client_name_after_searching = financial_transaction_list_page\
            .search_for_client_name(client_name)\
            .get_client_name_by_position_from_list(1)
        self.assertEqual(client_name, client_name_after_searching, "Wrong client name was found")

        # Search for transaction type. Search form is opened
        transaction_type_after_searching = financial_transaction_list_page\
            .search_for_transaction_type(transaction_type_text)\
            .get_transaction_type_by_position_from_list(1)
        self.assertEqual(transaction_type_text, transaction_type_after_searching, "Wrong transaction type was found")

        # Search for modified time. Search form is opened
        is_modified_time_found = financial_transaction_list_page\
            .search_for_modified_time(modified_time)\
            .is_modified_time_in_search_results(modified_time)
        self.assertTrue(is_modified_time_found, "Wrong modified time was found")

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def test_export_financial_transactions_csv(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        financial_transaction_module = CRMHomePage(self.driver).open_more_list_modules() \
            .select_financial_transactions_module_more_list(
            FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)

        if global_var.current_brand_name == "4xfx" \
        or global_var.current_brand_name == "24btcmarket" or \
                (global_var.current_brand_name == "kontofx"):
            financial_transaction_module.enter_client_name(CRMConstants.EASY_SEARCH_CLIENT_TEST)
        else:
            financial_transaction_module.enter_client_name(CRMConstants.EASY_SEARCH_CLIENT)
        financial_transaction_module.click_search_button()
        financial_transaction_module.click_select_all_checkbox()

        transaction_number = financial_transaction_module.get_transaction_id_by_position_from_list()
        client_name = financial_transaction_module.get_client_name_by_position_from_list()
        transaction_type_text = financial_transaction_module.get_transaction_type_by_position_from_list()
        modified_time = financial_transaction_module.get_modified_time_by_position_from_list()

        financial_transaction_module.click_export()
        financial_transaction_module.click_export_pop_ups()
        sleep(10)
        # financial_transaction_module.click_save_as(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
        #                                                 LeadsModuleConstants.FIRST_NAME])

        list_of_files = glob.glob('C:/Users/Administrator/Downloads/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        path_to_latest_file = "%s" % latest_file
        count = 0
        with open(path_to_latest_file) as f_obj:
            reader = csv.reader(f_obj, delimiter=',')
            for line in reader:
                # print(line)
                if transaction_number and client_name and transaction_type_text and modified_time in line:
                    # print("String found in first row of csv")
                    count = count + 1

        # print(count)
        if count == 1:
            Logging().reportDebugStep(self, "Pass: checked csv file financial transactions")
        else:
            Logging().reportDebugStep(self, "Fail: checked csv file financial transactions")

        assert count == 1

    def test_export_financial_transactions_xls(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        financial_transaction_module = CRMHomePage(self.driver).open_more_list_modules() \
            .select_financial_transactions_module_more_list(
            FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)

        if (global_var.current_brand_name == "4xfx") or (global_var.current_brand_name == "24btcmarket") or (global_var.current_brand_name == "kontofx"):
            financial_transaction_module.enter_client_name(CRMConstants.EASY_SEARCH_CLIENT_TEST)
        else:
            financial_transaction_module.enter_client_name(CRMConstants.EASY_SEARCH_CLIENT)

        financial_transaction_module.click_search_button()
        financial_transaction_module.click_select_all_checkbox()

        transaction_number = financial_transaction_module.get_transaction_id_by_position_from_list()
        client_name = financial_transaction_module.get_client_name_by_position_from_list()
        transaction_type_text = financial_transaction_module.get_transaction_type_by_position_from_list()
        modified_time = financial_transaction_module.get_modified_time_by_position_from_list()

        financial_transaction_module.click_export()
        financial_transaction_module.select_xls_format()
        financial_transaction_module.click_export_pop_ups()
        sleep(10)
        list_of_files = glob.glob(
            'C:/Users/Administrator/Downloads/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        path_to_latest_file = "%s" % latest_file

        wb = xlrd.open_workbook(path_to_latest_file)

        sheet = wb.sheet_by_index(0)
        count = 0
        for row_num in range(sheet.nrows):
            row_value = sheet.row_values(row_num)
            if transaction_number and client_name and transaction_type_text and modified_time in row_value:
                # print(row_value)
                count = count + 1

        if count == 1:
            Logging().reportDebugStep(self, "Pass: checked excel file financial transactions")
        else:
            Logging().reportDebugStep(self, "Fail: checked excel file financial transactions")

        assert count == 1
