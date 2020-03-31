import pytest
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksSearchingColumnsPreconditionUI import \
    TasksSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksAddDeleteEventPreconditionUI import \
    TasksAddDeleteEventPreconditionUI
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksMassEditPreconditionUI import \
    TasksMassEditPreconditionUI
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksEmailPreconditionUI import \
    TasksEmailPreconditionUI


@pytest.mark.run(order=26)
class TestTasksModuleUI(BaseTest):

    def test_tasks_searching_columns_ui(self):
        TasksSearchingColumnsPreconditionUI(self.driver, self.config).tasks_searching_columns_ui()

    def test_add_delete_event_ui(self):
        TasksAddDeleteEventPreconditionUI(self.driver, self.config).add_delete_event_ui()

    def test_tasks_mass_edit(self):
        TasksMassEditPreconditionUI(self.driver, self.config).mass_edit_tasks_ui()

    def test_tasks_email_ui(self):
        TasksEmailPreconditionUI(self.driver, self.config).send_email_tasks_ui()
