import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.crm_config_ui.CrmConfigPagesPreconditionUI import \
    CrmConfigPagesPreconditionUI


@pytest.mark.run(order=3)
class TestCrmConfigurationUI(BaseTest):

    def test_crm_config_pages_ui(self):
        CrmConfigPagesPreconditionUI(self.driver, self.config).crm_config_pages_ui()
