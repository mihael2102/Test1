from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.UserManagementConstants import UserManagementConstants
from time import sleep
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
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)
        user_management = CRMHomePage(self.driver)\
            .select_user_management()
        tab_name = user_management\
            .check_user_management_tab()
        UserManagementPage(self.driver)\
            .open_crm_users_tab()\
            .check_table_loaded()
        assert tab_name == UserManagementConstants.USER_MANAGEMENT_TAB

    def create_user(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)
        CRMHomePage(self.driver)\
            .select_user_management()
        UserManagementPage(self.driver)\
            .open_crm_users_tab()\
            .click_more_icon()\
            .check_delete_btn_exist()\
            .click_new_user_module() \
            .set_user_name(UserInformation.FIRST_USER_NAME) \
            .set_email(UserInformation.FIRST_EMAIL) \
            .set_first_name(UserInformation.FIRST_NAME)
        if global_var.current_brand_name == "brokerz":
            UserManagementPage(self.driver).set_role(UserInformation.ROLE1)
        elif global_var.current_brand_name == "ptbanc" or \
             global_var.current_brand_name == "dax-300" or \
             global_var.current_brand_name == "q8":
            UserManagementPage(self.driver).set_role(UserInformation.ROLE2)
        elif global_var.current_brand_name == "trade99":
            UserManagementPage(self.driver).set_role(UserInformation.ROLE3)
        else:
            UserManagementPage(self.driver).set_role(UserInformation.ROLE)
        UserManagementPage(self.driver)\
            .set_password(UserInformation.PASSWORD) \
            .set_confirm_password(UserInformation.PASSWORD) \
            .set_last_name(UserInformation.LAST_NAME) \
            .click_save_button_user_module() \
            .click_remove_filter_btn()\
            .search_by_username(UserInformation.FIRST_USER_NAME) \
            .check_user_found(UserInformation.FIRST_USER_NAME)

    def delete_user(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)
        CRMHomePage(self.driver)\
            .select_user_management()
        UserManagementPage(self.driver)\
            .open_crm_users_tab() \
            .click_more_icon()\
            .check_delete_btn_exist() \
            .click_remove_filter_btn()\
            .search_by_username(UserInformation.FIRST_USER_NAME) \
            .check_user_found(UserInformation.FIRST_USER_NAME) \
            .click_more_icon()\
            .click_delete_icon() \
            .click_delete_btn() \
            .check_data_not_found()

    def login_as(self):
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)

        ' Go to User Management and make Login As DragonTest user: '
        CRMHomePage(self.driver)\
            .select_user_management()
        UserManagementPage(self.driver) \
            .open_crm_users_tab() \
            .click_remove_filter_btn() \
            .search_by_username(UserInformation.DRAGON_USER_NAME) \
            .check_user_found(UserInformation.DRAGON_USER_NAME) \
            .click_more_icon() \
            .click_login_as_icon()\
            .click_logout_login_as_session(UserInformation.DRAGON_NAME)\
            .verify_current_user_name(UserInformation.PANDA_AUTO_NAME)
