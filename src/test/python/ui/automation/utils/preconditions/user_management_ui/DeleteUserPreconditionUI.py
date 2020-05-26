import pytest
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.usermanagement.UserManagementPage import UserManagementPage
from src.main.python.ui.crm.model.constants.UserInformation import UserInformation


@pytest.mark.run(order=13)
class DeleteUserPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def delete_user_ui(self):
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

        """ Delete user """
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[contains(@src,'UserManagement')]"))
        UserManagementPage(self.driver) \
            .open_crm_users_tab() \
            .click_more_icon() \
            .check_delete_btn_exist() \
            .click_remove_filter_btn() \
            .search_by_username(UserInformation.FIRST_USER_NAME) \
            .check_user_found(UserInformation.FIRST_USER_NAME) \
            .click_more_icon() \
            .click_delete_icon() \
            .click_delete_btn() \
            .check_data_not_found()
