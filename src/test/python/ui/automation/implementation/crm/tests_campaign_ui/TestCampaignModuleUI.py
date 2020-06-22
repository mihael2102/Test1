import pytest
from src.test.python.ui.automation.utils.preconditions.campaign_ui.CreateCampaignsPreconditionUI import \
    CreateCampaignsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.campaign_ui.EditCampaignsPreconditionUI import \
    EditCampaignsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.campaign_ui.DeleteCampaignsPreconditionUI import \
    DeleteCampaignsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.campaign_ui.CampaignsSearchingColumnsPreconditionUI import \
    CampaignsSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *


@pytest.mark.run(order=35)
class TestCampaignModuleUI(BaseTest):

    def test_create_campaign_ui(self):
        CreateCampaignsPreconditionUI(self.driver, self.config).create_new_campaign_ui()

    def test_edit_campaign_ui(self):
        EditCampaignsPreconditionUI(self.driver, self.config).edit_campaign_ui()

    def test_delete_campaign_ui(self):
        DeleteCampaignsPreconditionUI(self.driver, self.config).delete_campaign_ui()

    def test_campaign_searching_by_columns_ui(self):
        CampaignsSearchingColumnsPreconditionUI(self.driver, self.config).searching_by_columns_ui()
