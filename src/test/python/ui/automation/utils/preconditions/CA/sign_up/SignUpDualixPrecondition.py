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


class SignUpDualixPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def sign_up_dualix(self):
        """ Registration form """
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .close_campaign_banner() \
            .click_sign_up() \
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)
                             [LeadsModuleConstants.FIRST_NAME]) \
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)
                            [LeadsModuleConstants.FIRST_LAST_NAME]) \
            .fill_email(CAConstants.EMAIL_CA) \
            .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.PHONE]) \
            .fill_password(CAConstants.PASSWORD) \
            .fill_confirm_password(CAConstants.PASSWORD) \
            .check_box_accept() \
            .risk_check_box_accept() \
            .select_country_first_step(CAConstants.COUNTRY1) \
            .click_submit() \
            .close_payment_popup()

        """ Check graphs """
        WebTraderPage(self.driver) \
            .open_trading_page() \
            .check_chart_loaded()

        """ Personal details form """
        CALoginPage(self.driver) \
            .verify() \
            .click_hi_guest() \
            .click_transactions_history() \
            .select_data_birth_day(CAConstants.DAY_BIRTH) \
            .select_data_birth_month(CAConstants.MONTH_BIRTH) \
            .select_data_birth_year(CAConstants.YEAR_BIRTH) \
            .choose_currency(CAConstants.CURRENCY) \
            .choose_citizenship(CAConstants.CITIZENSHIP3) \
            .fill_city(CAConstants.CITY) \
            .fill_zip_code(CAConstants.ZIP_CODE) \
            .fill_address(CAConstants.ADDRESS) \
            .click_next() \
            .enter_ssn_tin(QuesStrattonConstants.SSN_TIN) \
            .enter_id(QuesStrattonConstants.NAT_ID) \
            .select_country_tax(QuesStrattonConstants.COUNTRY_TAX) \
            .enter_company_name(QuesStrattonConstants.COMPANY_NAME) \
            .select_us_reportable(CAConstants.US_REPORTABLE_NO) \
            .click_save_changes_btn()
        QuestionnairePage(self.driver) \
            .select_item_pick_list(QuesDualixConstants.LIST_1, QuesDualixConstants.ITEM_1) \
            .select_item_pick_list(QuesDualixConstants.LIST_2, QuesDualixConstants.ITEM_2) \
            .select_item_pick_list(QuesDualixConstants.LIST_3, QuesDualixConstants.ITEM_3) \
            .select_item_pick_list(QuesDualixConstants.LIST_4, QuesDualixConstants.ITEM_4) \
            .select_item_pick_list(QuesDualixConstants.LIST_5, QuesDualixConstants.ITEM_5) \
            .select_item_pick_list(QuesDualixConstants.LIST_6, QuesDualixConstants.ITEM_6) \
            .click_next_btn() \
            .select_item_pick_list(QuesDualixConstants.LIST_7, QuesDualixConstants.ITEM_7) \
            .select_item_pick_list(QuesDualixConstants.LIST_8, QuesDualixConstants.ITEM_8) \
            .select_item_pick_list(QuesDualixConstants.LIST_9, QuesDualixConstants.ITEM_9) \
            .select_item_pick_list(QuesDualixConstants.LIST_10, QuesDualixConstants.ITEM_10) \
            .select_item_pick_list(QuesDualixConstants.LIST_11, QuesDualixConstants.ITEM_11) \
            .select_item_pick_list(QuesDualixConstants.LIST_12, QuesDualixConstants.ITEM_12) \
            .select_item_pick_list(QuesDualixConstants.LIST_13, QuesDualixConstants.ITEM_13) \
            .select_item_pick_list(QuesDualixConstants.LIST_14, QuesDualixConstants.ITEM_14) \
            .select_item_pick_list(QuesDualixConstants.LIST_15, QuesDualixConstants.ITEM_15) \
            .select_item_pick_list(QuesDualixConstants.LIST_16, QuesDualixConstants.ITEM_16) \
            .select_item_pick_list(QuesDualixConstants.LIST_17, QuesDualixConstants.ITEM_17) \
            .select_item_pick_list(QuesDualixConstants.LIST_18, QuesDualixConstants.ITEM_18) \
            .select_item_pick_list(QuesDualixConstants.LIST_19, QuesDualixConstants.ITEM_19) \
            .select_item_pick_list(QuesDualixConstants.LIST_20, QuesDualixConstants.ITEM_20) \
            .select_item_pick_list(QuesDualixConstants.LIST_21, QuesDualixConstants.ITEM_21) \
            .select_item_pick_list(QuesDualixConstants.LIST_22, QuesDualixConstants.ITEM_22) \
            .select_item_pick_list(QuesDualixConstants.LIST_23, QuesDualixConstants.ITEM_23) \
            .click_next_btn() \
            .close_questionnaire_message()

        sleep(2)
        existing_client = CALoginPage(self.driver).verify_client(self.load_lead_from_config(
                                                    TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME])
        expected_client = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]

        assert existing_client.lower() == expected_client.lower()
