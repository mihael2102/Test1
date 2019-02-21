from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from src.main.python.ui.ca.model.pages.login.CAPage import CAPage
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskEditPage import HelpDeskEditPage
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants


class Support_Ticket_Preconditions(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def create_support_ticket(self):
        if global_var.current_brand_name != "q8":
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                    .login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login() \
                                    .verify() \
                                    .open_ca_menu()
            CAPage(self.driver).open_service_desk() \
                               .click_create_new_ticket() \
                               .set_subject_field(CAConstants.TICKET_SUBJECT) \
                               .set_category_drop_down(CAConstants.CATEGORY) \
                               .set_description(CAConstants.TICKET_DESCRIPTION) \
                               .open_new_ticket_button() \
                               .get_ca_ticket_id()
        else:
            return self

    def check_and_update_ticket_in_crm(self):
        # Login to CRM
        if global_var.current_brand_name != "q8":
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD)) \
                .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

            sleep(2)
            ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                              LeadsModuleConstants.EMAIL])
            sleep(2)
            ClientProfilePage(self.driver).open_help_desk_tab() \
                                          .check_help_desk_ticket_exist(CAConstants.TICKET_NUMBER_CA) \
                                          .click_edit_help_desk_ticket() \
                                          .set_help_desk_title(HelpDeskConstants.FIRST_TITTLE) \
                                          .set_help_desk_status(HelpDeskConstants.EDIT_HT_STATUS) \
                                          .click_save_button()
        else:
            return self

    def check_updated_ticket_in_ca(self):
        if global_var.current_brand_name != "q8":
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                    .login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login() \
                                    .verify() \
                                    .open_ca_menu()
            CAPage(self.driver).open_service_desk() \
                               .open_closed_tickets_tab() \
                               .found_closed_ticket(CAConstants.TICKET_NUMBER_CA) \
                               .verify_closed_ticket_title(HelpDeskConstants.FIRST_TITTLE) \
                               .check_ticket_status(HelpDeskConstants.EDIT_HT_STATUS)
        else:
            return self


