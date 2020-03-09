import pytest
from src.test.python.ui.automation.utils.preconditions.api_ui.ApiAutorizationPreconditionUI import \
    ApiAutorizationPreconditionUI
from src.test.python.ui.automation.utils.preconditions.api_ui.ApiDuplicateCustomerPreconditionUI import \
    ApiDuplicateCustomerPreconditionUI
from src.test.python.ui.automation.utils.preconditions.api_ui.ApiReadCustomerPreconditionUI import \
    ApiReadCustomerPreconditionUI
from src.test.python.ui.automation.utils.preconditions.api_ui.ApiCreateCustomerPreconditionUI import \
    ApiCreateCustomerPreconditionUI
from src.test.python.ui.automation.utils.preconditions.api.Api_Preconditions import ApiPrecondition
from src.test.python.ui.automation.BaseTest import *


class TestApiUI(BaseTest):

    def test_autorization_ui(self):
        ApiAutorizationPreconditionUI(self.driver, self.config).autorization_ui()

    def test_create_customer_ui(self):
        ApiCreateCustomerPreconditionUI(self.driver, self.config).create_customer_ui()

    def test_duplicate_customer_ui(self):
        ApiDuplicateCustomerPreconditionUI(self.driver, self.config).duplicate_customer_ui()

    def test_read_customer_ui(self):
        ApiReadCustomerPreconditionUI(self.driver, self.config).read_customer_ui()

    def test_update_customer(self):
        ApiPrecondition(self.driver, self.config).test_update_customer()

    def test_create_lead_api(self):
        ApiPrecondition(self.driver, self.config).test_create_lead()

    def test_read_leads_api(self):
        ApiPrecondition(self.driver, self.config).test_read_leads()

    def test_login_token(self):
        ApiPrecondition(self.driver, self.config).login_token()

    def test_autoassign_create_new_customer(self):
        ApiPrecondition(self.driver, self.config).autoassign_create_new_customer()

    def test_autoassign_create_new_lead(self):
        ApiPrecondition(self.driver, self.config).autoassign_create_lead()
