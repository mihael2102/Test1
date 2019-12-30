import pytest
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.Leads_Searching_Columns_Precondition_UI import \
    LeadsSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *


@pytest.mark.run(order=26)
class TestLeadsModuleUI(BaseTest):

    def test_leads_searching_columns_ui(self):
        LeadsSearchingColumnsPreconditionUI(self.driver, self.config).leads_searching_columns_ui()
