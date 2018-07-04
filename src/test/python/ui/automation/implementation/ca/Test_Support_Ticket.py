import pytest

from src.main.python.ui.brand.model.client_area_modules.service_desk.CaServiceDesk import CaServiceDesk
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=4)
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

        crm_login_page = CRMLoginPage()
        crm_help_desk = crm_login_page \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD)) \
            .open_help_desk_module() \
            .select_filter(Config.data.get_data_client(TestDataConstants.FILTER)) \
            .find_ticket_by_id(ca_id) \
            .perform_search() \
            .open_ticket_number()

        category_tittle_crm = crm_help_desk.get_category_status_text()
        ticket_status_crm = crm_help_desk.get_ticket_status_text()
        subject_crm = crm_help_desk.get_subject_tittle()

        assert subject_ca == subject_crm
        assert category_tittle_ca == category_tittle_crm
        assert ticket_status_ca == ticket_status_crm
