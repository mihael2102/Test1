import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.workflows_ui.CreateWorkflowPreconditionUI import \
    CreateWorkflowPreconditionUI


class TestWorkflowsUI(BaseTest):

    def test_create_workflow_ui(self):
        CreateWorkflowPreconditionUI(self.driver, self.config).create_workflow_ui()
