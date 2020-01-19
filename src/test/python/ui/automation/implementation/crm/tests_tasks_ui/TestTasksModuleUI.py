import pytest
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksSearchingColumnsPreconditionUI import \
    TasksSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksAddDeleteEventPreconditionUI import \
    TasksAddDeleteEventPreconditionUI
from src.test.python.ui.automation.utils.preconditions.leads_module_ui.Leads_Mass_Edit_Precondition_UI import \
    LeadsMassEditPreconditionUI


@pytest.mark.run(order=26)
class TestTasksModuleUI(BaseTest):

    def test_tasks_searching_columns_ui(self):
        TasksSearchingColumnsPreconditionUI(self.driver, self.config).tasks_searching_columns_ui()

    def test_add_delete_event_ui(self):
        TasksAddDeleteEventPreconditionUI(self.driver, self.config).add_delete_event_ui()
