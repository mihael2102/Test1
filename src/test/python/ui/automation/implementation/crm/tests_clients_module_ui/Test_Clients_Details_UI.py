import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.clients_module_ui.Clients_Searching_Columns_Precondition_UI \
    import ClientsSearchingColumnsPreconditionUI


@pytest.mark.run(order=3)
class TestClientsDetailsUI(BaseTest):

    def test_make_deposit_crm_new_ui(self):
        ClientsSearchingColumnsPreconditionUI(self.driver, self.config).clients_searching_columns_ui()
