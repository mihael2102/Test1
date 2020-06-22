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


class CampaignsSearchingColumnsPreconditionUI(object):
    driver = None
    config = None
    camp_name = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.camp_name = CRMConstants.CAMPAIGN_NAME

    def searching_by_columns_ui(self):
        """ Login to CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
            url=self.config.get_value('url'),
            user_name=self.config.get_value(TestDataConstants.USER_NAME),
            password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
            otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .open_module_ui(TestDataConstants.MODULE_CAMPAIGNS)

        """ Edit campaign """
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[@name='tradeChartFrame']"))

        """ Get data from list view """
        campaign_id = CampaignsPage(self.driver).get_campaign_id_list_view()
        campaign_name = CampaignsPage(self.driver).get_campaign_name_list_view()
        cpa = CampaignsPage(self.driver).get_cpa_list_view()

        """ Searching by Campaign ID """
        CampaignsPage(self.driver) \
            .set_campaign_id(campaign_id) \
            .campaign_data_checker(campaign_id) \
            .clear_filter()

        """ Searching by Campaign Name """
        CampaignsPage(self.driver) \
            .set_campaign_name(campaign_name) \
            .campaign_data_checker(campaign_name) \
            .clear_filter()

        """ Searching by CPA """
        CampaignsPage(self.driver) \
            .set_cpa(cpa) \
            .campaign_data_checker(cpa) \
            .clear_filter() \
            .refresh_page()

        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[@name='tradeChartFrame']"))
        CampaignsPage(self.driver) \
            .perform_searching_campaign_by_columns(
                campaign_name,
                campaign_id,
                cpa) \
            .refresh_filter() \
            .campaign_data_checker(campaign_id) \
            .campaign_data_checker(campaign_name) \
            .campaign_data_checker(cpa)
