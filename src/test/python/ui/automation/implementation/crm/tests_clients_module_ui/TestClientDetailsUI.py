import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.ClientEditPreconditionUI import \
    ClientEditPreconditionUI
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.AddInteractionPreconditionUI import \
    AddInteractionPreconditionUI


@pytest.mark.run(order=3)
class TestClientDetailsUI(BaseTest):

    def test_edit_client_ui(self):
        ClientEditPreconditionUI(self.driver, self.config).edit_client_ui()

    def test_add_interaction_ui(self):
        AddInteractionPreconditionUI(self.driver, self.config).add_interaction_ui()
