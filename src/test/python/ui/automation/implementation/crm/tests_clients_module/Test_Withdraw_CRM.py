import pytest

from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.withdraw_crm.WithdrawPreconditionCRM import WithdrawPreconditionCRM


@pytest.mark.run(order=35)
class WithdrawTest(BaseTest):

    def test_withdraw_crm(self):
        WithdrawPreconditionCRM(self.driver, self.config).create_withdraw()

    def test_withdraw_crm_new_ui(self):
        WithdrawPreconditionCRM(self.driver, self.config).create_withdraw_new_ui()
