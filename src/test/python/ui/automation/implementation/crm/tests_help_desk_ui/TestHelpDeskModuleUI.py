import pytest
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HelpDeskSearchingColumnsPreconditionUI import \
    HelpDeskSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HelpDeskCreateTicketPreconditionUI import \
    HelpDeskCreateTicketPreconditionUI
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HelpDeskDeleteTicketPreconditionUI import \
    HelpDeskDeleteTicketPreconditionUI
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HelpDeskEditTicketPreconditionUI import \
    HelpDeskEditTicketPreconditionUI


@pytest.mark.run(order=26)
class TestHelpDeskModuleUI(BaseTest):

    def test_create_ticket_ui(self):
        HelpDeskCreateTicketPreconditionUI(self.driver, self.config).create_ticket_ui()

    def test_edit_ticket_ui(self):
        HelpDeskEditTicketPreconditionUI(self.driver, self.config).edit_ticket_ui()

    def test_edit_pencil_ticket_ui(self):
        HelpDeskEditTicketPreconditionUI(self.driver, self.config).edit_ticket_ui()

    def test_delete_ticket_ui(self):
        HelpDeskDeleteTicketPreconditionUI(self.driver, self.config).delete_ticket_ui()

    def test_help_desk_searching_columns_ui(self):
        HelpDeskSearchingColumnsPreconditionUI(self.driver, self.config).help_desk_searching_columns_ui()
