from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliatePage import AffiliatePage
from src.main.python.ui.crm.model.constants.LeaderboardConstants import LeaderboardConstants
from src.main.python.ui.crm.model.constants.UserManagementConstants import UserManagementConstants

class UserManagementPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def check_user_management(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        user_management = CRMHomePage(self.driver).select_user_management()
        tab_name = user_management.check_user_management_tab()
        email = user_management.check_table_loaded()
        assert tab_name == UserManagementConstants.USER_MANAGEMENT_TAB
        assert UserManagementConstants.EMAIL in email



