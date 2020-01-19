import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.Clients_Searching_Columns_Precondition_UI \
    import ClientsSearchingColumnsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.Clients_Mass_Assign_Precondition_UI import \
    ClientsMassAssignPreconditionUI
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.Clients_Mass_Edit_Precondition_UI import \
    ClientsMassEditPreconditionUI


@pytest.mark.run(order=3)
class TestClientsModuleUI(BaseTest):

    def test_clients_searching_columns_ui(self):
        ClientsSearchingColumnsPreconditionUI(self.driver, self.config).clients_searching_columns_ui()

    def test_mass_assign_clients_ui(self):
        ClientsMassAssignPreconditionUI(self.driver, self.config).mass_assign_clients_ui()

    def test_mass_edit_clients_ui(self):
        ClientsMassEditPreconditionUI(self.driver, self.config).mass_edit_clients_ui()
