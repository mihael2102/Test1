import pytest
from src.test.python.ui.automation.utils.preconditions.api.Api_Preconditions import ApiPrecondition
from src.test.python.ui.automation.BaseTest import *


class CreateLead(BaseTest):

    def test_create_lead_api(self):
        ApiPrecondition(self.driver, self.config).test_create_lead()