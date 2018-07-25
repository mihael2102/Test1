from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


class AffiliatesPrecondition(object):

    def create_affiliate(self):
        """ Login to CRM """
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        """ Open Affiliates page """
        affiliate_list_view_page = CRMHomePage().open_more_list_modules().open_more_list_modules() \
            .select_affiliates_module_more_list(AffiliateModuleConstants.AFFILIATES_MODULE)

        '''Open popup and create new affiliate '''
        return affiliate_list_view_page.open_create_affiliate_popup() \
            .perform_create_affiliate(AffiliateModuleConstants.PARTNER_NAME,
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.BRAND_NEW_FOREX),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.ALLOWED_IP),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.IS_ENABLED),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.FIRST_ALLOWED_METHOD),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.SECOND_ALLOWED_METHOD),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.THIRD_ALLOWED_METHOD),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.FOURTH_ALLOWED_METHOD),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.FIFTH_ALLOWED_METHOD),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.FIRST_COUNTRY),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.SECOND_COUNTRY),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.THIRD_COUNTRY),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.FOURTH_COUNTRY),
                                      Config.data.get_data_affliate_info(AffiliateModuleConstants.AFFILIATE_INFO,
                                                                         AffiliateModuleConstants.FIFTH_COUNTRY))

