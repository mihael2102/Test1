import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.ClientsSearchingColumnsPreconditionUI \
    import ClientsSearchingColumnsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.ClientsMassAssignPreconditionUI import \
    ClientsMassAssignPreconditionUI
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.ClientsMassEditPreconditionUI import \
    ClientsMassEditPreconditionUI
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.ClientEditPreconditionUI import \
    ClientEditPreconditionUI


@pytest.mark.run(order=3)
class TestClientsModuleUI(BaseTest):

    def test_clients_searching_columns_ui(self):
        ClientsSearchingColumnsPreconditionUI(self.driver, self.config).clients_searching_columns_ui()

    def test_mass_assign_clients_ui(self):
        ClientsMassAssignPreconditionUI(self.driver, self.config).mass_assign_clients_ui()

    def test_mass_edit_clients_ui(self):
        ClientsMassEditPreconditionUI(self.driver, self.config).mass_edit_clients_ui()

    def test_edit_client_ui(self):
        ClientEditPreconditionUI(self.driver, self.config).edit_client_ui()
