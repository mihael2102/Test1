import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.user_management_ui.CreateUserPreconditionUI import \
    CreateUserPreconditionUI


@pytest.mark.run(order=3)
class TestUserManagementUI(BaseTest):

    def test_create_user_ui(self):
        CreateUserPreconditionUI(self.driver, self.config).create_user_ui()
