import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.side_bar.SidebarModules import SidebarModules
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=4)
class AddInteraction(BaseTest):

    def test_add_interaction(self):
        crm_client_profile = CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.E_MAIL))

        SidebarModules().open_create_event_module(CRMConstants.ADD_INTERACTION) \
            .create_event(TaskModuleConstants.FIRST_EVENT_STATUS, TaskModuleConstants.FIRST_EVENT_TYPE,
                          TaskModuleConstants.FIRST_DURATION,
                          CRMConstants.DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                          CRMConstants.DATE.strftime(CRMConstants.FORMAT_DATE),
                          TaskModuleConstants.FIRST_ASSIGN_TO, TaskModuleConstants.FIRST_PRIORITY,
                          CRMConstants.DESCRIPTION_ADD_INTERACTION)

        confirmation_message = crm_client_profile.get_confirm_message()
        assert confirmation_message == CRMConstants.INTERACTION_SUCCESSFULLY
        crm_client_profile.click_ok()
