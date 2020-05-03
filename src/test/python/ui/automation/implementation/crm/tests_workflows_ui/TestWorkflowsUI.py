import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.workflows_ui.CreateWorkflowPreconditionUI import \
    CreateWorkflowPreconditionUI
from src.test.python.ui.automation.utils.preconditions.workflows_ui.CheckWorkflowStatusPreconditionUI import \
    CheckWorkflowStatusPreconditionUI
from src.test.python.ui.automation.utils.preconditions.workflows_ui.CheckWorkflowCountryPreconditionUI import \
    CheckWorkflowCountryPreconditionUI
from src.test.python.ui.automation.utils.preconditions.workflows_ui.DeleteWorkflowPreconditionUI import \
    DeleteWorkflowPreconditionUI


class TestWorkflowsUI(BaseTest):

    def test_create_workflow_ui(self):
        CreateWorkflowPreconditionUI(self.driver, self.config).create_workflow_ui()

    def test_check_workflow_by_status_ui(self):
        CheckWorkflowStatusPreconditionUI(self.driver, self.config).check_workflow_by_status_ui()

    def test_check_workflow_by_country_ui(self):
        CheckWorkflowCountryPreconditionUI(self.driver, self.config).check_workflow_by_country_ui()

    def test_delete_workflow_ui(self):
        DeleteWorkflowPreconditionUI(self.driver, self.config).delete_workflow_ui()
