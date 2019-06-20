from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.modules.campaigns_module.AddCampaignsModule import AddCampaignsModule
from src.main.python.ui.crm.model.pages.campaigns.CampaignsPage import CampaignsPage
from time import sleep

class BaseCRMPrecondition(object):
    driver = None
    config = None
    camp_name = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.camp_name = CRMConstants.CAMPAIGN_NAME

    def check_sprint_version(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_client_module()
        current_vtiger_version = CRMHomePage(self.driver).get_current_version()
        prev_vtiger_version = CRMHomePage(self.driver).check_previous_version()
        day = CRMHomePage(self.driver).get_day_of_week()
        if day == 6:
            assert int(current_vtiger_version) == int(prev_vtiger_version) + 1
        else:
            assert int(current_vtiger_version) == int(prev_vtiger_version)