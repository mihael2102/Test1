from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
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
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        affiliate_list_view_page = CRMHomePage(self.driver)\
            .open_more_list_modules().select_affiliates_module_more_list(AffiliateModuleConstants.AFFILIATES_MODULE)

        if global_var.current_brand_name == "gmo":
            AffiliatePage(self.driver).search_by_partner_id(APIConstants.PARTNER_ID_GMO)
        elif global_var.current_brand_name == "kbcapitals":
            AffiliatePage(self.driver).search_by_partner_id(APIConstants.PARTNER_ID_KB)
        elif global_var.current_brand_name == "oinvestsa":
            AffiliatePage(self.driver).search_by_partner_id(APIConstants.PARTNER_ID_OI)
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
        if global_var.current_brand_name == "gmo":
            ApiPage(self.driver).input_partner_id(APIConstants.PARTNER_ID_GMO)
        elif global_var.current_brand_name == "kbcapitals":
            ApiPage(self.driver).input_partner_id(APIConstants.PARTNER_ID_KB)
        elif global_var.current_brand_name == "oinvestsa":
            ApiPage(self.driver).input_partner_id(APIConstants.PARTNER_ID_OI)
        else:
            ApiPage(self.driver).input_partner_id(APIConstants.PARTNER_ID)

        ApiPage(self.driver).generate_time()
        ApiPage(self.driver).generate_accessKey()
        ApiPage(self.driver).send_authorization()
        check_token = ApiPage(self.driver).check_token()
        time.sleep(10)
        assert APIConstants.STATUS_OK in check_token

    def autorization_process_short(self):
        """ Login to CRM """
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        affiliate_list_view_page = CRMHomePage(self.driver)\
            .open_more_list_modules()\
            .select_affiliates_module_more_list(AffiliateModuleConstants.AFFILIATES_MODULE)

        if global_var.current_brand_name == "gmo":
            AffiliatePage(self.driver)\
                .search_by_partner_id(APIConstants.PARTNER_ID_GMO)
        elif global_var.current_brand_name == "kbcapitals":
            AffiliatePage(self.driver)\
                .search_by_partner_id(APIConstants.PARTNER_ID_KB)
        elif global_var.current_brand_name == "oinvestsa":
            AffiliatePage(self.driver)\
                .search_by_partner_id(APIConstants.PARTNER_ID_OI)
        else:
            AffiliatePage(self.driver)\
                .search_by_partner_id(APIConstants.PARTNER_ID)

        secret_key = AffiliatePage(self.driver)\
            .copy_secret_key()

        api = affiliate_list_view_page\
            .get_link_api()
        CRMLoginPage(self.driver)\
            .open_first_tab_page(api)
        ApiPage(self.driver)\
            .enter_secret_key(secret_key)\
            .authorization_module()
        if global_var.current_brand_name == "gmo":
            ApiPage(self.driver)\
                .input_partner_id(APIConstants.PARTNER_ID_GMO)
        elif global_var.current_brand_name == "kbcapitals":
            ApiPage(self.driver)\
                .input_partner_id(APIConstants.PARTNER_ID_KB)
        elif global_var.current_brand_name == "oinvestsa":
            ApiPage(self.driver)\
                .input_partner_id(APIConstants.PARTNER_ID_OI)
        else:
            ApiPage(self.driver)\
                .input_partner_id(APIConstants.PARTNER_ID)

        ApiPage(self.driver)\
            .generate_time()\
            .generate_accessKey()\
            .send_authorization()
        check_token = ApiPage(self.driver).check_token()
        time.sleep(1)
        assert APIConstants.STATUS_OK in check_token

    def test_create_new_customer(self):
        self.autorization_process_short()
        ApiPage(self.driver).create_customer_module()
        ApiPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])
        ApiPage(self.driver).enter_password(APIConstants.PASSWORD)
        if global_var.current_brand_name == "oinvestsa":
            ApiPage(self.driver).enter_country(APIConstants.COUNTRY_SA)
        elif global_var.current_brand_name == "itrader_global":
            ApiPage(self.driver).enter_country(APIConstants.COUNTRY_MX)
        elif global_var.current_brand_name == "gmo":
            ApiPage(self.driver).enter_country(APIConstants.COUNTRY_AUS)
        else:
            ApiPage(self.driver).enter_country(APIConstants.COUNTRY)
        ApiPage(self.driver).enter_firstName(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])
        ApiPage(self.driver).enter_lastName(APIConstants.LASTNAME)
        ApiPage(self.driver).enter_phone(APIConstants.PHONE)
        ApiPage(self.driver).enter_refferal(APIConstants.REFFERAL)
        ApiPage(self.driver).send_create_customer()

        check_create_customer_token = ApiPage(self.driver).check_create_customer_token()
        sleep(3)
        count = 0
        while APIConstants.STATUS_OK not in check_create_customer_token:
            sleep(2)
            check_create_customer_token = ApiPage(self.driver).check_create_customer_token()
            count += 1
            if count == 5:
                break
        assert APIConstants.STATUS_OK in check_create_customer_token

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        ClientsPage(self.driver).select_filter(self.config.get_data_client(
            TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        if (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "gmo"):
            ClientsPage(self.driver) \
                .find_client_by_fname(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME))
        else:
            ClientsPage(self.driver) \
                .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
        client_email = ClientsPage(self.driver).get_first_client_email()
        client_country = ClientsPage(self.driver).get_client_country()
        client_first_name = ClientsPage(self.driver).get_client_first_name()
        client_last_name = ClientsPage(self.driver).get_client_last_name()
        client_phone = ClientsPage(self.driver).get_client_phone()
        ClientsPage(self.driver).click_custom_information()
        refferal = ""
        if global_var.current_brand_name != "itrader" and global_var.current_brand_name != "oinvestsa" and \
                global_var.current_brand_name != "gmo":
            refferal = ClientsPage(self.driver).get_refferal_client()

        try:
            assert client_email == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                            LeadsModuleConstants.EMAIL]
        except:
            assert "*" in client_email
        if global_var.current_brand_name == "oinvestsa":
            assert client_country == APIConstants.COUNTRY_CRM_SA
        elif global_var.current_brand_name == "itrader_global":
            assert client_country == APIConstants.COUNTRY_MX_CRM
        elif global_var.current_brand_name == "gmo":
            assert client_country == APIConstants.COUNTRY_CRM_AUS
        else:
            assert client_country == APIConstants.COUNTRY_CRM
        assert client_first_name == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME]
        assert client_last_name == APIConstants.LASTNAME
        if '*' not in client_phone:
            assert client_phone == APIConstants.PHONE_CRM
        if global_var.current_brand_name != "itrader" and global_var.current_brand_name != "oinvestsa" and \
                global_var.current_brand_name != "gmo":
            assert APIConstants.REFFERAL in refferal

    def test_read_customer_details(self):
        self.autorization_process_short()
        ApiPage(self.driver).read_customer_module()
        ApiPage(self.driver).enter_email_for_read_customer(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])
        ApiPage(self.driver).send_read_customer()
        token = ApiPage(self.driver).check_read_customer_details()
        count = 0
        while (self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL] not in token):
            sleep(2)
            token = ApiPage(self.driver).check_read_customer_details()
            count += 1
            if count == 5:
                break
        assert self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL] in token
        assert APIConstants.REFFERAL in token
        if global_var.current_brand_name == "gmo":
            assert APIConstants.COUNTRY_AUS in token
        else:
            assert APIConstants.COUNTRY in token
        assert APIConstants.LASTNAME in token
        assert self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME] in token

    def test_read_customers_details(self):
        self.autorization_process_short()
        ApiPage(self.driver).read_customers_module()
        ApiPage(self.driver).enter_page(APIConstants.PAGE)
        ApiPage(self.driver).enter_limit(APIConstants.LIMIT)
        ApiPage(self.driver).send_read_customers()
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
        self.autorization_process_short()
        ApiPage(self.driver).update_customer_module()
        ApiPage(self.driver).enter_email_for_update(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])
        ApiPage(self.driver).change_first_name(APIConstants.CHANGE_FIRST_NAME)
        ApiPage(self.driver).change_postalCode(APIConstants.CHANGE_POSTAL_CODE)
        # ApiPage(self.driver).change_phone(APIConstants.CHANGE_PHONE)
        ApiPage(self.driver).send_update_customer()
        token = ApiPage(self.driver).check_update_token()

        assert APIConstants.STATUS_OK in token

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        ClientsPage(self.driver).select_filter(self.config.get_data_client(
            TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        if (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "gmo"):
            ClientsPage(self.driver) \
                .find_client_by_fname(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME))
        else:
            ClientsPage(self.driver) \
                .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
        client_email = ClientsPage(self.driver).get_first_client_email()
        client_first_name = ClientsPage(self.driver).get_client_first_name()
        # client_phone = ClientsPage(self.driver).get_client_phone()
        ClientsPage(self.driver).click_custom_information()
        client_postalCode = ClientsPage(self.driver).get_client_postalCode()

        try:
            assert client_email == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                           LeadsModuleConstants.EMAIL]
        except:
            assert "*" in client_email

        assert client_first_name == APIConstants.CHANGE_FIRST_NAME

        # assert client_phone == APIConstants.CHANGE_PHONE_CRM

        assert client_postalCode == APIConstants.CHANGE_POSTAL_CODE

    def test_create_lead(self):
        self.autorization_process_short()
        ApiPage(self.driver).create_lead_module()
        ApiPage(self.driver).enter_email_lead(
            self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)[LeadsModuleConstants.EMAIL])
        ApiPage(self.driver).enter_firstName_lead(APIConstants.LEAD_FNAME)
        ApiPage(self.driver).enter_lastName_lead(APIConstants.LEAD_LNAME)
        ApiPage(self.driver).enter_phone_lead(APIConstants.LEAD_PHONE)
        ApiPage(self.driver).send_create_lead()
        token = ApiPage(self.driver).check_create_lead_token()
        count1 = 0
        while APIConstants.STATUS_ERROR in token:
            ApiPage(self.driver).create_lead_module()
            ApiPage(self.driver).enter_email_lead(
                self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)[LeadsModuleConstants.EMAIL])
            ApiPage(self.driver).enter_firstName_lead(APIConstants.LEAD_FNAME)
            ApiPage(self.driver).enter_lastName_lead(APIConstants.LEAD_LNAME)
            ApiPage(self.driver).enter_phone_lead(APIConstants.LEAD_PHONE2)
            ApiPage(self.driver).send_create_lead()
            token = ApiPage(self.driver).check_create_lead_token()
            count1 += 1
            if count1 == 5:
                break
        count = 0
        while APIConstants.STATUS_OK not in token:
            sleep(1)
            token = ApiPage(self.driver).check_create_lead_token()
            count += 1
            if count == 5:
                break
        assert APIConstants.STATUS_OK in token

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

        lead_module = CRMHomePage(self.driver) \
            .open_lead_module()

        lead_module.select_filter(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))

        lead_module.perform_searching_lead_by_fname(APIConstants.LEAD_FNAME)
        lead_module.open_personal_details_lead()
        email = lead_module.get_lead_email()
        fname = lead_module.get_lead_fname()
        lname = lead_module.get_lead_lname()
        phone = ""
        expected_phone = APIConstants.LEAD_PHONE
        print(expected_phone)
        if global_var.current_brand_name != "stoxmarket":
            phone = lead_module.get_lead_phone()
        actual_phone = re.sub('[+," "]', '', phone)
        if "*" not in email:
            assert email == self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)[LeadsModuleConstants.EMAIL]
        assert fname == APIConstants.LEAD_FNAME
        assert lname == APIConstants.LEAD_LNAME
        if '*' not in actual_phone:
            if actual_phone == APIConstants.LEAD_PHONE:
                assert actual_phone == expected_phone
            else:
                expected_phone = APIConstants.LEAD_PHONE2
                assert actual_phone == expected_phone

    def test_read_leads(self):
        self.autorization_process_short()
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
        self.autorization_process_short()
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
