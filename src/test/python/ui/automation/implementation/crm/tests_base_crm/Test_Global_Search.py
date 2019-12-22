import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.base_crm.BaseCRMPrecondition import BaseCRMPrecondition


@pytest.mark.run(order=35)
class TestGlobalSearch(BaseTest):

    # CRM tests:
    def test_global_search_leads(self):
        BaseCRMPrecondition(self.driver, self.config).global_search_leads()

    def test_global_search_tasks(self):
        BaseCRMPrecondition(self.driver, self.config).global_search_tasks()
