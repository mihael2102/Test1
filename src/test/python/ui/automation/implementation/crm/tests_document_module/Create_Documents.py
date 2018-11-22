from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.documents_module.DocumentPrecondition import DocumentPrecondition

class CreateDocument(BaseTest):

    def test_create_documents(self):

        DocumentPrecondition(self.driver, self.config).create_document()
        DocumentPrecondition(self.driver, self.config).verified_document()
