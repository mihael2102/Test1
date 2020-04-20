import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.workflows_ui.CreateWorkflowPreconditionUI import \
    CreateWorkflowPreconditionUI
from src.test.python.ui.automation.utils.preconditions.workflows_ui.CheckWorkflowStatusPreconditionUI import \
    CheckWorkflowStatusPreconditionUI


class TestWorkflowsUI(BaseTest):

    def test_create_workflow_ui(self):
        CreateWorkflowPreconditionUI(self.driver, self.config).create_workflow_ui()

    def test_check_workflow_by_status_ui(self):
        CheckWorkflowStatusPreconditionUI(self.driver, self.config).check_workflow_by_status_ui()
