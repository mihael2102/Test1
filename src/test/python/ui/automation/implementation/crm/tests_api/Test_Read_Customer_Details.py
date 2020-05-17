import pytest
from src.test.python.ui.automation.utils.preconditions.api.Api_Preconditions import ApiPrecondition
from src.test.python.ui.automation.BaseTest import *


class ReadCustomerDetails(BaseTest):

    def test_read_customer_details(self):
        ApiPrecondition(self.driver, self.config).test_read_customer_details()