import pytest
from src.test.python.ui.automation.utils.preconditions.api.Api_Preconditions import ApiPrecondition
from src.test.python.ui.automation.BaseTest import *

class RefferalField(BaseTest):

    def test_refferal_field(self):
        ApiPrecondition(self.driver, self.config).test_refferal_field()