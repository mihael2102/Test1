import pytest
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HelpDeskSearchingColumnsPreconditionUI import \
    HelpDeskSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HelpDeskCreateTicketPreconditionUI import \
    HelpDeskCreateTicketPreconditionUI


@pytest.mark.run(order=26)
class TestHelpDeskModuleUI(BaseTest):

    def test_create_ticket_ui(self):
        HelpDeskCreateTicketPreconditionUI(self.driver, self.config).create_ticket_ui()

    def test_help_desk_searching_columns_ui(self):
        HelpDeskSearchingColumnsPreconditionUI(self.driver, self.config).help_desk_searching_columns_ui()
