from src.main.python.ui.crm.model.constants.FilterConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.help_desk.HelpDeskPrecondition import HelpDeskPrecondition


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

        assert all_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_TABS,
                                                              HelpDeskConstants.FIRST_TAB)
        assert closed_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_TABS,
                                                                 HelpDeskConstants.SECOND_TAB)
        assert in_progress_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_TABS,
                                                                      HelpDeskConstants.THIRD_TAB)
        assert open_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_TABS,
                                                               HelpDeskConstants.FOURTH_TAB)
        assert opened_today_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_TABS,
                                                                       HelpDeskConstants.FIFTH_TAB)
        assert wait_for_response_tab_name == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_TABS,
                                                                            HelpDeskConstants.SIXTH_TAB)

    def test_searching_help_desk(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        help_desk_module = CRMHomePage().open_help_desk_page()

        HelpDeskPrecondition().create_first_ticket()

        detail_view_page_service_desk_module = HelpDeskPage().select_filter(HelpDeskConstants.FILTER_INFO) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        tittle = detail_view_page_service_desk_module.get_title_text()
        category = detail_view_page_service_desk_module.get_category_status_text()
        ticket_status = detail_view_page_service_desk_module.get_ticket_status_text()
        account_name = detail_view_page_service_desk_module.get_account_name()
        description = detail_view_page_service_desk_module.get_description_text()
        notes = detail_view_page_service_desk_module.get_notes_text()
        priority = detail_view_page_service_desk_module.get_priority_text()

        detail_view_page_service_desk_module.came_back_on_previous_page()

        help_desk_module.find_ticket_by_columns(

            HelpDeskConstants.FIRST_TITTLE,
            Config.data.get_data_help_desk(tittle),
            Config.data.get_data_help_desk(category),
            Config.data.get_data_help_desk(ticket_status),
            Config.data.get_data_help_desk(account_name),
            Config.data.get_data_help_desk(description),
            Config.data.get_data_help_desk(notes),
            Config.data.get_data_help_desk(priority))

        help_desk_module.open_ticket_number()
