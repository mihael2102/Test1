import pytest
from src.test.python.ui.automation.utils.preconditions.api.Api_Preconditions import ApiPrecondition
from src.test.python.ui.automation.BaseTest import *

class CreateNewCustomer(BaseTest):

    def test_create_new_customer(self):
        ApiPrecondition(self.driver, self.config).test_create_new_customer()

    def test_create_new_lead(self):
        ApiPrecondition(self.driver, self.config).test_create_lead()