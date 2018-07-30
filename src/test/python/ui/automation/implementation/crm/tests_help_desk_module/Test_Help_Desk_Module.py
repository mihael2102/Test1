from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.filter.FilterPrecondition import FilterPrecondition
from src.test.python.ui.automation.utils.preconditions.help_desk.HelpDeskPrecondition import HelpDeskPrecondition


class HelpDeskTest(BaseTest):

    def test_create_ticket(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()

        detail_view_page_service_desk_module = HelpDeskPage().find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        tittle = detail_view_page_service_desk_module.get_title_text()
        category = detail_view_page_service_desk_module.get_category_status_text()
        ticket_status = detail_view_page_service_desk_module.get_ticket_status_text()
        account_name = detail_view_page_service_desk_module.get_account_name()
        description = detail_view_page_service_desk_module.get_description_text()
        notes = detail_view_page_service_desk_module.get_notes_text()
        priority = detail_view_page_service_desk_module.get_priority_text()

        assert tittle == HelpDeskConstants.FIRST_TITTLE
        assert category == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                          HelpDeskConstants.FIRST_CATEGORY)
        assert ticket_status == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                               HelpDeskConstants.FIRST_STATUS)

        assert account_name == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                              HelpDeskConstants.SECOND_RELATED_TO)

        assert description == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                             HelpDeskConstants.FIRST_DESCRIPTION)

        assert notes == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                       HelpDeskConstants.FIRST_NOTES)

        assert priority == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                          HelpDeskConstants.FIRST_PRIORITY)

    def test_edit_ticket(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        FilterPrecondition().create_filter_service_desk()

        HelpDeskPrecondition().create_first_ticket()

        HelpDeskPage().find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .click_edit_ticket_pencil().perform_edit_ticket(
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
                                           HelpDeskConstants.FIRST_TICKET_SOURCE),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                           HelpDeskConstants.FIRST_DESCRIPTION),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                           HelpDeskConstants.FIRST_NOTES))

        detail_view_page_service_desk_module = HelpDeskPage().find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        tittle = detail_view_page_service_desk_module.get_title_text()
        category = detail_view_page_service_desk_module.get_category_status_text()
        ticket_status = detail_view_page_service_desk_module.get_ticket_status_text()
        account_name = detail_view_page_service_desk_module.get_account_name()
        description = detail_view_page_service_desk_module.get_description_text()
        notes = detail_view_page_service_desk_module.get_notes_text()
        priority = detail_view_page_service_desk_module.get_priority_text()

        assert tittle == HelpDeskConstants.FIRST_TITTLE
        assert category == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                          HelpDeskConstants.FIRST_CATEGORY)
        assert ticket_status == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                               HelpDeskConstants.FIRST_STATUS)

        assert account_name == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                              HelpDeskConstants.SECOND_RELATED_TO)

        assert description == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                             HelpDeskConstants.FIRST_DESCRIPTION)

        assert notes == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                       HelpDeskConstants.FIRST_NOTES)

        assert priority == Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_INFO,
                                                          HelpDeskConstants.FIRST_PRIORITY)
