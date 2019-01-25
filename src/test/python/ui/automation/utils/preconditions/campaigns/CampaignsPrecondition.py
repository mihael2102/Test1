from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.modules.campaigns_module.AddCampaignsModule import AddCampaignsModule
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
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
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        """ Open Affiliates page """
        campaign_list_view_page = CRMHomePage(self.driver).open_more_list_modules()\
            .select_campaigns_module_more_list(CampaignsConstants.MODULE) \
            .open_add_campaign_module()
        AddCampaignsModule(self.driver).perform_add_new_campaign(self.camp_name,
                                                                 CRMConstants.FIST_ASSIGNED_TO,
                                                                 CRMConstants.START_DATE,
                                                                 CRMConstants.END_DATE,
                                                                 CRMConstants.FIST_DEAL,
                                                                 CRMConstants.RATE)
        CampaignsPage(self.driver).perform_searching_campaign_by_name(self.camp_name)
        sleep(2)
        existing_campaign = CampaignsPage(self.driver).campaign_exist()

        assert self.camp_name == existing_campaign
        #return self.camp_name, existing_campaign
        sleep(2)

    """edit campaign"""
    def edit_campaign(self):
        """ Login to CRM """
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Campaign page """
        CRMHomePage(self.driver).open_more_list_modules() \
            .select_campaigns_module_more_list(CampaignsConstants.MODULE)
        CampaignsPage(self.driver).perform_searching_campaign_by_name(self.camp_name)
        sleep(2)
        CampaignsPage(self.driver).open_campaign_view(self.camp_name)
        sleep(2)
        AddCampaignsModule(self.driver).set_start_date(CRMConstants.START_DATE2)
        AddCampaignsModule(self.driver).set_end_date(CRMConstants.END_DATE2)
        sleep(2)
        AddCampaignsModule(self.driver).click_save_button()
        sleep(2)
        CampaignsPage(self.driver).open_campaign_view(self.camp_name)
        sleep(2)
        actual_start_date = CampaignsPage(self.driver).get_start_date()
        assert actual_start_date == CRMConstants.START_DATE2
        sleep(2)
        assert CampaignsPage(self.driver).get_end_date() == CRMConstants.END_DATE2

    """delete campaign"""
    def delete_campaign(self):
        """ Login to CRM """
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        """ Open Affiliates page """
        CRMHomePage(self.driver).open_more_list_modules() \
                                .select_campaigns_module_more_list(CampaignsConstants.MODULE)
        CampaignsPage(self.driver).perform_searching_campaign_by_name(self.camp_name)
        sleep(2)
        CampaignsPage(self.driver).click_delete_campaign()
        sleep(2)
        CampaignsPage(self.driver).deleting_confirmation()
        sleep(1)
        CampaignsPage(self.driver).perform_searching_campaign_by_name(self.camp_name)
        sleep(1)
        CampaignsPage(self.driver).check_campaign_deleted()


        # return CampaignsPrecondition()

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



