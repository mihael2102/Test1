from src.main.python.ui.brand.model.client_area_modules.service_desk.CaServiceDesk import CaServiceDesk
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.modules.help_desk.HelpDeskModule import HelpDeskModule
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.filter.FilterPrecondition import FilterPrecondition
from src.test.python.utils.TestDataConstants import TestDataConstants


class CreateSupportTicketTestCa(BaseTest):

    def test_create_ticket(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area) \
            .login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(TestDataConstants.SERVICE_DESK)

        brand_service_desk = CaServiceDesk()

        subject_ca = brand_service_desk \
            .open_tickets_tab() \
            .create_new_ticket() \
            .set_subject_field(TestDataConstants.SUBJECT) \
            .set_category_drop_down(TestDataConstants.CATEGORY_FIRST) \
            .set_description(TestDataConstants.DESCRIPTION) \
            .open_new_ticket_button() \
            .get_subject_id_text()

        category_tittle_ca = brand_service_desk.get_category_tittle()
        ticket_status_ca = brand_service_desk.get_ticket_status()
        ca_id = brand_service_desk.get_ca_id()

        FilterPrecondition().test_create_filter_service_desc()

        detail_view_page_service_desk_module = HelpDeskModule().find_ticket_by_id(ca_id) \
            .perform_search_ticket() \
            .open_ticket_number()

        category_tittle_crm = detail_view_page_service_desk_module.get_category_status_text()
        ticket_status_crm = detail_view_page_service_desk_module.get_ticket_status_text()
        subject_crm = detail_view_page_service_desk_module.get_subject_tittle()

        assert subject_ca == subject_crm
        assert category_tittle_ca == category_tittle_crm
        assert ticket_status_ca == ticket_status_crm
