from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging


class DocumentDetailViewPage(BrandBasePage):
    def __init__(self):
        super().__init__()

    def get_document_status(self):
        document_status_crm = super().wait_load_element_present(
            "//td[contains(text(),'Status')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "The document status is: "+document_status_crm.text)
        return document_status_crm.text

    def get_document_type(self):
        document_type_crm = super().wait_load_element_present(
            "//td[contains(text(),'Document Type')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "The document type is: " + document_type_crm.text)
        return document_type_crm.text

    def get_document_comment(self):
        document_comment = super().wait_load_element_present(
            "//td[contains(text(),'Comments')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "The document comment is: " + document_comment.text)
        return document_comment.text
