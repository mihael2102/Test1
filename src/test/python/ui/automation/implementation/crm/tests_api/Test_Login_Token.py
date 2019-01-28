import pytest
from src.test.python.ui.automation.utils.preconditions.api.Api_Preconditions import ApiPrecondition
from src.test.python.ui.automation.BaseTest import *

class LoginToken(BaseTest):

    def test_login_token(self):
        ApiPrecondition(self.driver, self.config).login_token()