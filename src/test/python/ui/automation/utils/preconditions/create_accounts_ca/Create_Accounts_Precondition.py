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
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.pages.ca.CAPage import CAPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskEditPage import HelpDeskEditPage
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage

class Create_Accounts_Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def verify_upload_document(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        ClientProfilePage(self.driver).open_document_tab()
        documents = ClientProfilePage(self.driver).verify_documents()
        assert documents == CAConstants.DOCUMENTS
        ClientProfilePage(self.driver).documents_page()
        sleep(3)
        DocumentsPage(self.driver).edit_documents()
        DocumentsPage(self.driver).select_document_status(CAConstants.STATUS_DOCUMENTS_APPROVED)
        DocumentsPage(self.driver).save_document()
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        sleep(3)
        CAPage(self.driver).open_upload_document_module()
        status = CAPage(self.driver).verify_status_documents()
        assert status == CAConstants.STATUS_DOCUMENTS_APPROVED_CA

    def upload_document(self):

        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()

        CAPage(self.driver).open_upload_document_module()
        CAPage(self.driver).browse_documents()
        sleep(5)



    def open_ticket_ca(self):

        ##CREATE NEW TICKET

        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()

        CAPage(self.driver).open_service_desk()
        CAPage(self.driver).open_new_ticket()\
                           .enter_subject(CAConstants.TICKET_SUBJECT)\
                           .enter_description(CAConstants.TICKET_DESCRIPTION)\
                           .select_category(CAConstants.TICKET_CATEGORY)\
                           .click_submit_ticket()

        ca_ticket_number_v1 = CAPage(self.driver).get_ticket_number()
        ca_ticket_number_v2 = ca_ticket_number_v1.replace(' Was Submitted Successfuly','')
        ca_ticket_number = ca_ticket_number_v2.replace('Ticket No. ', '')
        CAPage(self.driver).close_popup_create()
        ca_ticket_status = CAPage(self.driver).verify_ticket_status()

        ##VERIFY AND CHANGE STATUS TO IN PROGRESS IN CRM

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])

        ClientProfilePage(self.driver).open_help_desk_tab()
        crm_ticket_number = ClientProfilePage(self.driver).verify_ticket_number()
        crm_ticket_status = ClientProfilePage(self.driver).verify_ticket_status()
        ClientProfilePage(self.driver).change_status_ticket()

        HelpDeskEditPage(self.driver).select_status(CAConstants.TICKET_IN_PROGRESS)
        HelpDeskEditPage(self.driver).click_save_button()

        crm_ticket_status_upper = crm_ticket_status.upper()

        ##VERIFY STATUS IN CA

        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CAPage(self.driver).open_service_desk()
        # ca_ticket_status_in_progress = CAPage(self.driver).verify_ticket_status()

        ##VERIFY AND CHANGE STATUS TO CLOSED IN CRM

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        ClientsPage(self.driver).select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        sleep(3)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        # ClientProfilePage(self.driver).open_help_desk_tab()
        sleep(3)
        ClientProfilePage(self.driver).change_status_ticket()
        sleep(3)
        HelpDeskEditPage(self.driver).select_status(CAConstants.TICKET_CLOSED)
        sleep(3)
        HelpDeskEditPage(self.driver).click_save_button()

        ##VERIFY STATUS IN CA

        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CAPage(self.driver).open_service_desk()
        sleep(3)
        ca_ticket_status_in_closed = CAPage(self.driver).verify_ticket_status_closed()

        ##VERIFY AND CHANGE STATUS TO OPEN IN CRM

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        ClientsPage(self.driver).select_filter(
            self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        sleep(3)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        sleep(3)
        # ClientProfilePage(self.driver).open_help_desk_tab()
        sleep(3)
        ClientProfilePage(self.driver).change_status_ticket()
        sleep(3)
        HelpDeskEditPage(self.driver).select_status(CAConstants.TICKET_OPEN_CRM)
        sleep(3)
        HelpDeskEditPage(self.driver).click_save_button()

        ##VERIFY STATUS IN CA

        # CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        # CAPage(self.driver).open_service_desk()

        assert ca_ticket_status == CAConstants.TICKET_OPEN
        assert crm_ticket_number == ca_ticket_number
        assert crm_ticket_status_upper == ca_ticket_status
        # assert ca_ticket_status_in_progress == CAConstants.TICKET_IN_PROGRESS_CA
        assert ca_ticket_status_in_closed == CAConstants.TICKET_CLOSED_CA







    def check_demo_in_crm(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        ClientProfilePage(self.driver).open_trading_accounts_tab()
        demo = ClientsPage(self.driver).check_demo_account()

        assert demo == CAConstants.DEMO


    def update_details(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()\
            .click_personal_details()\
            .update_address(CAConstants.NEW_ADDRESS)\
            .update_city(CAConstants.NEW_CITY)\
            .update_code(CAConstants.NEW_CODE)\
            .submit_personal_details()

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])

        address = ClientsPage(self.driver).get_client_address()
        city = ClientsPage(self.driver).get_client_city()
        code = ClientsPage(self.driver).get_client_code()

        assert CAConstants.NEW_ADDRESS in address
        assert CAConstants.NEW_CITY in city
        assert CAConstants.NEW_CODE in code

    def create_live_account(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()
        CAPage(self.driver).open_live_account()
        if global_var.current_brand_name == "finmarket":
            CALoginPage(self.driver).enter_data_birth(CAConstants.DATA_MONTH_YEAR)

        else:
            CALoginPage(self.driver).select_data_birth_day(CAConstants.DAY_BIRTH) \
                                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                                .select_data_birth_year(CAConstants.YEAR_BIRTH)

        if global_var.current_brand_name != "itrader_global" and global_var.current_brand_name != "oinvestsa" and global_var.current_brand_name != "finmarket":
            CALoginPage(self.driver).choose_currency(CAConstants.CURRENCY)
        if global_var.current_brand_name == "oinvestsa":
            CALoginPage(self.driver).choose_currency(CAConstants.CURRENCY_USD)


        CALoginPage(self.driver).fill_city(CAConstants.CITY) \
                            .fill_zip_code(CAConstants.ZIP_CODE) \
                            .fill_address(CAConstants.ADDRESS)

        CALoginPage(self.driver).click_next_open_live_account()
        # CALoginPage(self.driver).my_account_link()
        CAPage(self.driver).click_check_box_confirm()
        CAPage(self.driver).click_confirm()
        currency = CAPage(self.driver).verify_relevant_currency()
        assert currency == CAConstants.CURRENCY
        data = CAPage(self.driver).verify_correct_data()

        assert data == CAConstants.LEVERAGE


    def create_demo_account(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()

        CAPage(self.driver).open_demo_account()
        CAPage(self.driver).select_currency()
        CAPage(self.driver).select_leverage()
        CAPage(self.driver).select_deposit()
        CAPage(self.driver).click_submit()
        CAPage(self.driver).finish_button()

