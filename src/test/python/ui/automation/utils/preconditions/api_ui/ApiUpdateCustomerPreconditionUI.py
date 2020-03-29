from src.test.python.ui.automation.utils.preconditions.api_ui.ApiAutorizationPreconditionUI import \
    ApiAutorizationPreconditionUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants.APIConstants import APIConstants
from src.main.python.ui.crm.model.constants_ui.api_ui.ApiCustomerConstantsUI import ApiCustomerConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from time import sleep


class ApiUpdateCustomerPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def update_customer_ui(self):
        """ Autorization """
        ApiAutorizationPreconditionUI(self.driver, self.config)\
            .autorization_ui()

        """ Update Customer """
        token = ApiPage(self.driver) \
            .update_customer_module() \
            .enter_email_for_update(ApiCustomerConstantsUI.EMAIL) \
            .change_postalCode(ApiCustomerConstantsUI.CHANGE_POSTAL_CODE) \
            .change_address(ApiCustomerConstantsUI.CHANGE_ADDRESS) \
            .change_city(ApiCustomerConstantsUI.CHANGE_CITY) \
            .send_update_customer() \
            .check_update_token()

        assert ApiCustomerConstantsUI.STATUS_OK in token

        """ CRM: get client's data """
        CRMLoginPageUI(self.driver) \
            .switch_first_tab_page()
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   ApiCustomerConstantsUI.EMAIL)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        details = ClientDetailsPageUI(self.driver)
        email = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_EMAIL)
        city = details \
            .open_tab(ClientDetailsConstantsUI.TAB_ADDRESS_INFORMATION) \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_CITY)
        address = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_ADDRESS)
        code = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_CODE)

        """ Verify client's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(city, ApiCustomerConstantsUI.CHANGE_CITY) \
            .comparator_string(address, ApiCustomerConstantsUI.CHANGE_ADDRESS) \
            .comparator_string(code, ApiCustomerConstantsUI.CHANGE_POSTAL_CODE)
