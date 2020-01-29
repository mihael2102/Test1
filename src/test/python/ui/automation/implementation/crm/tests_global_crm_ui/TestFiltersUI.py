import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.filter_ui.FilterClientsPreconditionUI import \
    FilterClientsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.filter_ui.FilterLeadsPreconditionUI import \
    FilterLeadsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.filter_ui.FilterDocumentsPreconditionUI import \
    FilterDocumentsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.filter_ui.FilterHelpDeskPreconditionUI import \
    FilterHelpDeskPreconditionUI


@pytest.mark.run(order=3)
class TestFiltersUI(BaseTest):

    def test_filter_clients_ui(self):
        FilterClientsPreconditionUI(self.driver, self.config).create_filter_clients_ui()

    def test_filter_leads_ui(self):
        FilterLeadsPreconditionUI(self.driver, self.config).create_filter_leads_ui()

    def test_filter_documents_ui(self):
        FilterDocumentsPreconditionUI(self.driver, self.config).create_filter_documents_ui()

    def test_filter_help_desk_ui(self):
        FilterHelpDeskPreconditionUI(self.driver, self.config).create_filter_help_desk_ui()
