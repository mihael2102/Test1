from src.main.python.ui.crm.model.constants.AutoAssignConstants import AutoAssignConstants
from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.pages.auto_assign.AutoAssignPage import AutoAssignPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.auto_assign.AutoAssignPrecondition import AutoAssignPrecondition
from src.test.python.ui.automation.utils.preconditions.campaigns.CampaignsPrecondition import CampaignsPrecondition


class AutoAssignTest(BaseTest):

    def test_perform_add_rule(self):
        CampaignsPrecondition().perform_create_new_campaigns()
        AutoAssignPrecondition().perform_add_rule(CampaignsConstants.CAMPAIGN_NAME)
        auto_assign_module = AutoAssignPage()
        assert auto_assign_module.get_successfull_message() == AutoAssignConstants().SUCCESSFUL_MESSAGE
        auto_assign_module.click_ok()
