from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class AddEventTaskModule(BaseTest):

    def test_add_event(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        task_module.open_add_event_module().create_event(TaskModuleConstants.FIRST_EVENT_STATUS,
                                                         TaskModuleConstants.FIRST_EVENT_TYPE,
                                                         TaskModuleConstants.FIRST_DURATION,
                                                         CRMConstants.DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                         TaskModuleConstants.FIRST_ASSIGN_TO,
                                                         TaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                         TaskModuleConstants.FOURTH_SUBJECT,
                                                         TaskModuleConstants.FIRST_PRIORITY,
                                                         TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == TaskModuleConstants.MESSAGE_CREATE_EVENT

    def test_edit_event(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        task_module.open_add_event_module().create_event(TaskModuleConstants.FIRST_EVENT_STATUS,
                                                         TaskModuleConstants.FIRST_EVENT_TYPE,
                                                         TaskModuleConstants.FIRST_DURATION,
                                                         CRMConstants.DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                         TaskModuleConstants.FIRST_ASSIGN_TO,
                                                         TaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                         TaskModuleConstants.FOURTH_SUBJECT,
                                                         TaskModuleConstants.FIRST_PRIORITY,
                                                         TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == TaskModuleConstants.MESSAGE_CREATE_EVENT

        task_module.open_show_all_tab() \
            .click_pencil_button().edit_event(TaskModuleConstants.SECOND_EVENT_STATUS,
                                              TaskModuleConstants.SECOND_EVENT_TYPE,
                                              TaskModuleConstants.SECOND_DURATION,
                                              CRMConstants.THIRD_DATE.strftime(
                                                  CRMConstants.SECOND_FORMAT_DATE),
                                              CRMConstants.THIRD_DATE.strftime(
                                                  CRMConstants.FIRST_FORMAT_TIME),
                                              TaskModuleConstants.SECOND_ASSIGN_TO,
                                              TaskModuleConstants.SECOND_SUBJECT,
                                              TaskModuleConstants.SECOND_PRIORITY,
                                              TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == TaskModuleConstants.MESSAGE_TASK_WAS_UPDATED
