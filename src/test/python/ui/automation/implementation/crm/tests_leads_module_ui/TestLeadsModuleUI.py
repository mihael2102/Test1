import pytest
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.LeadsSearchingColumnsPreconditionUI import \
    LeadsSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.LeadsMassAssignPreconditionUI import \
    LeadsMassAssignPreconditionUI
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.LeadsMassEditPreconditionUI import \
    LeadsMassEditPreconditionUI
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.ConvertLeadPreconditionUI import \
    ConvertLeadPreconditionUI
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.EditLeadPreconditionUI import \
    EditLeadPreconditionUI
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.EditPencilLeadPreconditionUI import \
    EditPencilLeadPreconditionUI


@pytest.mark.run(order=26)
class TestLeadsModuleUI(BaseTest):

    def test_leads_searching_columns_ui(self):
        LeadsSearchingColumnsPreconditionUI(self.driver, self.config).leads_searching_columns_ui()

    def test_mass_assign_leads_ui(self):
        LeadsMassAssignPreconditionUI(self.driver, self.config).mass_assign_leads_ui()

    def test_mass_edit_leads_ui(self):
        LeadsMassEditPreconditionUI(self.driver, self.config).mass_edit_leads_ui()

    def test_edit_lead_ui(self):
        EditLeadPreconditionUI(self.driver, self.config).edit_lead_ui()

    def test_edit_pencil_lead_ui(self):
        EditPencilLeadPreconditionUI(self.driver, self.config).edit_pencil_lead_ui()

    def test_convert_lead_ui(self):
        ConvertLeadPreconditionUI(self.driver, self.config).convert_lead_ui()
