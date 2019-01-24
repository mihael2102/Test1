import pytest
from src.test.python.ui.automation.utils.preconditions.api.Api_Preconditions import ApiPrecondition
from src.test.python.ui.automation.BaseTest import *

class RefferalField(BaseTest):

    def test_create_new_customer(self):
        ApiPrecondition(self.driver, self.config).test_refferal_field()