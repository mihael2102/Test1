from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage


class DocumentDetailViewPage(BrandBasePage):
    def __init__(self):
        super().__init__()

    def get_document_status(self):
        document_status_crm = super().wait_load_element("//td[contains(text(),'Status')]//following-sibling::td[1]")
        return document_status_crm.text
