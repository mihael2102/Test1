import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.Clients_Searching_Columns_Precondition_UI \
    import ClientsSearchingColumnsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.Clients_Mass_Assign_Precondition_UI import \
    ClientsMassAssignPreconditionUI


@pytest.mark.run(order=3)
class TestClientsModuleUI(BaseTest):

    def test_clients_searching_columns_ui(self):
        ClientsSearchingColumnsPreconditionUI(self.driver, self.config).clients_searching_columns_ui()

    def test_mass_assign_clients_ui(self):
        ClientsMassAssignPreconditionUI(self.driver, self.config).mass_assign_clients_ui()
