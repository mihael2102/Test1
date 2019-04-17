from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from time import sleep
from src.main.python.ui.crm.model.pages.chat_page.ChatPage import ChatPage

class Chat_Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def chat_vtiger_test(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
                      .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                 self.config.get_value(TestDataConstants.CRM_PASSWORD),
                                 self.config.get_value(TestDataConstants.OTP_SECRET)) \
                      .open_client_module_clients_module()
        sleep(5)
        ChatPage(self.driver).click_chat_icon()
