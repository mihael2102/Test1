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


class ApiReadCustomerPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def read_customer_ui(self):
        """ Autorization """
        ApiAutorizationPreconditionUI(self.driver, self.config)\
            .autorization_ui()

        """ Read Customer """
        token = ApiPage(self.driver)\
            .read_customer_module() \
            .enter_email_for_read_customer(ApiCreateCustomerConstantsUI.EMAIL) \
            .send_read_customer() \
            .check_read_customer_details()
        count = 0
        while (self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                   LeadsModuleConstants.EMAIL1] not in token):
            time.sleep(2)
            token = ApiPage(self.driver).check_read_customer_details()
            count += 1
            if count == 5:
                break
        assert self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                   LeadsModuleConstants.EMAIL1] in token
        assert APIConstants.REFFERAL in token
        assert APIConstants.COUNTRY2 in token
        assert APIConstants.LASTNAME in token
        assert self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                   LeadsModuleConstants.FIRST_NAME] in token
