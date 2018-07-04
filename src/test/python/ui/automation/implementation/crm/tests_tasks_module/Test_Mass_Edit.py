from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.modules.tasks_module.TaskModule import TaskModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.task_module.MassEditPrecondition import MassEditPrecondition
from src.test.python.utils.TestDataConstants import TestDataConstants


class MassEditTaskModule(BaseTest):

    def test_mass_edit_task(self):
        # MassEditPrecondition().create_first_event().create_second_event().create_third_event()

        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD))

        CRMHomePage().open_task_module()

        task_module = TaskModule()
        task_module.open_show_all_tab().find_event_by_subject(
            TaskModuleConstants.FIFTH_SUBJECT).select_three_records_task_module() \
            .open_mass_edit_task().perform_mass_edit(TaskModuleConstants.SECOND_EVENT_STATUS,
                                                     TaskModuleConstants.SECOND_EVENT_TYPE,
                                                     TaskModuleConstants.SECOND_DURATION,
                                                     CRMConstants.THIRD_DATE.strftime(
                                                         CRMConstants.SECOND_FORMAT_DATE),
                                                     CRMConstants.THIRD_DATE.strftime(
                                                         CRMConstants.FIRST_FORMAT_TIME),
                                                     TaskModuleConstants.SECOND_ASSIGN_TO,
                                                     TaskModuleConstants.SECOND_PRIORITY,
                                                     TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == TaskModuleConstants.MESSAGE_TASK_WERE_UPDATED
        task_module.perform_screen_shot()
