import pytest
from src.test.python.ui.automation.utils.preconditions.campaign_ui.CreateCampaignsPreconditionUI import \
    CreateCampaignsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.campaigns.CampaignsPrecondition import CampaignsPrecondition


@pytest.mark.run(order=35)
class TestCampaignModuleUI(BaseTest):

    def test_create_campaign_ui(self):
        CreateCampaignsPreconditionUI(self.driver, self.config).create_new_campaign_ui()

    def test_edit_campaign(self):
        CampaignsPrecondition(self.driver, self.config).edit_campaign()

    def test_delete_campaign(self):
        CampaignsPrecondition(self.driver, self.config).delete_campaign()

    def test_campaign_searching_by_columns(self):
        CampaignsPrecondition(self.driver, self.config).searching_by_columns()
