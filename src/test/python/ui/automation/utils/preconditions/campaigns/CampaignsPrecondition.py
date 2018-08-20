from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config


class CampaignsPrecondition(object):
    def __init__(self) -> None:
        super().__init__()

    def perform_create_new_campaigns(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage().open_more_list_modules() \
            .select_campaigns_module_more_list(CampaignsConstants.MODULE) \
            .open_add_campaign_module() \
            .perform_add_new_campaign(CampaignsConstants.CAMPAIGN_NAME,
                                      Config.data.get_data_campaign_module(CampaignsConstants.FIST_ASSIGNED_TO),
                                      CampaignsConstants.FIRST_START_DATE.strftime(CampaignsConstants.FORMAT_DATE),
                                      CampaignsConstants.FIRST_END_DATE.strftime(CampaignsConstants.FORMAT_DATE),
                                      Config.data.get_data_campaign_module(CampaignsConstants.FIST_DEAL),
                                      CampaignsConstants.RATE)

        return CampaignsPrecondition()

    def perform_create_second_campaigns(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage().open_more_list_modules() \
            .select_campaigns_module_more_list(CampaignsConstants.MODULE) \
            .open_add_campaign_module() \
            .perform_add_new_campaign(CampaignsConstants.CAMPAIGN_NAME,
                                      Config.data.get_data_campaign_module(CampaignsConstants.FIST_ASSIGNED_TO),
                                      CampaignsConstants.FIRST_START_DATE.strftime(CampaignsConstants.FORMAT_DATE),
                                      CampaignsConstants.FIRST_END_DATE.strftime(CampaignsConstants.FORMAT_DATE),
                                      Config.data.get_data_campaign_module(CampaignsConstants.FIST_DEAL),
                                      CampaignsConstants.RATE)

        return CampaignsPrecondition()



