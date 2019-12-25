from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
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
import re


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
        # Create new ticket
        CALoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()

        CAPage(self.driver)\
            .open_service_desk() \
            .open_new_ticket()\
            .enter_subject(CAConstants.TICKET_SUBJECT)\
            .enter_description(CAConstants.TICKET_DESCRIPTION)\
            .select_category(CAConstants.TICKET_CATEGORY)\
            .click_submit_ticket()

        ca_ticket_number_v1 = CAPage(self.driver).get_ticket_number()
        ca_ticket_number = int(re.search(r'\d+', ca_ticket_number_v1).group(0))
        CAPage(self.driver).close_popup_create()
        ca_ticket_status = CAPage(self.driver).verify_ticket_status()
        assert ca_ticket_status == CAConstants.TICKET_OPEN

        # Verify and change status to 'IN PROGRESS' in CRM
        # CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
        #     .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
        #                self.config.get_value(TestDataConstants.CRM_PASSWORD),
        #                self.config.get_value(TestDataConstants.OTP_SECRET)) \
        #     .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        #
        # sleep(2)
        # ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
        #                                                   LeadsModuleConstants.EMAIL])
        #
        # ClientProfilePage(self.driver).open_help_desk_tab()
        # crm_ticket_number = ClientProfilePage(self.driver).verify_ticket_number()
        # crm_ticket_status = ClientProfilePage(self.driver).verify_ticket_status()
        # if global_var.current_brand_name == "capitalmarketsbanc":
        #     ClientProfilePage(self.driver).change_status_ticket_cmb()
        # else:
        #     ClientProfilePage(self.driver).click_edit_ticket_pensil()
        #
        # HelpDeskEditPage(self.driver).select_status(CAConstants.TICKET_IN_PROGRESS)
        # HelpDeskEditPage(self.driver).click_save_button()
        #
        # crm_ticket_status_upper = crm_ticket_status.upper()
        #
        # # Verify status in CA
        # CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        # CAPage(self.driver).open_service_desk()
        # ca_ticket_status_in_progress = CAPage(self.driver).verify_ticket_status()

        # Verify and change status to 'CLOSED' in CRM:
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL])
        ClientProfilePage(self.driver).open_help_desk_tab()
        ticket_number = ClientProfilePage(self.driver).verify_ticket_number()
        crm_ticket_number = ticket_number.replace("TT", "")
        crm_ticket_status = ClientProfilePage(self.driver).verify_ticket_status()
        assert crm_ticket_number == str(ca_ticket_number)
        assert crm_ticket_status == CAConstants.TICKET_OPEN_CRM
        if global_var.current_brand_name == "capitalmarketsbanc":
            ClientProfilePage(self.driver).change_status_ticket_cmb()
        else:
            ClientProfilePage(self.driver).click_edit_ticket_pensil()
        sleep(3)
        HelpDeskEditPage(self.driver).select_status(CAConstants.TICKET_CLOSED)
        sleep(3)
        HelpDeskEditPage(self.driver).click_save_button()

        # Verify Status has been changed to 'CLOSED' in CA:
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CAPage(self.driver).open_service_desk()
        sleep(3)
        ca_ticket_status_in_closed = CAPage(self.driver).verify_ticket_status_closed()
        assert ca_ticket_status_in_closed == CAConstants.TICKET_CLOSED_CA

        # Verify and change status to 'OPEN' in CRM:
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        ClientsPage(self.driver).select_filter(
            self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        sleep(3)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL])
        sleep(3)
        ClientProfilePage(self.driver).click_edit_ticket_pensil()
        sleep(3)
        HelpDeskEditPage(self.driver).select_status(CAConstants.TICKET_OPEN_CRM)
        sleep(3)
        HelpDeskEditPage(self.driver).click_save_button()

        # Verify status has been updated to 'OPEN' in CA:
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CAPage(self.driver).open_service_desk()
        sleep(3)
        ca_ticket_status = CAPage(self.driver).verify_ticket_status()
        assert ca_ticket_status == CAConstants.TICKET_OPEN

    def check_accounts_in_crm(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        ClientProfilePage(self.driver).open_trading_accounts_tab()
        ClientsPage(self.driver).check_account_exist_in_crm(TestDataConstants.SERVER_DEMO) \
                                .check_account_exist_in_crm(TestDataConstants.SERVER_REAL)

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
        if global_var.current_brand_name != "itrader" and global_var.current_brand_name != "gmo":
            CAPage(self.driver).open_live_account()

        if global_var.current_brand_name == "finmarket":
            CALoginPage(self.driver).enter_data_birth(CAConstants.DATA_MONTH_YEAR)
        else:
            CALoginPage(self.driver).select_data_birth_day(CAConstants.DAY_BIRTH) \
                                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                                .select_data_birth_year(CAConstants.YEAR_BIRTH)

        if global_var.current_brand_name != "itrader_global" and global_var.current_brand_name != "oinvestsa" and \
                global_var.current_brand_name != "finmarket":
            CALoginPage(self.driver).choose_currency(CAConstants.CURRENCY)
        if global_var.current_brand_name == "oinvestsa":
            CALoginPage(self.driver).choose_currency(CAConstants.CURRENCY_USD)

        if global_var.current_brand_name != "finmarket":
            CALoginPage(self.driver).fill_city(CAConstants.CITY) \
                                    .fill_zip_code(CAConstants.ZIP_CODE) \
                                    .fill_address(CAConstants.ADDRESS)
            CALoginPage(self.driver).click_next_open_live_account()
        else:
            CAPage(self.driver).open_finmarket()

        if global_var.current_brand_name == "itrader" or global_var.current_brand_name == "gmo":
            CAPage(self.driver).fill_questionarie_itrader(CAConstants.ITRADER_EMPLOYMENT_STATUS,
                                                          CAConstants.ITRADER_INDUSTRY,
                                                          CAConstants.YES,
                                                          CAConstants.ITRADER_SOURCE,
                                                          CAConstants.ESTIMATED_INCOME,
                                                          CAConstants.ESTIMATED_WORTH,
                                                          CAConstants.ITRADER_PURPOSE,
                                                          CAConstants.ESTIMATED_AMOUNT,
                                                          CAConstants.INCOMING_FUNDS,
                                                          CAConstants.ITRADER_LEVEL,
                                                          CAConstants.TIME_INVESTING,
                                                          CAConstants.TIME_LAST_TRADE,
                                                          CAConstants.INSTRUMENTS,
                                                          CAConstants.TIME_EXPERIENCE,
                                                          CAConstants.TRADE_SIZE,
                                                          CAConstants.APPLIES,
                                                          CAConstants.PRICE,
                                                          CAConstants.FB_PRICE,
                                                          CAConstants.INITIAL_DEPOSIT,
                                                          CAConstants.RESULT_OF_TRADING,
                                                          CAConstants.INVESTMENT_OBJECTIVES,
                                                          CAConstants.NO,
                                                          CAConstants.TIN)
                                                          # CAConstants.LEVERAGE_ITRADER)
            CAPage(self.driver).close_popup_itrader()

        if global_var.current_brand_name == "triomarkets":
            CAPage(self.driver).fill_questionarie_triomarket(CAConstants.AMOUNT,
                                                             CAConstants.PURPOSE,
                                                             CAConstants.ANTICIPATED,
                                                             CAConstants.EXPERIENCE,
                                                             CAConstants.LEVEL,
                                                             CAConstants.GLOSS,
                                                             CAConstants.EMPLOYMENT,
                                                             CAConstants.WORTH,
                                                             CAConstants.SOURCE_TRIO,
                                                             CAConstants.WORK,
                                                             CAConstants.RELATE,
                                                             CAConstants.YES,
                                                             CAConstants.NO,
                                                             CAConstants.LAST_TRANSACTION,
                                                             CAConstants.AMOUNT_SELECT,
                                                             CAConstants.INVESTED_VOLUME,
                                                             CAConstants.KNOWLEDGE_TRIO,
                                                             CAConstants.ACCOUNT,
                                                             CAConstants.RISK,
                                                             CAConstants.TIN)
        if global_var.current_brand_name == "oinvestsa":
            CAPage(self.driver).fill_questionarie(CAConstants.KNOWLEDGE,
                                                  CAConstants.SOURCE,
                                                  CAConstants.FUNDS,
                                                  CAConstants.CITIZEN,
                                                  CAConstants.COUNTRY,
                                                  CAConstants.TIN,
                                                  CAConstants.PEP)
        # CALoginPage(self.driver).my_account_link()
        if global_var.current_brand_name == "mlnfx":
            CAPage(self.driver).click_check_box_confirm()
            CAPage(self.driver).click_confirm()
        if global_var.current_brand_name != "itrader" and global_var.current_brand_name != "gmo":
            currency = CAPage(self.driver).verify_relevant_currency()
            data = CAPage(self.driver).verify_correct_data()

            if global_var.current_brand_name == "oinvestsa":
                assert data == CAConstants.LEVERAGE_OINVESTSA
                assert currency == CAConstants.CURRENCY_USD
            elif global_var.current_brand_name == "soarfx":
                assert data == CAConstants.LEVERAGE_SOARFX
                assert currency == CAConstants.CURRENCY
            elif global_var.current_brand_name == "capitalmarketsbanc":
                assert data == CAConstants.LEVERAGE_CMB
                assert currency == CAConstants.CURRENCY
            elif global_var.current_brand_name == "kbcapitals":
                assert data == CAConstants.LEVERAGE_KB
                assert currency == CAConstants.CURRENCY
            elif global_var.current_brand_name == "finmarket":
                assert data == CAConstants.LEVERAGE_FIN
                assert currency == CAConstants.CURRENCY_USD
            elif global_var.current_brand_name == "itrader_global":
                assert data == CAConstants.LEVERAGE_IG
                assert currency == CAConstants.CURRENCY_USD
            else:
                assert data == CAConstants.LEVERAGE
                assert currency == CAConstants.CURRENCY




    def create_demo_account(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()

        CAPage(self.driver).open_demo_account()
        CAPage(self.driver).select_currency()
        CAPage(self.driver).select_leverage()
        if global_var.current_brand_name != "itrader" and global_var.current_brand_name != "finmarket" and global_var.current_brand_name != "itrader_global":
            CAPage(self.driver).select_deposit()
        CAPage(self.driver).click_submit()
        if global_var.current_brand_name != "triomarkets" and global_var.current_brand_name != "itrader" and global_var.current_brand_name != "finmarket":
            CAPage(self.driver).finish_button()

