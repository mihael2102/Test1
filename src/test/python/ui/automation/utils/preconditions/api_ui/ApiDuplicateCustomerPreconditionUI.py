from src.test.python.ui.automation.utils.preconditions.api_ui.ApiAutorizationPreconditionUI import \
    ApiAutorizationPreconditionUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants.APIConstants import APIConstants
from src.main.python.ui.crm.model.constants_ui.api_ui.ApiCreateCustomerConstantsUI import ApiCreateCustomerConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from time import sleep


class ApiDuplicateCustomerPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def duplicate_customer_ui(self):
        """ Autorization """
        ApiAutorizationPreconditionUI(self.driver, self.config)\
            .autorization_ui()

        """ Create Customer with same email"""
        check_create_customer_token = ApiPage(self.driver)\
            .create_customer_module() \
            .enter_email(ApiCreateCustomerConstantsUI.EMAIL) \
            .enter_password(ApiCreateCustomerConstantsUI.PASSWORD) \
            .enter_country(ApiCreateCustomerConstantsUI.COUNTRY) \
            .enter_firstName(ApiCreateCustomerConstantsUI.FNAME) \
            .enter_lastName(ApiCreateCustomerConstantsUI.LNAME) \
            .enter_phone(ApiCreateCustomerConstantsUI.PHONE) \
            .enter_refferal(ApiCreateCustomerConstantsUI.REFFERAL) \
            .send_create_customer() \
            .check_create_customer_token()

        assert ApiCreateCustomerConstantsUI.STATUS_DUPLICATE_CUSTOMER in check_create_customer_token
