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


class QuesDualixPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def questionnaire_dualix(self):
        """ Personal details form """
        CALoginPage(self.driver) \
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
