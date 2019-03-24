from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.affiliates.AffiliatePage import AffiliatePage
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants.APIConstants import APIConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
import re
import time
from time import sleep

class ApiPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def autorization_process(self):
        """ Login to CRM """
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        affiliate_list_view_page = CRMHomePage(self.driver).open_more_list_modules().select_affiliates_module_more_list(AffiliateModuleConstants.AFFILIATES_MODULE)
        if global_var.current_brand_name == "eafx":
            AffiliatePage(self.driver).search_by_partner_id(APIConstants.PARTNER_ID_EAFX)
        elif global_var.current_brand_name == "uft":
            AffiliatePage(self.driver).search_by_partner_id(APIConstants.PARTNER_ID_UFT)
        else:
            AffiliatePage(self.driver).search_by_partner_id(APIConstants.PARTNER_ID)
        AffiliatePage(self.driver).open_edit_affiliate()
        selected_methods = AffiliatePage(self.driver).check_selected_methods()
        if "Selected" in selected_methods:
            AffiliatePage(self.driver).add_all_methods()
            selected_methods_new = AffiliatePage(self.driver).check_selected_methods()
            if "None selected" in selected_methods_new:
                AffiliatePage(self.driver).add_all_methods()
        else:
            AffiliatePage(self.driver).add_all_methods()

        selected_countries = AffiliatePage(self.driver).check_selected_countries()
        if "Selected" in selected_countries:
            AffiliatePage(self.driver).add_none_selected_countries()
            selected_countries_new = AffiliatePage(self.driver).check_selected_countries()
            if "None selected" in selected_countries_new:
                AffiliatePage(self.driver).click_submit()
            else:
                AffiliatePage(self.driver).add_none_selected_countries()
                AffiliatePage(self.driver).click_submit()
        else:
            AffiliatePage(self.driver).click_submit()

        secret_key = AffiliatePage(self.driver).copy_secret_key()

        api = affiliate_list_view_page.get_link_api()
        CRMLoginPage(self.driver).open_first_tab_page(api)
        ApiPage(self.driver).enter_secret_key(secret_key)
        ApiPage(self.driver).authorization_module()
        if global_var.current_brand_name == "eafx":
            ApiPage(self.driver).input_partner_id(APIConstants.PARTNER_ID_EAFX)
        elif global_var.current_brand_name == "uft":
            ApiPage(self.driver).input_partner_id(APIConstants.PARTNER_ID_UFT)
        else:
            ApiPage(self.driver).input_partner_id(APIConstants.PARTNER_ID)
        ApiPage(self.driver).generate_time()
        ApiPage(self.driver).generate_accessKey()
        ApiPage(self.driver).send_authorization()
        check_token = ApiPage(self.driver).check_token()

        # assert APIConstants.PARTNER_ID or APIConstants.PARTNER_ID_EAFX in check_token
        assert APIConstants.STATUS_OK in check_token

    def test_create_new_customer(self):
        self.autorization_process()
        ApiPage(self.driver).create_customer_module()
        ApiPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])
        ApiPage(self.driver).enter_password(APIConstants.PASSWORD)
        ApiPage(self.driver).enter_country(APIConstants.COUNTRY)
        ApiPage(self.driver).enter_firstName(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])
        ApiPage(self.driver).enter_lastName(APIConstants.LASTNAME)
        ApiPage(self.driver).enter_phone(APIConstants.PHONE)
        ApiPage(self.driver).enter_refferal(APIConstants.REFFERAL)
        ApiPage(self.driver).send_create_customer()

        check_create_customer_token = ApiPage(self.driver).check_create_customer_token()
        count = 0
        while(APIConstants.STATUS_OK not in check_create_customer_token):
            sleep(1)
            check_create_customer_token = ApiPage(self.driver).check_create_customer_token()
            count += 1
            if count == 5:
                break

        assert APIConstants.STATUS_OK in check_create_customer_token

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        ClientsPage(self.driver).select_filter(self.config.get_data_client(
            TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])
        client_email = ClientsPage(self.driver).get_first_client_email()
        client_country = ClientsPage(self.driver).get_client_country()
        client_first_name = ClientsPage(self.driver).get_client_first_name()
        client_last_name = ClientsPage(self.driver).get_client_last_name()
        client_phone = ClientsPage(self.driver).get_client_phone()
        ClientsPage(self.driver).click_custom_information()
        refferal1 = ClientsPage(self.driver).get_refferal_client()
        refferal = refferal1.replace('  ','')

        if global_var.current_brand_name != "royal_cfds":
            assert client_email == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                            LeadsModuleConstants.EMAIL]
        assert client_country == APIConstants.COUNTRY_CRM
        assert client_first_name == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME]
        assert client_last_name == APIConstants.LASTNAME
        assert client_phone == APIConstants.PHONE_CRM
        assert refferal == APIConstants.REFFERAL


    def test_read_customer_details(self):
        self.autorization_process()
        ApiPage(self.driver).read_customer_module()
        ApiPage(self.driver).enter_email_for_read_customer(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])
        ApiPage(self.driver).send_read_customer()
        token = ApiPage(self.driver).check_read_customer_details()
        count = 0
        while (self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL] not in token):
            time.sleep(2)
            token = ApiPage(self.driver).check_read_customer_details()
            count += 1
            if count == 5:
                break
        assert self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL] in token
        assert APIConstants.REFFERAL in token
        assert APIConstants.COUNTRY in token
        assert APIConstants.LASTNAME in token
        assert self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME] in token


    def test_read_customers_details(self):
        self.autorization_process()
        ApiPage(self.driver).read_customers_module()
        ApiPage(self.driver).enter_page(APIConstants.PAGE)
        ApiPage(self.driver).enter_limit(APIConstants.LIMIT)
        ApiPage(self.driver).send_read_customers()
        time.sleep(7)
        token = ApiPage(self.driver).check_reads_customer_details()
        assert APIConstants.PANDATS_EMAIL in token
        # assert len(re.findall(r'\b{}\b'.format(APIConstants.PANDATS_EMAIL), token)) == 5

        # CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        # ClientsPage(self.driver).select_filter(APIConstants.API_filter)
        # client1, client2, client3, client4, client5 = ClientsPage(self.driver).get_first_clients()
        #
        # assert client1 in token
        # assert client2 in token
        # assert client3 in token
        # assert client4 in token
        # assert client5 in token

    def test_update_customer(self):
        self.autorization_process()
        ApiPage(self.driver).update_customer_module()
        ApiPage(self.driver).enter_email_for_update(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])
        ApiPage(self.driver).change_first_name(APIConstants.CHANGE_FIRST_NAME)
        ApiPage(self.driver).change_postalCode(APIConstants.CHANGE_POSTAL_CODE)
        ApiPage(self.driver).change_phone(APIConstants.CHANGE_PHONE)
        ApiPage(self.driver).send_update_customer()
        token = ApiPage(self.driver).check_update_token()

        assert APIConstants.STATUS_OK in token

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        ClientsPage(self.driver).select_filter(self.config.get_data_client(
            TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])
        client_email = ClientsPage(self.driver).get_first_client_email()
        client_first_name = ClientsPage(self.driver).get_client_first_name()
        client_phone = ClientsPage(self.driver).get_client_phone()
        ClientsPage(self.driver).click_custom_information()
        client_postalCode = ClientsPage(self.driver).get_client_postalCode()

        assert client_email == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL]

        assert client_first_name == APIConstants.CHANGE_FIRST_NAME

        assert client_phone == APIConstants.CHANGE_PHONE_CRM

        assert client_postalCode == APIConstants.CHANGE_POSTAL_CODE

    def test_create_lead(self):
        self.autorization_process()
        ApiPage(self.driver).create_lead_module()
        ApiPage(self.driver).enter_email_lead(self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)[LeadsModuleConstants.EMAIL])
        ApiPage(self.driver).enter_firstName_lead(APIConstants.LEAD_FNAME)
        ApiPage(self.driver).enter_lastName_lead(APIConstants.LEAD_LNAME)
        ApiPage(self.driver).enter_phone_lead(APIConstants.LEAD_PHONE)
        ApiPage(self.driver).send_create_lead()
        token = ApiPage(self.driver).check_create_lead_token()
        assert APIConstants.STATUS_OK in token

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

        lead_module = CRMHomePage(self.driver) \
            .open_lead_module()

        lead_module.select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))

        lead_module.perform_searching_lead_by_mail(self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)
                                                   [LeadsModuleConstants.EMAIL])
        lead_module.open_personal_details_lead()
        email = lead_module.get_lead_email()
        fname = lead_module.get_lead_fname()
        lname = lead_module.get_lead_lname()
        phone = lead_module.get_lead_phone()

        assert email == self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)[LeadsModuleConstants.EMAIL]
        assert fname == APIConstants.LEAD_FNAME
        assert lname == APIConstants.LEAD_LNAME
        assert phone == APIConstants.LEAD_PHONE_CRM


    def test_read_leads(self):

        self.autorization_process()
        ApiPage(self.driver).read_leads_module()
        ApiPage(self.driver).enter_leads_page(APIConstants.PAGE)
        ApiPage(self.driver).enter_leads_limit(APIConstants.LIMIT)
        ApiPage(self.driver).send_leads_read()
        token = ApiPage(self.driver).check_read_leads_token()
        assert APIConstants.PANDATS_EMAIL in token
        # assert len(re.findall(r'\b{}\b'.format(APIConstants.PANDATS_EMAIL), token)) == 5

        # CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        #
        # lead_module = CRMHomePage(self.driver) \
        #     .open_lead_module()
        #
        # lead_module.select_filter(APIConstants.API_filter)
        #
        # lead1, lead2, lead3, lead4, lead5 = CRMHomePage(self.driver).get_first_leads()
        #
        # assert lead1 in token
        # assert lead2 in token
        # assert lead3 in token
        # assert lead4 in token
        # assert lead5 in token

    def login_token(self):

        self.autorization_process()
        ApiPage(self.driver).login_token_module()
        ApiPage(self.driver).enter_email_for_login_token(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])
        ApiPage(self.driver).send_login_token()
        token = ApiPage(self.driver).check_login_token()
        token_new = token.replace(' ','')
        token_new_1 = token_new.replace('{\n"data":{\n"url":"','')
        token_new_2 = token_new_1.replace('"\n}\n}', '')

        CRMLoginPage(self.driver).open_first_tab_page(token_new_2)

        assert APIConstants.FOREX_DEPOSIT in token_new_2

        # payment_details = ApiPage(self.driver).check_page_from_token()
        #
        # assert payment_details == APIConstants.PAYMENT_DETAILS




















































