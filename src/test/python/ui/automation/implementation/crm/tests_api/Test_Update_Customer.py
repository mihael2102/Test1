import pytest
from src.test.python.ui.automation.utils.preconditions.api.Api_Preconditions import ApiPrecondition
from src.test.python.ui.automation.BaseTest import *


class UpdateCustomer(BaseTest):

    def test_update_customer(self):
        ApiPrecondition(self.driver, self.config).test_update_customer()
