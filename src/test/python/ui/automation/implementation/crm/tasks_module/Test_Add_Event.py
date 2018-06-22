from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.main_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class AddEventTaskModule(BaseTest):

    def test_add_event(self):
        crm_client_profile = CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module().open_event_module()

        task_module.create_event(CRMConstants.EVENT_STATUS, CRMConstants.EVENT_TYPE, CRMConstants.DURATION,
                                 CRMConstants.DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                 CRMConstants.DATE.strftime(CRMConstants.FORMAT_TIME),
                                 CRMConstants.ASSIGN_TO, CRMConstants.FIRST_ACCOUNT_NAME, CRMConstants.SUBJECT,
                                 CRMConstants.PRIORITY, CRMConstants.DESCRIPTION_ADD_EVENT)

        confirmation_message = crm_client_profile.get_message_task_was_updated()
        assert confirmation_message == CRMConstants.MESSAGE_CREATE_EVENT
