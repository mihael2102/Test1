from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.utils.preconditions.filter.FilterPrecondition import FilterPrecondition


class FilterModulesTest(BaseTest):

    def test_create_filter_clients_module(self):
        clients_module_page = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_data_client(TestDataConstants.USER_NAME),
                       self.config.get_data_client(TestDataConstants.CRM_PASSWORD),
                       self.config.get_data_client(TestDataConstants.OTP_SECRET))

        FilterPrecondition(self.driver, self.config).create_filter_clients_module()

        first_name__column = clients_module_page.get_first_name_column()
        second_name_column = clients_module_page.get_second_name_column()
        third_name__column = clients_module_page.get_third_name_column()
        fourth_name_column = clients_module_page.get_fourth_name_column()
        fifth_name_column = clients_module_page.get_fifth_name_column()
        sixth_name_column = clients_module_page.get_sixth_name_column()
        seventh_name_column = clients_module_page.get_seventh_name_column()
        eighth_name_column = clients_module_page.get_eighth_name_column()
        ninth_name_column = clients_module_page.get_ninth_name_column()
        tenth_name_column = clients_module_page.get_tenth_name_column()
        eleventh_name_column = clients_module_page.get_eleventh_name_column()

        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.FIRST_COLUMN) == first_name__column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.SECOND_COLUMN) == second_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.THIRD_COLUMN) == third_name__column
        assert CRMConstants.FOURTH_COLUMN_OTHER_TYPE == fourth_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FIFTH_COLUMN) == fifth_name_column
        assert CRMConstants.SIXTH_COLUMN_OTHER_TYPE == sixth_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.SEVENTH_COLUMN) == seventh_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.EIGHTH_COLUMN) == eighth_name_column
        assert CRMConstants.NINTH_COLUMN_OTHER_TYPE == ninth_name_column
        assert CRMConstants.TENTH_COLUMN_OTHER_TYPE == tenth_name_column
        assert self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER,
                                           CRMConstants.ELEVENTH_COLUMN) == eleventh_name_column

    def test_create_filter_documents_module(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        FilterPrecondition(self.driver, self.config).create_filter_documents_module()

        documents_module_page = DocumentsPage(self.driver)
        first_name__column = documents_module_page.get_first_name_column()
        second_name_column = documents_module_page.get_second_name_column()
        third_name__column = documents_module_page.get_third_name_column()
        fourth_name_column = documents_module_page.get_fourth_name_column()
        
        assert self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                                DocumentModuleConstants.FIRST_COLUMN) == first_name__column
        assert self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                                DocumentModuleConstants.SECOND_COLUMN) == second_name_column
        assert self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                                DocumentModuleConstants.THIRD_COLUMN) == third_name__column
        self.assertEqual(fourth_name_column, DocumentModuleConstants.FOURTH_COLUMN_TEXT,
                                                                "Filter columns are different in Documents module")

    def test_create_filter_leads_module(self):
        CRMLoginPage(self.driver).open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        FilterPrecondition(self.driver, self.config).create_filter_leads_module()

    def test_create_filter_help_desk(self):
        CRMLoginPage(self.driver).open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        FilterPrecondition(self.driver, self.config).create_filter_help_desk()

    def test_create_filter_trading_account_module(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        FilterPrecondition(self.driver, self.config).create_filter_trading_account_module()
