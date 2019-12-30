from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.affiliates.AffiliatePage import AffiliatePage


class AffiliatesPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def create_affiliate(self):
        """ Login to CRM """
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Affiliates page """
        affiliate_list_view_page = CRMHomePage(self.driver)\
            .open_more_list_modules()\
            .select_affiliates_module_more_list(AffiliateModuleConstants.AFFILIATES_MODULE)

        ''' Open popup and create new affiliate '''

        affiliate_list_view_page.add_new_affiliate()
        affiliate_list_view_page.add_partner_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])
        affiliate_list_view_page.choose_brand()
        affiliate_list_view_page.enter_allowed_ip(CRMConstants.ALLOWED_IP)
        affiliate_list_view_page.click_plus_ip()
        affiliate_list_view_page.select_allowed_methods(CRMConstants.ALLOWED_METHOD)
        affiliate_list_view_page.select_blocked_country(CRMConstants.BLOCKED_COUNTRY)
        affiliate_list_view_page.click_submit()
        success_message = affiliate_list_view_page.get_success_message()

        if global_var.current_brand_name != "solocapitlas":
            assert success_message == CRMConstants.CREATE_AFFILIATE_SUCCCESS

        CRMHomePage(self.driver).refresh_page()
        affiliate_list_view_page.search_affiliate_by_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])
        AffiliatePage(self.driver).click_on_affiliate(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])

        affiliate_name = affiliate_list_view_page.check_name_on_affiliate_details()
        assert affiliate_name == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME]

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))

        CRMHomePage(self.driver).open_more_list_modules().select_affiliates_module_more_list(
            AffiliateModuleConstants.AFFILIATES_MODULE)
        AffiliatePage(self.driver).search_affiliate_by_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                              LeadsModuleConstants.FIRST_NAME])
        AffiliatePage(self.driver).delete_affiliate()\
                                  .confirm_delete_affiliate()

        CRMHomePage(self.driver).refresh_page()
        AffiliatePage(self.driver).search_affiliate_by_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                                LeadsModuleConstants.FIRST_NAME])

        AffiliatePage(self.driver).check_data_not_found()
