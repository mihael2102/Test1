from datetime import *

from dateutil.relativedelta import relativedelta


class CRMDocumentConstants(object):
    FOURTH_TAB = "fourth_tab"
    FIRST_TAB = "first_tab"
    SECOND_TAB = "second_tab"
    THIRD_TAB = "third_tab"
    DOCUMENT = "Documents"
    CRM_ADD_DOCUMENT = "AddDocument"
    FIRST_DOCUMENT_TYPE = "first_document_type"
    FIRST_STATUS = "first_status"
    EXPIRE_DATE_DOCUMENT = datetime.now() + relativedelta(days=2)
    COMMENTS = "document"
    MESSAGE_SUCCESSFUL = "Upload Document successfull"
    MESSAGE_DELETE_DOCUMENT = "Document was deleted successfully"
