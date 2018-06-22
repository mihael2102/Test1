from datetime import *

from dateutil.relativedelta import relativedelta


class CRMDocumentConstants(object):
    CRM_ADD_DOCUMENT = "AddDocument"
    FIRST_DOCUMENT_TYPE = "first_document_type"
    FIRST_STATUS = "first_status"
    EXPIRE_DATE_DOCUMENT = datetime.now() + relativedelta(days=2)
    COMMENTS = "document"
