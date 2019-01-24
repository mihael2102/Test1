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
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        affiliate_list_view_page = CRMHomePage(self.driver).open_more_list_modules().select_affiliates_module_more_list(AffiliateModuleConstants.AFFILIATES_MODULE)
        api = affiliate_list_view_page.get_link_api()
        CRMLoginPage(self.driver).open_first_tab_page(api)
        ApiPage(self.driver).enter_secret_key(APIConstants.API_SECRET_KEY)
        ApiPage(self.driver).authorization_module()
        ApiPage(self.driver).input_partner_id(APIConstants.PARTNER_ID)
        ApiPage(self.driver).generate_time()
        ApiPage(self.driver).generate_accessKey()
        ApiPage(self.driver).send_authorization()
        check_token = ApiPage(self.driver).check_token()

        assert APIConstants.PARTNER_ID in check_token

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
        ApiPage(self.driver).send_create_customer()

        check_create_customer_token = ApiPage(self.driver).check_create_customer_token()

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

        assert client_email == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL]
        assert client_country == APIConstants.COUNTRY_CRM
        assert client_first_name == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME]
        assert client_last_name == APIConstants.LASTNAME
        assert client_phone == APIConstants.PHONE_CRM

    def test_refferal_field(self):
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

        assert APIConstants.STATUS_OK in check_create_customer_token

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
        ClientsPage(self.driver).select_filter(self.config.get_data_client(
            TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                      LeadsModuleConstants.EMAIL])
        client_email = ClientsPage(self.driver).get_first_client_email()














