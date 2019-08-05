from src.main.python.ui.crm.model.constants.UserInformation import UserInformation
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.utils.preconditions.usermanagement.UserManagementPrecondition import \
    UserManagementPrecondition


class UserManagementTest(BaseTest):

    def test_create_user(self):
        UserManagementPrecondition(self.driver, self.config).create_user()

    def test_delete_user(self):
        UserManagementPrecondition(self.driver, self.config).delete_user()
