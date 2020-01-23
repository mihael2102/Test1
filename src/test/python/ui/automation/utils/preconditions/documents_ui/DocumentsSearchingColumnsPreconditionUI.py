from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.documents_ui.DocumentsModuleConstantsUI import DocumentsModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI


class DocumentsSearchingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def documents_searching_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
            self.config.get_value('url'),
            self.config.get_value(TestDataConstants.USER_NAME),
            self.config.get_value(TestDataConstants.CRM_PASSWORD),
            self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Documents module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_DOCUMENTS) \
            .open_tab_list_view_ui(DocumentsModuleConstantsUI.TAB_ALL)

        """ Get data from the first row of list view """
        document_no = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=DocumentsModuleConstantsUI.COLUMN_DOCUMENT_NO,
                                        row=DocumentsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        status = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=DocumentsModuleConstantsUI.COLUMN_STATUS,
                                        row=DocumentsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        document_type = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=DocumentsModuleConstantsUI.COLUMN_DOCUMENT_TYPE,
                                        row=DocumentsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        attached_to = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=DocumentsModuleConstantsUI.COLUMN_ATTACHED_TO,
                                        row=DocumentsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        assigned_to = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=DocumentsModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                        row=DocumentsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """
        search = GlobalTablePageUI(self.driver)
        if status:
            search\
                .select_data_column_field(column=DocumentsModuleConstantsUI.COLUMN_STATUS,
                                          data=status)
        if document_no:
            search\
                .set_data_column_field(column=DocumentsModuleConstantsUI.COLUMN_DOCUMENT_NO,
                                       data=document_no)
        if document_type:
            search\
                .select_data_column_field(column=DocumentsModuleConstantsUI.COLUMN_DOCUMENT_TYPE,
                                          data=document_type)
        if assigned_to:
            search\
                .select_data_column_field(column=DocumentsModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                          data=assigned_to)
        if attached_to:
            search\
                .set_data_column_field(column=DocumentsModuleConstantsUI.COLUMN_ATTACHED_TO,
                                       data=attached_to)

        """ Verify correct data found """
        result = GlobalTablePageUI(self.driver)
        if document_no:
            result\
                .global_data_checker_new_ui(document_no)
        if document_type:
            result\
                .global_data_checker_new_ui(document_type)
        if status:
            result\
                .global_data_checker_new_ui(status)
        if assigned_to:
            result\
                .global_data_checker_new_ui(assigned_to)
        if attached_to:
            result\
                .global_data_checker_new_ui(attached_to)

        """ Verify, only 1 record was found """
        number_records = CRMBaseMethodsPage(self.driver)\
            .get_number_records()
        assert number_records == 1
