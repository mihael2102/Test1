from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.crm_base_page.GlobalSearchPage import GlobalSearchPage
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
        """ Login to CRM """
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Check version in vtiger module """
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

        """ Check version in laravel module """
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

    def global_search_leads(self):
        """ Login to CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_LEADS)

        """ Get Lead data """
        lead_no = LeadsModule(self.driver) \
            .select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))\
            .get_lead_number_list_view('5')

        lead_email = LeadsModule(self.driver)\
            .get_lead_email_list_view('5')

        """ Global Search """
        CRMBaseMethodsPage(self.driver) \
            .global_search_vtiger(lead_no)
        sleep(1)
