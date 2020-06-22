from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.modules.campaigns_module.AddCampaignsModule import AddCampaignsModule
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from time import sleep


class DeleteCampaignsPreconditionUI(object):
    driver = None
    config = None
    camp_name = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.camp_name = CRMConstants.CAMPAIGN_NAME

    def delete_campaign_ui(self):
        """ Login to CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .open_module_ui(TestDataConstants.MODULE_CAMPAIGNS)

        """ Delete campaign """
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[@name='tradeChartFrame']"))
        CampaignsPage(self.driver) \
            .perform_searching_campaign_by_name(self.camp_name)
        sleep(2)
        CampaignsPage(self.driver) \
            .click_delete_campaign()
        sleep(2)
        CampaignsPage(self.driver) \
            .deleting_confirmation()
        sleep(1)
        CampaignsPage(self.driver) \
            .perform_searching_campaign_by_name(self.camp_name)
        sleep(1)
        CampaignsPage(self.driver) \
            .check_campaign_deleted()
