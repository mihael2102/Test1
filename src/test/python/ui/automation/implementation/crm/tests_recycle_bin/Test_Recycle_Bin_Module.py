from src.main.python.ui.crm.model.constants.RecycleBinModuleConstants import RecycleBinModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.utils.postconditions.lead.LeadPostCondition import LeadPostCondition
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition


class RecycleBinTest(BaseTest):

    def test_check_recycle_bin(self):
        LeadPrecondition().create_lead()

        LeadPostCondition().delete_lead_by_pencil()

        recycle_module = CRMHomePage().open_client_module()\
            .open_more_list_modules() \
            .select_recycle_bin_module_more_list(RecycleBinModuleConstants.RECYCLE_BIN_MODULE)
