from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.help_desk.HelpDeskPrecondition import HelpDeskPrecondition


class HelpDeskTest(BaseTest):

    def test_create_ticket(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()

        detail_view_page_service_desk_module = HelpDeskPage().select_filter(
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        tittle = detail_view_page_service_desk_module.get_title_text()
        category = detail_view_page_service_desk_module.get_category_text()
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

        HelpDeskPrecondition().create_first_ticket()

        HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
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
        category = detail_view_page_service_desk_module.get_category_text()
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

    def test_searching_in_help_desk_by_ticket_number(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        ticket_number = detail_view_page_service_desk_module.get_ticket_number_text()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        ticket_number_id = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.TICKET_NUMBER) \
            .enter_search_for_field(ticket_number) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_ticket_number_text()

        assert ticket_number == ticket_number_id

    def test_searching_in_help_desk_by_tittle(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        tittle = detail_view_page_service_desk_module.get_title_text()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        tittle_view_page = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.TITLE) \
            .enter_search_for_field(tittle) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_title_text()

        assert tittle == tittle_view_page

    def test_searching_in_help_desk_by_priority(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        priority = detail_view_page_service_desk_module.get_priority_text()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        priority_id = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.PRIORITY) \
            .enter_search_for_field(priority) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_account_name()

        assert priority == priority_id

    def test_searching_in_help_desk_by_assigned_to(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        assigned = detail_view_page_service_desk_module.get_assigned_to_text()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        assigned_id = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.ASSIGNED_TO_TYPE) \
            .enter_search_for_field(assigned) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_assigned_to_text()

        assert assigned == assigned_id

    def test_searching_in_help_desk_by_status(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        status = detail_view_page_service_desk_module.get_ticket_status_text()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        status_id = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.STATUS) \
            .enter_search_for_field(status) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_ticket_status_text()

        assert status == status_id

    def test_searching_in_help_desk_by_ca_id(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        ca_id = detail_view_page_service_desk_module.get_ca_id_text()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        ca_id_view_page = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.CA_ID_TYPE) \
            .enter_search_for_field(ca_id) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_ca_id_text()

        assert ca_id == ca_id_view_page

    def test_searching_in_help_desk_by_category(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                   TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        category = detail_view_page_service_desk_module.get_category_text()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        category_view_page = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.CATEGORY) \
            .enter_search_for_field(category) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_category_text()

        assert category == category_view_page

    def test_searching_in_help_desk_by_brand(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                   TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        brand = detail_view_page_service_desk_module.get_brand_text()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        brand_view_page = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.BRAND) \
            .enter_search_for_field(brand) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_brand_text()

        assert brand == brand_view_page

    def test_searching_in_help_desk_by_description(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                   TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        description = detail_view_page_service_desk_module.get_description_text()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        description_view_page = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.DESCRIPTION) \
            .enter_search_for_field(description) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_description_text()

        assert description == description_view_page

    def test_searching_in_help_desk_by_related_to(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                   TestDataConstants.CRM_PASSWORD))

        HelpDeskPrecondition().create_first_ticket()
        detail_view_page_service_desk_module = HelpDeskPage().select_filter(Config.data.get_data_help_desk(
            HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME)) \
            .find_ticket_by_title(HelpDeskConstants.FIRST_TITTLE) \
            .perform_search_ticket() \
            .open_ticket_number()

        account_name = detail_view_page_service_desk_module.get_account_name()
        detail_view_page_service_desk_module.came_back_on_previous_page()

        account_name_id = HelpDeskPage().click_searching_in_help_desk() \
            .select_in_column(HelpDeskConstants.ACCOUNT_NAME) \
            .enter_search_for_field(account_name) \
            .click_search_now_button() \
            .open_ticket_number() \
            .get_account_name()

        assert account_name == account_name_id

    def tearDown(self):
            self.widget.dispose()
            self.widget = None
