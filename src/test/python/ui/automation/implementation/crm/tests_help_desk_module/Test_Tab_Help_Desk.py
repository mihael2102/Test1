from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *


class TabHelpDeskTest(BaseTest):

    def test_check_tab_help_desk(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        help_desk_module = CRMHomePage().open_help_desk_page()

        all_tab_name = help_desk_module.get_all_tab_text()
        closed_tab_name = help_desk_module.get_closed_tab_text()
        in_progress_tab_name = help_desk_module.get_in_progress_tab_text()
        open_tab_name = help_desk_module.get_open_tab_text()
        opened_today_tab_name = help_desk_module.get_open_today_tab_text()
        wait_for_response_tab_name = help_desk_module.get_wait_for_response_tab_text()

        assert all_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.FIRST_TAB)
        assert closed_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.SECOND_TAB)
        assert in_progress_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.THIRD_TAB)
        assert open_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.FOURTH_TAB)
        assert opened_today_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.FIFTH_TAB)
        assert wait_for_response_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.SIXTH_TAB)
