import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.autoassign_ui.AutoAssignLeadRulePreconditionUI import \
    AutoAssignLeadRulePreconditionUI
from src.test.python.ui.automation.utils.preconditions.autoassign_ui.AutoAssignClientRulePreconditionUI import \
    AutoAssignClientRulePreconditionUI
from src.test.python.ui.automation.utils.preconditions.autoassign_ui.AutoAssignDeletePreconditionUI import \
    AutoAssignDeletePreconditionUI


@pytest.mark.run(order=34)
class TestAutoAssignModuleUI(BaseTest):

    def test_add_auto_assign_rule_lead_ui(self):
        AutoAssignLeadRulePreconditionUI(self.driver, self.config).add_rule_lead()

    def test_add_auto_assign_rule_client_ui(self):
        AutoAssignClientRulePreconditionUI(self.driver, self.config).add_rule_client()

    def test_delete_auto_assign_rule_ui(self):
        AutoAssignDeletePreconditionUI(self.driver, self.config).delete_rule()
