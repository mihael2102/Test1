import pytest
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.Leads_Searching_Columns_Precondition_UI import \
    LeadsSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.Leads_Mass_Assign_Precondition_UI import \
    LeadsMassAssignPreconditionUI


@pytest.mark.run(order=26)
class TestLeadsModuleUI(BaseTest):

    def test_leads_searching_columns_ui(self):
        LeadsSearchingColumnsPreconditionUI(self.driver, self.config).leads_searching_columns_ui()

    def test_mass_assign_leads_ui(self):
        LeadsMassAssignPreconditionUI(self.driver, self.config).mass_assign_leads_ui()
