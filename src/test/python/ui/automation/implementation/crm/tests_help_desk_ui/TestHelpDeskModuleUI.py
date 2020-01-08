import pytest
from src.test.python.ui.automation.utils.preconditions.help_desk_ui.HelpDeskSearchingColumnsPreconditionUI import \
    HelpDeskSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.Leads_Mass_Assign_Precondition_UI import \
    LeadsMassAssignPreconditionUI
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.Leads_Mass_Edit_Precondition_UI import \
    LeadsMassEditPreconditionUI


@pytest.mark.run(order=26)
class TestHelpDeskModuleUI(BaseTest):

    def test_help_desk_searching_columns_ui(self):
        HelpDeskSearchingColumnsPreconditionUI(self.driver, self.config).help_desk_searching_columns_ui()
