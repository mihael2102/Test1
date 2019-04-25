from datetime import *

from dateutil.relativedelta import relativedelta


class DocumentModuleConstants(object):
    DOCUMENTS_MODULE_TABS = "DocumentModuleTabs"
    DOCUMENTS_MODULE_COLUMNS = "DocumentsModuleColumns"
    FILTER_NAME = "filter_name"
    DOCUMENTS_INFO_MODULE = "DocumentsModuleInformation"
    FOURTH_TAB = "fourth_tab"
    FIRST_TAB = "first_tab"
    SECOND_TAB = "second_tab"
    THIRD_TAB = "third_tab"
    DOCUMENT = "Documents"
    FIRST_DOCUMENT_TYPE = "first_document_type"
    FIRST_STATUS = "first_status"
    EXPIRE_DATE_DOCUMENT = datetime.now() + relativedelta(days=2)
    COMMENTS = "first_comments"
    MESSAGE_SUCCESSFUL = "Upload Document successfull"
    MESSAGE_DELETE_DOCUMENT = "Document was deleted successfully"
    NAME_DOCUMENT = "Bear.jpg"
    FIRST_COLUMN = "first_column"
    SECOND_COLUMN = "second_column"
    SECOND_COLUMN_DOC_ST = "second_column_doc_status"
    THIRD_COLUMN = "third_column"
    FOURTH_COLUMN = "fourth_column"
    FOURTH_COLUMN_TEXT = "Assigned To"
    ROW_NUMBER = "1"
    ROW_NUMBER2 = "2"
    ROW_NUMBER3 = "3"
    DOCUMENT_TYPE = "Other"
    DATA_TYPE_DOC_NO = "Document No"
    DATA_TYPE_DOC_TYPE = "Document Type"
    DATA_TYPE_MODIFIED_TIME = "Modified Time"
