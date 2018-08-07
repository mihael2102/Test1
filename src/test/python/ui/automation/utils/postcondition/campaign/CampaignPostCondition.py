from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.main.python.utils.logs.Loging import Logging


class CampaignPostCondition(object):

    def __init__(self) -> None:
        super().__init__()

    def delete_campaign_by_pencil(self, campaign_name):
        confirm_text = CampaignsPage().perform_searching_campaign_by_name(campaign_name) \
            .click_delete_campaign() \
            .get_message()

        Logging().reportDebugStep(self, "The campaign_name was deleted: " + campaign_name)
        return confirm_text
