import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.main.python.ui.crm.model.main_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants

@pytest.mark.run(order=4)
class AddEventTaskModule(BaseTest):

    def test_add_event(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        task_module.open_add_event_module().create_event(CRMTaskModuleConstants.FIRST_EVENT_STATUS,
                                                         CRMTaskModuleConstants.FIRST_EVENT_TYPE,
                                                         CRMTaskModuleConstants.FIRST_DURATION,
                                                         CRMConstants.DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                         CRMTaskModuleConstants.FIRST_ASSIGN_TO,
                                                         CRMTaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                         CRMTaskModuleConstants.FIRST_SUBJECT,
                                                         CRMTaskModuleConstants.FIRST_PRIORITY,
                                                         CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == CRMTaskModuleConstants.MESSAGE_CREATE_EVENT

    def test_edit_event(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        task_module.open_add_event_module().create_event(CRMTaskModuleConstants.FIRST_EVENT_STATUS,
                                                         CRMTaskModuleConstants.FIRST_EVENT_TYPE,
                                                         CRMTaskModuleConstants.FIRST_DURATION,
                                                         CRMConstants.DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                         CRMTaskModuleConstants.FIRST_ASSIGN_TO,
                                                         CRMTaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                         CRMTaskModuleConstants.FIRST_SUBJECT,
                                                         CRMTaskModuleConstants.FIRST_PRIORITY,
                                                         CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == CRMTaskModuleConstants.MESSAGE_CREATE_EVENT

        task_module.open_this_week_tab() \
            .click_pencil_button().edit_event(CRMTaskModuleConstants.SECOND_EVENT_STATUS,
                                              CRMTaskModuleConstants.SECOND_EVENT_TYPE,
                                              CRMTaskModuleConstants.SECOND_DURATION,
                                              CRMConstants.THIRD_DATE.strftime(
                                                  CRMConstants.SECOND_FORMAT_DATE),
                                              CRMConstants.THIRD_DATE.strftime(
                                                  CRMConstants.FIRST_FORMAT_TIME),
                                              CRMTaskModuleConstants.SECOND_ASSIGN_TO,
                                              CRMTaskModuleConstants.SECOND_SUBJECT,
                                              CRMTaskModuleConstants.SECOND_PRIORITY,
                                              CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == CRMTaskModuleConstants.MESSAGE_TASK_WAS_UPDATED
