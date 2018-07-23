from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.test.python.utils.TestDataConstants import TestDataConstants


class MassEditPrecondition(object):
    def __init__(self) -> None:
        super().__init__()

    def create_first_event(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        task_module.open_add_event_module().create_event(TaskModuleConstants.FIRST_EVENT_STATUS,
                                                         TaskModuleConstants.FIRST_EVENT_TYPE,
                                                         TaskModuleConstants.FIRST_DURATION,
                                                         CRMConstants.SECOND_DATE.strftime(
                                                             CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.SECOND_DATE.strftime(
                                                             CRMConstants.FIRST_FORMAT_TIME),
                                                         TaskModuleConstants.FIRST_ASSIGN_TO,
                                                         TaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                         TaskModuleConstants.FIFTH_SUBJECT,
                                                         TaskModuleConstants.FIRST_PRIORITY,
                                                         TaskModuleConstants.DESCRIPTION_ADD_EVENT)
        return MassEditPrecondition()

    def create_second_event(self):
        task_module = TasksPage()
        task_module.open_add_event_module().create_event(TaskModuleConstants.SECOND_EVENT_STATUS,
                                                         TaskModuleConstants.SECOND_EVENT_TYPE,
                                                         TaskModuleConstants.SECOND_DURATION,
                                                         CRMConstants.THIRD_DATE.strftime(
                                                             CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.THIRD_DATE.strftime(
                                                             CRMConstants.FIRST_FORMAT_TIME),
                                                         TaskModuleConstants.SECOND_ASSIGN_TO,
                                                         TaskModuleConstants.SECOND_ACCOUNT_NAME,
                                                         TaskModuleConstants.FIFTH_SUBJECT,
                                                         TaskModuleConstants.SECOND_PRIORITY,
                                                         TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        return MassEditPrecondition()

    def create_third_event(self):
        task_module = TasksPage()
        task_module.open_add_event_module().create_event(TaskModuleConstants.THIRD_EVENT_STATUS,
                                                         TaskModuleConstants.THIRD_EVENT_TYPE,
                                                         TaskModuleConstants.THIRD_DURATION,
                                                         CRMConstants.FOURTH_DATE.strftime(
                                                             CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.FOURTH_DATE.strftime(
                                                             CRMConstants.FIRST_FORMAT_TIME),
                                                         TaskModuleConstants.THIRD_ASSIGN_TO,
                                                         TaskModuleConstants.THIRD_ACCOUNT_NAME,
                                                         TaskModuleConstants.FIFTH_SUBJECT,
                                                         TaskModuleConstants.THIRD_PRIORITY,
                                                         TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        return MassEditPrecondition()
