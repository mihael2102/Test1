from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.ca.model.constants.sign_up.SignUpFirstStepConstants import SignUpFirstStepConstants
from src.main.python.ui.crm.model.pages.clients_ui.ClientEditPageUI import ClientEditPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientEditConstantsUI import ClientEditConstantsUI
from src.main.python.ui.ca.model.constants.sign_up.CaUpdateClientConstants import CaUpdateClientConstants
from src.main.python.ui.ca.model.pages.ca_pages_ui.PersonalDetailsPage import PersonalDetailsPage
from src.main.python.ui.ca.model.constants.main_page.MainPageConstants import MainPageConstants
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from src.main.python.ui.ca.model.constants.client_area.ServiceDeskConstants import ServiceDeskConstants
from src.main.python.ui.ca.model.pages.ca_pages_ui.ServiceDeskPage import ServiceDeskPage
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDModuleConstantsUI import HDModuleConstantsUI
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskCreateTicketPageUI import HelpDeskCreateTicketPageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HDCreateTicketConstantsUI import HDCreateTicketConstantsUI
from src.main.python.ui.ca.model.pages.ca_pages_ui.MainPage import MainPage
from src.main.python.ui.ca.model.pages.ca_pages_ui.LoginPage import LoginPage


class CaSupportTicketPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_ticket_ca(self):
        """ Log in CA """
        LoginPage(self.driver) \
            .open_first_tab_page(url=self.config.get_value('url_ca')) \
            .login(email=SignUpFirstStepConstants.EMAIL,
                   password=SignUpFirstStepConstants.PASSWORD) \
            .click_hi_user() \
            .click_main_menu_item(item=MainPageConstants.ITEM_SERV_DESK)

        """ Create ticket """
        ca_ticket_id = ServiceDeskPage(self.driver)\
            .create_ticket(start_button=ServiceDeskConstants.BTN_START,
                           field1=ServiceDeskConstants.FIELD_SUBJECT, subject=ServiceDeskConstants.SUBJECT,
                           list1=ServiceDeskConstants.LIST_CATEGORY, category=ServiceDeskConstants.CATEGORY,
                           field2=ServiceDeskConstants.FIELD_DESCRIPTION, description=ServiceDeskConstants.DESCRIPTION,
                           final_button=ServiceDeskConstants.BTN_FINAL) \
            .get_ca_ticket_id()

        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login_second_tab(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module and find created client by email """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        ClientsModulePageUI(self.driver) \
            .select_filter_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(column=ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   data=SignUpFirstStepConstants.EMAIL) \
            .click_crm_id_ui('1') \
            .open_tab(ClientDetailsConstantsUI.TAB_HELP_DESK)

        """ Verify Ticket data in CRM """
        crm_ticket_id = ClientsModulePageUI(self.driver) \
            .get_data_from_list_view_ui(column=HDModuleConstantsUI.COLUMN_TICKET_NO,
                                        row='1')
        crm_ticket_id = crm_ticket_id.replace('TT', '')
        title = ClientsModulePageUI(self.driver) \
            .get_data_from_list_view_ui(column=HDModuleConstantsUI.COLUMN_TITLE,
                                        row='1')
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(ServiceDeskConstants.SUBJECT, title)

        """ Edit ticket in CRM """
        HelpDeskCreateTicketPageUI(self.driver)\
            .create_edit_ticket(
                edit_btn=True, row='1',
                field1=HDCreateTicketConstantsUI.FIELD_TITLE, title=ServiceDeskConstants.TITLE,
                list3=HDCreateTicketConstantsUI.LIST_STATUS, status=ServiceDeskConstants.STATUS,
                final_btn=HDCreateTicketConstantsUI.BTN_FNL_EDIT)

        """ Verify ticket updated in CA """
        MainPage(self.driver) \
            .switch_first_tab() \
            .refresh_page_ca() \
            .click_hi_user() \
            .click_main_menu_item(item=MainPageConstants.ITEM_SERV_DESK)

        ticket_data = ServiceDeskPage(self.driver)\
            .get_ticket_data(row='1')

        assert ServiceDeskConstants.TITLE in ticket_data
        assert ServiceDeskConstants.STATUS in ticket_data

        """ Edit ticket status to Closed in CRM """
        ClientDetailsPageUI(self.driver) \
            .switch_second_tab_page() \
            .refresh_client_page() \
            .open_tab(ClientDetailsConstantsUI.TAB_HELP_DESK)

        HelpDeskCreateTicketPageUI(self.driver) \
            .create_edit_ticket(
                edit_btn=True, row='1',
                list3=HDCreateTicketConstantsUI.LIST_STATUS, status=ServiceDeskConstants.STATUS_CL,
                final_btn=HDCreateTicketConstantsUI.BTN_FNL_EDIT)

        """ Verify ticket status changed to Closed in CA """
        MainPage(self.driver) \
            .switch_first_tab() \
            .refresh_page_ca() \
            .click_hi_user() \
            .click_main_menu_item(item=MainPageConstants.ITEM_SERV_DESK)

        ticket_data = ServiceDeskPage(self.driver)\
            .open_tab(ServiceDeskConstants.TAB_CLOSED) \
            .get_ticket_data(row='1')

        assert ServiceDeskConstants.STATUS_CL in ticket_data
