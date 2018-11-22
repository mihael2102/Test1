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

        document_module = CRMHomePage(self.driver).open_more_list_modules().select_document_module_more_list(DocumentModuleConstants.DOCUMENT)
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

        document_module = CRMHomePage(self.driver).open_more_list_modules().select_document_module_more_list(
            DocumentModuleConstants.DOCUMENT)

        document_module.search_by_attached_to(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])

        # document_module.search_document_module()
        document_module.open_doc()

        assert document_module.get_title_doc() == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME]