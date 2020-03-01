from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.modules.campaigns_module.AddCampaignsModule import AddCampaignsModule
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from time import sleep


class CampaignsPrecondition(object):
    driver = None
    config = None
    camp_name = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.camp_name = CRMConstants.CAMPAIGN_NAME

    def create_new_campaign(self):
        """ Login to CRM """
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Campaigns page """
        CRMHomePage(self.driver)\
            .open_more_list_modules()\
            .select_campaigns_module_more_list(CampaignsConstants.MODULE) \
            .open_add_campaign_module()

        """ Add new campaign """
        AddCampaignsModule(self.driver)\
            .perform_add_new_campaign(
                self.camp_name,
                CRMConstants.FIST_ASSIGNED_TO,
                CRMConstants.FIST_DEAL,
                CRMConstants.RATE)
        CampaignsPage(self.driver)\
            .perform_searching_campaign_by_name(self.camp_name)
        sleep(2)
        existing_campaign = CampaignsPage(self.driver)\
            .campaign_exist()

        assert self.camp_name == existing_campaign
        sleep(2)

    """edit campaign"""
    def edit_campaign(self):
        """ Login to CRM """
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Campaign page """
        CRMHomePage(self.driver)\
            .open_more_list_modules() \
            .select_campaigns_module_more_list(CampaignsConstants.MODULE)
        CampaignsPage(self.driver)\
            .perform_searching_campaign_by_name(self.camp_name)
        sleep(2)
        CampaignsPage(self.driver)\
            .open_campaign_view(self.camp_name)
        sleep(2)
        AddCampaignsModule(self.driver)\
            .set_deal(CRMConstants.SECOND_DEAL)
        AddCampaignsModule(self.driver)\
            .set_rate(CRMConstants.RATE1)
        sleep(2)
        AddCampaignsModule(self.driver)\
            .click_save_button()
        sleep(2)
        CampaignsPage(self.driver)\
            .open_campaign_view(self.camp_name)
        sleep(2)
        actual_deal = CampaignsPage(self.driver)\
            .get_deal()
        assert actual_deal == CRMConstants.SECOND_DEAL
        sleep(2)
        assert CampaignsPage(self.driver).get_rate() == CRMConstants.RATE1

    """delete campaign"""
    def delete_campaign(self):
        """ Login to CRM """
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Campaign page """
        CRMHomePage(self.driver)\
            .open_more_list_modules() \
            .select_campaigns_module_more_list(CampaignsConstants.MODULE)
        CampaignsPage(self.driver)\
            .perform_searching_campaign_by_name(self.camp_name)
        sleep(2)
        CampaignsPage(self.driver)\
            .click_delete_campaign()
        sleep(2)
        CampaignsPage(self.driver)\
            .deleting_confirmation()
        sleep(1)
        CampaignsPage(self.driver)\
            .perform_searching_campaign_by_name(self.camp_name)
        sleep(1)
        CampaignsPage(self.driver)\
            .check_campaign_deleted()

    def searching_by_columns(self):
        """ Login to CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Campaign page """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_CAMPAIGNS)

        """ Get data from list view """
        campaign_id = CampaignsPage(self.driver).get_campaign_id_list_view()
        campaign_name = CampaignsPage(self.driver).get_campaign_name_list_view()
        cpa = CampaignsPage(self.driver).get_cpa_list_view()

        """ Searching by Campaign ID """
        CampaignsPage(self.driver)\
            .set_campaign_id(campaign_id)\
            .campaign_data_checker(campaign_id)\
            .clear_filter()

        """ Searching by Campaign Name """
        CampaignsPage(self.driver) \
            .set_campaign_name(campaign_name) \
            .campaign_data_checker(campaign_name)\
            .clear_filter()

        """ Searching by CPA """
        CampaignsPage(self.driver) \
            .set_cpa(cpa) \
            .campaign_data_checker(cpa)\
            .clear_filter()\
            .refresh_page()

        CampaignsPage(self.driver)\
            .perform_searching_campaign_by_columns(campaign_name,
                                                   campaign_id,
                                                   cpa)\
            .refresh_filter()\
            .campaign_data_checker(campaign_id)\
            .campaign_data_checker(campaign_name)\
            .campaign_data_checker(cpa)

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
