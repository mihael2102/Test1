from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from time import sleep


class CreateCampaignsPreconditionUI(object):
    driver = None
    config = None
    camp_name = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.camp_name = CRMConstants.CAMPAIGN_NAME

    def create_new_campaign_ui(self):
        """ Login to CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .open_module_ui(TestDataConstants.MODULE_CAMPAIGNS)

        """ Add new campaign """
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[@name='tradeChartFrame']"))
        CampaignsPage(self.driver) \
            .open_add_campaign_module() \
            .add_campaign(
                name=self.camp_name,
                assigned_to=CRMConstants.FIST_ASSIGNED_TO,
                deal=CRMConstants.FIST_DEAL,
                rate=CRMConstants.RATE)
        CampaignsPage(self.driver) \
            .perform_searching_campaign_by_name(self.camp_name)
        sleep(2)
        existing_campaign = CampaignsPage(self.driver) \
            .campaign_exist()

        assert self.camp_name == existing_campaign
