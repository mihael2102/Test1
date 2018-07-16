import random

from src.main.python.ui.crm.model.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class CreateUserTest(BaseTest):

    def test_create_user(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD))

        user_management_module = CRMHomePage().open_user_management_module("User Management")
        new_user_profile = user_management_module.click_new_user_module() \
            .perform_create_user("User_QA",
                                 "testing+%s@pandats.com" % str(random.randrange(1, 999)),
                                 "Panda",
                                 "CEO VP",
                                 "Testinqa",
                                 "Testinqa",
                                 "UA")
        new_user_profile.click_save_button_user_module()
