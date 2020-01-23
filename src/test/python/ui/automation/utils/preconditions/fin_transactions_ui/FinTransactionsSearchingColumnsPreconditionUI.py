from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.fin_transactions_ui.FinTransactionsModuleConstantsUI import \
    FinTransactionsModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI


class FinTransactionsSearchingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def fin_transactions_searching_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                self.config.get_value('url'),
                self.config.get_value(TestDataConstants.USER_NAME),
                self.config.get_value(TestDataConstants.CRM_PASSWORD),
                self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Financial Transactions module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_FIN_TRANSACTIONS) \
            .open_tab_list_view_ui(FinTransactionsModuleConstantsUI.TAB_ALL)

        """ Get data from the first row of list view """
        transaction_no = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=FinTransactionsModuleConstantsUI.COLUMN_TRANSACTION_NO,
                                        row=FinTransactionsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        login = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=FinTransactionsModuleConstantsUI.COLUMN_LOGIN,
                                        row=FinTransactionsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        client = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=FinTransactionsModuleConstantsUI.COLUMN_CLIENT,
                                        row=FinTransactionsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        transaction_type = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=FinTransactionsModuleConstantsUI.COLUMN_T_TYPE,
                                        row=FinTransactionsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        payment_type = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=FinTransactionsModuleConstantsUI.COLUMN_P_TYPE,
                                        row=FinTransactionsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """
        search = GlobalTablePageUI(self.driver)
        if transaction_no:
            search\
                .set_data_column_field(column=FinTransactionsModuleConstantsUI.COLUMN_TRANSACTION_NO,
                                       data=transaction_no)
        if login:
            search\
                .set_data_column_field(column=FinTransactionsModuleConstantsUI.COLUMN_LOGIN,
                                       data=login)
        if client:
            search\
                .set_data_column_field(column=FinTransactionsModuleConstantsUI.COLUMN_CLIENT,
                                       data=client)
        if transaction_type:
            search\
                .select_data_column_field(column=FinTransactionsModuleConstantsUI.COLUMN_T_TYPE,
                                          data=transaction_type)
        if payment_type:
            search\
                .select_data_column_field(column=FinTransactionsModuleConstantsUI.COLUMN_P_TYPE,
                                          data=payment_type)

        """ Verify correct data found """
        result = GlobalTablePageUI(self.driver)
        if transaction_no:
            result\
                .global_data_checker_new_ui(transaction_no)
        if login:
            result\
                .global_data_checker_new_ui(login)
        if client:
            result\
                .global_data_checker_new_ui(client)
        if transaction_type:
            result\
                .global_data_checker_new_ui(transaction_type)
        if payment_type:
            result\
                .global_data_checker_new_ui(payment_type)

        """ Verify, only 1 record was found """
        number_records = CRMBaseMethodsPage(self.driver)\
            .get_number_records()
        assert number_records == 1
