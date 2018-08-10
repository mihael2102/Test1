from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.leads.LeadsPage import LeadsPage
from src.main.python.utils.config import Config


class LeadPostCondition(object):
    def __init__(self) -> None:
        super().__init__()

    def delete_lead_by_pencil(self):
        CRMHomePage().open_lead_module()
        LeadsPage().select_filter(
            Config.data.get_data_lead_info(
                LeadsModuleConstants.LEADS_MODULE_COLUMNS, LeadsModuleConstants.FILTER_NAME)) \
            .enter_first_name(LeadsModuleConstants.SECOND_NAME_LEAD)\
            .click_search_button_leads_module()\
            .click_delete_lead() \
            .get_confirm_delete_ticket()
        return LeadPostCondition()
