import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.load_crm_ui.LoadSwitchTabsPreconditionUI import \
    LoadSwitchTabsPreconditionUI


@pytest.mark.run(order=3)
class TestLoadCRMUI(BaseTest):

    def test_load_switch_tabs_ui(self):
        LoadSwitchTabsPreconditionUI(self.driver, self.config).load_switch_tabs_ui()
