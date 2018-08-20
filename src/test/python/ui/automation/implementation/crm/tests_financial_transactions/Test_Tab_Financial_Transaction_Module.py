import pytest

from src.main.python.ui.crm.model.constants.FinancialTransactionsModuleConstants import \
    FinancialTransactionsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=27)
class TabFinancialTransaction(BaseTest):

    def test_check_all_tab_from_financial_transactions(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        financial_transaction_module = CRMHomePage().open_more_list_modules() \
            .select_financial_transactions_module_more_list(
            FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE)

        all_tab_name = financial_transaction_module.get_all_tab_text()
        credit_in_tab_name = financial_transaction_module.get_credit_in_tab_text()
        credit_out_name = financial_transaction_module.get_credit_out_tab_text()
        demo_accounts_name = financial_transaction_module.get_demo_accounts_transactions_tab_text()
        deposit_name = financial_transaction_module.get_deposits_tab_text()
        withdraw = financial_transaction_module.get_withdraw_tab_text()

        assert all_tab_name == Config.data.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.FIRST_TAB)
        assert credit_in_tab_name == Config.data.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.SECOND_TAB)
        assert credit_out_name == Config.data.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.THIRD_TAB)
        assert demo_accounts_name == Config.data.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.FOURTH_TAB)
        assert deposit_name == Config.data.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.FIFTH_TAB)
        assert withdraw == Config.data.get_data_financial_transactions_info(
            FinancialTransactionsModuleConstants.SIX_TAB)

    def test_check_searching_by_column(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        financial_transaction_information = CRMHomePage().open_more_list_modules() \
            .select_financial_transactions_module_more_list(
            FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE) \
            .open_first_transactions()

        trading_account = financial_transaction_information.get_trading_account_text()
        login = financial_transaction_information.get_login_text()
        client = financial_transaction_information.get_client_text()
        amount = financial_transaction_information.get_amount_text()
        currency = financial_transaction_information.get_currency_text()
        transaction_type = financial_transaction_information.get_transaction_type_text()
        transaction_numbe = financial_transaction_information.get_transaction_number_text()
        assigned_to = financial_transaction_information.get_assigned_to_text()
        get_brand = financial_transaction_information.get_brand_text()
        modified_time = financial_transaction_information.get_modified_time()
        crm_id = financial_transaction_information.get_crm_id()
