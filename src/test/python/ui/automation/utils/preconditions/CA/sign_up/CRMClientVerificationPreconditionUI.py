from src.main.python.ui.ca.model.pages.ca.QuestionnairePage import QuestionnairePage
from src.main.python.ui.ca.model.constants.questionnaire.QuesStrattonConstants import QuesStrattonConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from time import sleep
import poplib
from email import parser
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.constants.EmailConstants import EmailConstants
from src.main.python.ui.crm.model.constants.DragonConstants import DragonConstants
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.ca.model.constants.questionnaire.QuesDualixConstants import QuesDualixConstants
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


class CRMClientVerificationPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def client_exist_in_crm_new_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module and find created client by email """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   CAConstants.EMAIL_CA)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Get client's data """
        details = ClientDetailsPageUI(self.driver)

        first_name = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_FNAME)
        last_name = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_LNAME)
        phone = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_PHONE)
        birthday = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_BIRTHDAY)
        address = details \
            .open_tab(ClientDetailsConstantsUI.TAB_ADDRESS_INFORMATION) \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_ADDRESS)
        postal_code = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_CODE)
        city = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_CITY)
        country = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_COUNTRY)
        currency = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_BASE_CURRENCY)

        """ Verify client's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(
                first_name,
                self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]) \
            .comparator_string(
                last_name,
                self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_LAST_NAME]) \
            .comparator_string(birthday, CAConstants.BIRTHDAY_CRM) \
            .comparator_string(currency, var.get_var(self.__class__.__name__)["signup_currency"]) \
            .comparator_string(address, CAConstants.ADDRESS) \
            .comparator_string(postal_code, CAConstants.ZIP_CODE) \
            .comparator_string(city, CAConstants.CITY) \
            .comparator_string(country, CAConstants.COUNTRY_DEFAULT)

        if "*" not in phone:
            assert self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.PHONE] in phone
