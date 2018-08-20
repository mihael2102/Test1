import pytest

from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.help_desk.HelpDeskPrecondition import HelpDeskPrecondition


@pytest.mark.run(order=32)
class TabHelpDeskTest(BaseTest):

    def test_check_tab_help_desk(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

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
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        help_desk_module = CRMHomePage().open_help_desk_page()

        HelpDeskPrecondition().create_first_ticket()

        detail_view_page_service_desk_module = HelpDeskPage().select_filter(
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        ticket_number = detail_view_page_service_desk_module.get_ticket_number_text()
        ca_id = detail_view_page_service_desk_module.get_ca_id_text()
        brand = detail_view_page_service_desk_module.get_brand_text()

        detail_view_page_service_desk_module.came_back_on_previous_page()

        help_desk_module.find_ticket_by_columns(ticket_number, ca_id, brand,
                                                HelpDeskConstants.FIRST_TITTLE,
                                                Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                               HelpDeskConstants.FIRST_RELATED_TO),
                                                Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                               HelpDeskConstants.FIRST_ASSIGNED_TO),
                                                Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                               HelpDeskConstants.FIRST_STATUS),
                                                Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                               HelpDeskConstants.FIRST_PRIORITY),
                                                Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                               HelpDeskConstants.FIRST_CATEGORY),
                                                Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                                               HelpDeskConstants.FIRST_DESCRIPTION))

        help_desk_module.open_ticket_number()
