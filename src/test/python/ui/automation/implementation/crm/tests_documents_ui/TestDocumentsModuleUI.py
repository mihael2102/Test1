import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.documents_ui.DocumentsSearchingColumnsPreconditionUI \
    import DocumentsSearchingColumnsPreconditionUI


@pytest.mark.run(order=3)
class TestDocumentsModuleUI(BaseTest):

    def test_documents_searching_columns_ui(self):
        DocumentsSearchingColumnsPreconditionUI(self.driver, self.config).documents_searching_columns_ui()
