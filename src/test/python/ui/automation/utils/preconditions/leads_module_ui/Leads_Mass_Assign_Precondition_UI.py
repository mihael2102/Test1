from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.leads.LeadDetailViewInfo import LeadDetailViewInfo
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.leads.CreateLeadsProfilePage import CreateLeadsProfilePage
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.constants.LeadsModuleConstantsUI import LeadsModuleConstantsUI


class LeadsMassAssignPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def mass_assign_leads_ui(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_LEADS)

        LeadsModule(self.driver) \
            .select_filter_new_ui(self.config.get_data_lead_info(
                                LeadsModuleConstants.FIRST_LEAD_INFO,
                                LeadsModuleConstants.FILTER_NAME))

        GlobalTablePageUI(self.driver)\
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL)\
            .select_all_records()

        CRMHomePage(self.driver)\
            .open_lead_module()\
            .select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))\
            .enter_email(CRMConstants.SHORT_EMAIL)\
            .click_search_button_leads_module()\
            .click_check_box_all_leads()\
            .click_mass_assign()\
            .input_mass_assign(CRMConstants.PANDAQA_ASSIGN)\
            .select_user_assign(CRMConstants.PANDAQA_ASSIGN)\
            .click_status()

        if global_var.current_brand_name == "uft" or global_var.current_brand_name == "trade99":
            LeadsModule(self.driver)\
                .select_status(CRMConstants.STATUS_EDIT_1)
        elif global_var.current_brand_name == "stoxmarket":
            LeadsModule(self.driver)\
                .select_status(CRMConstants.STATUS_EDIT_STOX)
        else:
            LeadsModule(self.driver)\
                .select_status(CRMConstants.STATUS_ASSIGN)
        LeadsModule(self.driver)\
            .click_assign()\
            .mass_assign_result(CRMConstants.PANDAQA_ASSIGN)
        i = 1
        for i in range(1, 10):
            status = LeadsModule(self.driver).check_status_leads(i)
            if global_var.current_brand_name == "uft" or \
               global_var.current_brand_name == "trade99":
                assert status == CRMConstants.STATUS_EDIT_1
            elif global_var.current_brand_name == "stoxmarket":
                assert status == CRMConstants.STATUS_EDIT_STOX
            else:
                assert status == CRMConstants.STATUS_ASSIGN
            assign_leads = LeadsModule(self.driver).check_assign_leads(i)

            assert assign_leads == CRMConstants.PANDAQA_ASSIGN
