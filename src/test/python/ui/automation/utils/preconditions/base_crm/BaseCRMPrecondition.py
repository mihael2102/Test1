from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
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
        # check version in vtiger module
        CRMHomePage(self.driver).open_client_module()
        brand = global_var.current_brand_name
        current_vtiger_version = CRMHomePage(self.driver).get_current_version(CRMConstants.MODULE_VTIGER)
        prev_vtiger_version = CRMHomePage(self.driver).check_previous_version(brand, CRMConstants.MODULE_VTIGER)
        day = CRMHomePage(self.driver).get_day_of_week()
        if day == 6:
            assert int(current_vtiger_version) == int(prev_vtiger_version) + 1
            new_version = int(prev_vtiger_version) + 1
            CRMHomePage(self.driver).update_version_in_file(new_version,
                                                            prev_vtiger_version,
                                                            brand)
        else:
            assert int(current_vtiger_version) == int(prev_vtiger_version)

        # check version in laravel module
        CRMHomePage(self.driver).open_task_module()
        brand = global_var.current_brand_name
        current_laravel_version = CRMHomePage(self.driver).get_current_version(CRMConstants.MODULE_LARAVEL)
        prev_laravel_version = CRMHomePage(self.driver).check_previous_version(brand, CRMConstants.MODULE_LARAVEL)
        day = CRMHomePage(self.driver).get_day_of_week()
        if day == 6:
            assert int(current_laravel_version) == int(prev_laravel_version) + 1
            new_version = int(prev_laravel_version) + 1
            CRMHomePage(self.driver).update_version_in_file(new_version,
                                                            prev_laravel_version,
                                                            brand)
        else:
            assert int(current_laravel_version) == int(prev_laravel_version)
