import pytest
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.usermanagement.UserManagementPage import UserManagementPage
from src.main.python.ui.crm.model.constants.UserInformation import UserInformation
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


@pytest.mark.run(order=13)
class CreateUserPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_user_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open User Management module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_UM)

        """ Create user """
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[contains(@src,'UserManagement')]"))
        UserManagementPage(self.driver) \
            .open_crm_users_tab() \
            .click_new_user_module() \
            .set_user_name(UserInformation.FIRST_USER_NAME) \
            .set_email(UserInformation.FIRST_EMAIL) \
            .set_first_name(UserInformation.FIRST_NAME) \
            .set_role(var.get_var(self.__class__.__name__)["role"])
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[contains(@src,'UserManagement')]"))
        UserManagementPage(self.driver) \
            .set_password(UserInformation.PASSWORD) \
            .set_confirm_password(UserInformation.PASSWORD) \
            .set_last_name(UserInformation.LAST_NAME) \
            .click_save_button_user_module() \
            .click_remove_filter_btn() \
            .search_by_username(UserInformation.FIRST_USER_NAME) \
            .check_user_found(UserInformation.FIRST_USER_NAME)
