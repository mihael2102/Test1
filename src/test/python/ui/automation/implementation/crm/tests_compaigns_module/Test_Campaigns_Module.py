import pytest

from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.campaigns.CampaignsPrecondition import CampaignsPrecondition


@pytest.mark.run(order=35)
class CampaignsModuleTest(BaseTest):

    def test_create_campaign(self):
        # camp_name, existing_campaign =
        CampaignsPrecondition(self.driver, self.config).create_new_campaign()
        # self.assertEqual(camp_name, existing_campaign, "Not equal")\

    def test_edit_campaign(self):
        CampaignsPrecondition(self.driver, self.config).edit_campaign()

    def test_delete_campaign(self):
        CampaignsPrecondition(self.driver, self.config).delete_campaign()

    def test_campaign_searching_by_columns(self):
        CampaignsPrecondition(self.driver, self.config).searching_by_columns()
