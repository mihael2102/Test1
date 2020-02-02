from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.crm_base_page.GlobalSearchPage import GlobalSearchPage
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients.ClientsModulePage import ClientsModulePage


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
            .get_lead_number_list_view(LeadsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING)

        lead_email = LeadsModule(self.driver)\
            .get_lead_email_list_view(LeadsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING)

        created_time = LeadsModule(self.driver)\
            .get_lead_created_time_list_view(LeadsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING)

        """ Global Search """
        lead_email_res = CRMBaseMethodsPage(self.driver) \
            .global_search_vtiger(lead_no)\
            .get_email_search_page_vtiger()
        created_time_res = GlobalSearchPage(self.driver)\
            .get_created_time_search_page_vtiger()

        """ Verify data from results """
        CRMBaseMethodsPage(self.driver)\
            .comparator_string(lead_email, lead_email_res)\
            .comparator_string(created_time.split(" ")[0], created_time_res)

    def global_search_tasks(self):
        """ Login to CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_CLIENTS)\
            .open_tab_list_view(ClientsModuleConstantsUI.TAB_ALL)

        """ Get Client data """
        crm_id = ClientsModulePage(self.driver)\
            .get_client_crm_id_list_view(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_5)

        created_time = ClientsModulePage(self.driver) \
            .get_client_created_time_list_view(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_5)

        """ Open Tasks module """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_TASKS)

        """ Global Search """
        crm_id_res = CRMBaseMethodsPage(self.driver) \
            .global_search_laravel(crm_id) \
            .get_crm_id_search_page_laravel()
        created_time_res = GlobalSearchPage(self.driver) \
            .get_created_time_search_page_laravel()

        """ Verify data from results """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(crm_id, crm_id_res) \
            .comparator_string(created_time, created_time_res)
