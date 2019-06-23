import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.workflows.WorkflowsPrecondition import WorkflowsPrecondition


class WorkflowsModulesTest(BaseTest):

    def test_create_workflows(self):
        WorkflowsPrecondition(self.driver, self.config).create_workflows()

    def test_check_workflow_by_status(self):
        WorkflowsPrecondition(self.driver, self.config).check_workflow_by_status()

    def test_check_workflow_by_country(self):
        WorkflowsPrecondition(self.driver, self.config).check_workflow_by_country()

    def test_delete_workflow(self):
        WorkflowsPrecondition(self.driver, self.config).delete_workflow()