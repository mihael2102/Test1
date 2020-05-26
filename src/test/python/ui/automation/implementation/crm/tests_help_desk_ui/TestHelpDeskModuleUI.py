import pytest
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HDSearchingColumnsPreconditionUI import \
    HDSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HDCreateTicketPreconditionUI import \
    HDCreateTicketPreconditionUI
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HDDeleteTicketPreconditionUI import \
    HDDeleteTicketPreconditionUI
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HDEditTicketPreconditionUI import \
    HDEditTicketPreconditionUI
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HDPencilTicketPreconditionUI import \
    HDPencilTicketPreconditionUI


@pytest.mark.run(order=26)
class TestHelpDeskModuleUI(BaseTest):

    def test_create_ticket_ui(self):
        HDCreateTicketPreconditionUI(self.driver, self.config).create_ticket_ui()

    def test_edit_ticket_ui(self):
        HDEditTicketPreconditionUI(self.driver, self.config).edit_ticket_ui()

    def test_pencil_ticket_ui(self):
        HDPencilTicketPreconditionUI(self.driver, self.config).pencil_ticket_ui()

    def test_delete_ticket_ui(self):
        HDDeleteTicketPreconditionUI(self.driver, self.config).delete_ticket_ui()

    def test_help_desk_searching_columns_ui(self):
        HDSearchingColumnsPreconditionUI(self.driver, self.config).help_desk_searching_columns_ui()
