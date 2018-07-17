from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class CreateAffiliate(BaseTest):

    def test_create_affiliate(self):
        # Login to CRM
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD))


        # Open Affiliates module
        affiliate_module = CRMHomePage().open_more_list_modules().open_more_list_modules() \
            .select_affiliates_module_more_list(AffiliateModuleConstants.AFFILIATES_MODULE)


        # Create new affiliate
        affiliate_module.open_create_affiliate_popup().perform_create_affiliate()


        # Read the message after creating affiliate




