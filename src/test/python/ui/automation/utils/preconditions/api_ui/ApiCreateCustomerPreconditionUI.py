from src.test.python.ui.automation.utils.preconditions.api_ui.ApiAutorizationPreconditionUI import \
    ApiAutorizationPreconditionUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants.APIConstants import APIConstants
from src.main.python.ui.crm.model.constants_ui.api_ui.ApiCustomerConstantsUI import ApiCustomerConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from time import sleep


class ApiCreateCustomerPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_customer_ui(self):
        """ Autorization """
        ApiAutorizationPreconditionUI(self.driver, self.config)\
            .autorization_ui()

        """ Create Customer """
        check_create_customer_token = ApiPage(self.driver)\
            .create_customer_module() \
            .enter_email(ApiCustomerConstantsUI.EMAIL) \
            .enter_password(ApiCustomerConstantsUI.PASSWORD) \
            .enter_country(ApiCustomerConstantsUI.COUNTRY) \
            .enter_firstName(ApiCustomerConstantsUI.FNAME) \
            .enter_lastName(ApiCustomerConstantsUI.LNAME) \
            .enter_phone(ApiCustomerConstantsUI.PHONE) \
            .enter_refferal(ApiCustomerConstantsUI.REFFERAL) \
            .send_create_customer() \
            .check_create_customer_token()

        count = 0
        while APIConstants.STATUS_OK not in check_create_customer_token:
            sleep(1)
            check_create_customer_token = ApiPage(self.driver)\
                .check_create_customer_token()
            count += 1
            if count == 5:
                break

        assert APIConstants.STATUS_OK in check_create_customer_token

        """ CRM: get client's data """
        CRMLoginPageUI(self.driver) \
            .switch_first_tab_page()
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalTablePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   ApiCustomerConstantsUI.EMAIL)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        details = ClientDetailsPageUI(self.driver)
        email = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_EMAIL)
        first_name = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_FNAME)
        last_name = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_LNAME)
        phone = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_PHONE)
        country = details \
            .open_tab(ClientDetailsConstantsUI.TAB_ADDRESS_INFORMATION) \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_COUNTRY)
        referral = details \
            .open_tab(ClientDetailsConstantsUI.TAB_CUSTOM_INFORMATION) \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_REFERRAL)

        """ Verify client's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(first_name, ApiCustomerConstantsUI.FNAME) \
            .comparator_string(last_name, ApiCustomerConstantsUI.LNAME) \
            .comparator_string(referral, ApiCustomerConstantsUI.REFFERAL) \
            .comparator_string(country, ApiCustomerConstantsUI.COUNTRY_CRM)

        if email and "*" not in email and "..." not in email:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(email, ApiCustomerConstantsUI.EMAIL)
        elif email and "*" not in email:
            email = email.replace('...', '')
            assert email in ApiCustomerConstantsUI.EMAIL

        if phone and "*" not in phone:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(phone, ApiCustomerConstantsUI.PHONE)
