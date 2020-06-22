import pytest
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskDetailViewPage import HelpDeskDetailViewPage
from src.test.python.ui.automation.utils.preconditions.help_desk.HelpDeskPrecondition import HelpDeskPrecondition
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage


@pytest.mark.run(order=32)
class TabHelpDeskTest(BaseTest):

    def test_check_tab_help_desk(self):
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_HELP_DESK)\
            .open_tab_list_view(HelpDeskConstants.TAB_CLOSED)\
            .global_data_checker(HelpDeskConstants.TAB_CLOSED)\
            .open_tab_list_view(HelpDeskConstants.TAB_IN_PROGRESS)\
            .global_data_checker(HelpDeskConstants.TAB_IN_PROGRESS)\
            .open_tab_list_view(HelpDeskConstants.TAB_OPEN)\
            .global_data_checker(HelpDeskConstants.TAB_OPEN)\
            .open_tab_list_view(HelpDeskConstants.TAB_OPENED_TODAY)
        HelpDeskPage(self.driver)\
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE)\
            .perform_search_ticket()
        # CRMBaseMethodsPage(self.driver) \
        #     .global_data_checker(HelpDeskConstants.FIRST_TITTLE)\
        #     .open_tab_list_view(HelpDeskConstants.TAB_WAIT_FOR_RESPONSE)\
        #     .global_data_checker(HelpDeskConstants.STATUS_AWAITING)

    def test_searching_help_desk(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url'))\
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        help_desk_module = CRMHomePage(self.driver)\
            .open_more_list_modules()\
            .open_help_desk_page()

        # Search ticket by title:
        counter = HelpDeskPage(self.driver)\
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE)\
            .perform_search_ticket()\
            .get_counter_text()

        assert counter == '1'

        # Verify the title and Get ticket no:
        HelpDeskPage(self.driver) \
            .open_ticket_number()

        ticket_number = HelpDeskDetailViewPage(self.driver)\
            .get_ticket_number_text()
        title = HelpDeskDetailViewPage(self.driver)\
            .get_title_text()

        assert title == HelpDeskConstants.FIRST_TITTLE

        # Searching by Ticket No and check only one record found:
        HelpDeskPage(self.driver)\
            .came_back_on_previous_page()

        counter = help_desk_module\
            .find_ticket_by_id(ticket_number)\
            .perform_search_ticket() \
            .get_counter_text()

        assert counter == '1'

        # Clear filter, check more than 1 record received:
        counter = help_desk_module\
            .clear_filter()\
            .get_counter_text()

        assert int(counter) > 1

        # Searching by Related To:
        help_desk_module \
            .enter_related_to(self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                             HelpDeskConstants.FIRST_RELATED_TO))\
            .perform_search_ticket()

        related_to = self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                    HelpDeskConstants.FIRST_RELATED_TO)

        CRMBaseMethodsPage(self.driver)\
            .global_data_checker(related_to)

        # Clear filter, make searching by 3 colunms:
        counter = HelpDeskPage(self.driver) \
            .clear_filter() \
            .search_ticket_by_3_columns(ticket_number,
                                        HelpDeskConstants.FIRST_TITTLE,
                                        related_to) \
            .get_counter_text()

        assert counter == '1'
