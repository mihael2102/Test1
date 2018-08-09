from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.campaigns.CampaignsPrecondition import CampaignsPrecondition


class CampaignsModuleTest(BaseTest):

    def test_create_campaigns_module(self):
        CampaignsPrecondition().perform_create_new_campaigns()

        campaign_view = CampaignsPage().perform_searching_campaign_by_name(CampaignsConstants.CAMPAIGN_NAME) \
            .open_campaign_view(CampaignsConstants.CAMPAIGN_NAME)

        assert campaign_view.get_name_text(CampaignsConstants.CAMPAIGN_NAME)
        assert campaign_view.get_assigned_to_text() == Config.data.get_data_campaign_module(
            CampaignsConstants.FIST_ASSIGNED_TO)
        assert campaign_view.get_start_date_text(CampaignsConstants.FIRST_START_DATE.strftime(
            CampaignsConstants.FORMAT_DATE))
        assert campaign_view.get_end_date_text(
            CampaignsConstants.FIRST_END_DATE.strftime(CampaignsConstants.FORMAT_DATE))
        assert campaign_view.get_deal_text(Config.data.get_data_campaign_module(CampaignsConstants.FIST_DEAL))
        assert campaign_view.get_rate_text(CampaignsConstants.RATE)

    def test_edit_campaigns_module(self):
        CampaignsPrecondition().perform_create_new_campaigns()

        CampaignsPage().perform_searching_campaign_by_name(CampaignsConstants.CAMPAIGN_NAME) \
            .open_campaign_view(CampaignsConstants.CAMPAIGN_NAME) \
            .perform_edit_campaign(CampaignsConstants.CAMPAIGN_NAME,
                                   Config.data.get_data_campaign_module(CampaignsConstants.SECOND_ASSIGNED_TO),
                                   CampaignsConstants.FIRST_START_DATE.strftime(CampaignsConstants.FORMAT_DATE),
                                   CampaignsConstants.FIRST_END_DATE.strftime(CampaignsConstants.FORMAT_DATE),
                                   Config.data.get_data_campaign_module(CampaignsConstants.SECOND_DEAL),
                                   CampaignsConstants.RATE)

        campaign_view = CampaignsPage().perform_searching_campaign_by_name(CampaignsConstants.CAMPAIGN_NAME) \
            .open_campaign_view(CampaignsConstants.CAMPAIGN_NAME)

        assert campaign_view.get_name_text(CampaignsConstants.CAMPAIGN_NAME)
        assert campaign_view.get_assigned_to_text() == Config.data.get_data_campaign_module(
            CampaignsConstants.SECOND_ASSIGNED_TO)
        assert campaign_view.get_start_date_text(CampaignsConstants.FIRST_START_DATE.strftime(
            CampaignsConstants.FORMAT_DATE))
        assert campaign_view.get_end_date_text(
            CampaignsConstants.FIRST_END_DATE.strftime(CampaignsConstants.FORMAT_DATE))
        assert campaign_view.get_deal_text(Config.data.get_data_campaign_module(CampaignsConstants.SECOND_DEAL))
        assert campaign_view.get_rate_text(CampaignsConstants.RATE)

    def test_searching_columns(self):
        CampaignsPrecondition().perform_create_new_campaigns()

        campaign_view = CampaignsPage().perform_searching_campaign_by_columns(
            CampaignsConstants.CAMPAIGN_NAME, Config.data.get_data_campaign_module(CampaignsConstants.FIRST_ACTIVITY),
            CampaignsConstants.FIRST_START_DATE.strftime(CampaignsConstants.FORMAT_DATE), CampaignsConstants.RATE) \
            .open_campaign_view(CampaignsConstants.CAMPAIGN_NAME)

        assert campaign_view.get_name_text(CampaignsConstants.CAMPAIGN_NAME)
        assert campaign_view.get_assigned_to_text() == Config.data.get_data_campaign_module(
            CampaignsConstants.FIST_ASSIGNED_TO)
        assert campaign_view.get_start_date_text(CampaignsConstants.FIRST_START_DATE.strftime(
            CampaignsConstants.FORMAT_DATE))
        assert campaign_view.get_end_date_text(
            CampaignsConstants.FIRST_END_DATE.strftime(CampaignsConstants.FORMAT_DATE))
        assert campaign_view.get_deal_text(Config.data.get_data_campaign_module(CampaignsConstants.FIST_DEAL))
        assert campaign_view.get_rate_text(CampaignsConstants.RATE)
