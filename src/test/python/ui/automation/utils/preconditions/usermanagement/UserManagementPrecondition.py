from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.UserManagementConstants import UserManagementConstants
from src.main.python.ui.crm.model.pages.usermanagement.UserManagementPage import UserManagementPage
from time import sleep
from src.main.python.ui.crm.model.constants.UserInformation import UserInformation


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
        assert UserManagementConstants.EMAIL in email or UserManagementConstants.EMAIL_NET in email or \
               UserManagementConstants.EMAIL_CO in email

    def create_delete_user(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)
        CRMHomePage(self.driver)\
            .select_user_management()
        UserManagementPage(self.driver)\
            .click_new_user_module() \
            .set_user_name(UserInformation.FIRST_USER_NAME) \
            .set_email(UserInformation.FIRST_EMAIL) \
            .set_first_name(UserInformation.FIRST_NAME)
        if global_var.current_brand_name == "gmo" or global_var.current_brand_name == "itrader":
            UserManagementPage(self.driver)\
                .set_role(UserInformation.ROLE)
        else:
            UserManagementPage(self.driver)\
                .set_role(UserInformation.ROLE1)
        UserManagementPage(self.driver)\
            .set_password(UserInformation.PASSWORD) \
            .set_confirm_password(UserInformation.PASSWORD) \
            .set_last_name(UserInformation.LAST_NAME)\
            .click_save_button_user_module()\
            .search_by_username(UserInformation.FIRST_USER_NAME)\
            .click_delete_icon()\
            .click_delete_btn()\
            .check_data_not_found(UserInformation.FIRST_USER_NAME)
