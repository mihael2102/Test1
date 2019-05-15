from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.modules.tasks_module.EditEventModule import EditEventModule
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage
import pytest

class DocumentPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def create_document(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        document_module = CRMHomePage(self.driver).open_more_list_modules().select_documents_module_more_list(DocumentModuleConstants.DOCUMENT)
        document_module.open_create_document_module()
        document_module.browse_documents()
        document_module.select_document_type(CRMConstants.DOCUMENT_TYPE)
        document_module.select_document_status(CRMConstants.DOCUMENT_STATUS)
        # document_module.select_document_sub_type(CRMConstants.DOCUMENT_SUB_TYPE)
        # document_module.input_message(CRMConstants.DOCUMENT_COMMENTS)
        # document_module.input_expiry_date(CRMConstants.SECOND_DATE.strftime(
        #                                                 CRMConstants.FORMAT_DATE_YEARS))

        document_module.attached_to(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])
        document_module.fill_title(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])
        document_module.save_document()
        # assert document_module.get_successful_message() == CRMConstants.DOCUMENT_SUCCESSFUL_MESSAGE

    def verified_document(self):

        document_module = CRMHomePage(self.driver).open_more_list_modules().select_documents_module_more_list(
            DocumentModuleConstants.DOCUMENT)

        document_module.search_by_attached_to(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])

        # document_module.search_document_module()
        document_module.open_doc()

        assert document_module.get_title_doc() == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME]

    def searching_by_columns(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                                 .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                            self.config.get_value(TestDataConstants.CRM_PASSWORD),
                                            self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)
        CRMHomePage(self.driver).open_more_list_modules() \
                                .select_documents_module_more_list(DocumentModuleConstants.DOCUMENT)
        document = DocumentsPage(self.driver)
        # get document's params
        document_number = document.get_document_no_from_listview(DocumentModuleConstants.ROW_NUMBER3)
        document_type = document.get_document_type_from_listview(DocumentModuleConstants.ROW_NUMBER2)
        modified_time = document.get_modified_time_from_listview(DocumentModuleConstants.ROW_NUMBER3)

        # search by Document's list view
        # search by doc number:
        actual_doc_no = document.enter_document_no_listview(document_number) \
                                .search_document_module() \
                                .get_document_no_from_listview(DocumentModuleConstants.ROW_NUMBER)
        document.compare_data(DocumentModuleConstants.DATA_TYPE_DOC_NO, document_number, actual_doc_no)
        # search by doc type:
        document.clear_filter() \
                .select_document_type_listview(document_type) \
                .search_document_module() \
                .global_data_checker(DocumentModuleConstants.DATA_TYPE_DOC_TYPE, document_type)
        # search by modified time:
        document.clear_filter() \
                .select_doc_modified_time(modified_time) \
                .search_document_module() \
                .global_data_checker(DocumentModuleConstants.DATA_TYPE_MODIFIED_TIME, modified_time)

    def check_tabs(self):
        # crm login, open Documents module
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                                 .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                            self.config.get_value(TestDataConstants.CRM_PASSWORD),
                                            self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)
        CRMHomePage(self.driver).open_more_list_modules() \
                                .select_documents_module_more_list(DocumentModuleConstants.DOCUMENT)
        # open tabs and check data
        document = DocumentsPage(self.driver)
        document.open_tab(DocumentModuleConstants.TAB_APPROVED) \
                .global_data_checker(DocumentModuleConstants.DOC_STATUS, DocumentModuleConstants.DOC_STATUS_APPROVED) \
                .open_tab(DocumentModuleConstants.TAB_NOT_APPROVED) \
                .global_data_checker(DocumentModuleConstants.DOC_STATUS, DocumentModuleConstants.DOC_STATUS_NOT_APPROVED) \
                .open_tab(DocumentModuleConstants.TAB_PENDING) \
                .global_data_checker(DocumentModuleConstants.DOC_STATUS, DocumentModuleConstants.DOC_STATUS_PENDING)

    def check_sorting(self):
        # crm login, open Documents module
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)
        CRMHomePage(self.driver).open_more_list_modules() \
                                .select_documents_module_more_list(DocumentModuleConstants.DOCUMENT)

        # sorting and verifying data
        document = DocumentsPage(self.driver)
        document.click_document_no()
        first_row_doc_number = document.get_row_doc_no(row_number=1)
        second_row_doc_number = document.get_row_doc_no(row_number=2)
        document.check_number_is_greater(first_row_doc_number, second_row_doc_number)