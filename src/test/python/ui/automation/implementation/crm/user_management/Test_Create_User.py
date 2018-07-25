from src.main.python.ui.crm.model.constants.UserInformation import UserInformation
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


class CreateUserTest(BaseTest):

    def test_create_user(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        user_management_module = CRMHomePage().open_user_management_module(UserInformation.USER_MANAGEMENT)
        new_user_profile = user_management_module.click_new_user_module() \
            .perform_create_user(UserInformation.FIRST_USER_NAME, UserInformation.FIRST_EMAIL,
                                 Config.data.get_data_user_info(UserInformation.FIRST_USER, UserInformation.FIRST_NAME),
                                 Config.data.get_data_user_info(UserInformation.FIRST_USER, UserInformation.FIRST_ROLE),
                                 Config.data.get_data_user_info(UserInformation.FIRST_USER,
                                                                UserInformation.FIRST_PASSWORD),
                                 Config.data.get_data_user_info(UserInformation.FIRST_USER,
                                                                UserInformation.FIRST_CONFIRM_PASSWORD),
                                 Config.data.get_data_user_info(UserInformation.FIRST_USER,
                                                                UserInformation.FIRST_LAST_NAME))
        new_user_profile.click_save_button_user_module()
