from src.main.python.ui.crm.model.constants.AffiliatePageConstants import AffiliatePageConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
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
            .select_affiliates_module_more_list(AffiliatePageConstants.AFFILIATES_MODULE)

        '''Open popup and create new affiliate '''
        created_client_initial_info = AffiliateListViewPage().created_client_initial_info     # Get dictionary with client info
        return affiliate_list_view_page.open_create_affiliate_popup() \
            .perform_create_affiliate(created_client_initial_info[AffiliatePageConstants.PARTNER_NAME],
                                      created_client_initial_info[AffiliatePageConstants.BRAND_NEW_FOREX],
                                      created_client_initial_info[AffiliatePageConstants.ALLOWED_IP],
                                      created_client_initial_info[AffiliatePageConstants.IS_ENABLED],
                                      created_client_initial_info[AffiliatePageConstants.FIRST_ALLOWED_METHOD],
                                      created_client_initial_info[AffiliatePageConstants.SECOND_ALLOWED_METHOD],
                                      created_client_initial_info[AffiliatePageConstants.THIRD_ALLOWED_METHOD],
                                      created_client_initial_info[AffiliatePageConstants.FOURTH_ALLOWED_METHOD],
                                      created_client_initial_info[AffiliatePageConstants.FIFTH_ALLOWED_METHOD],
                                      created_client_initial_info[AffiliatePageConstants.FIRST_COUNTRY],
                                      created_client_initial_info[AffiliatePageConstants.SECOND_COUNTRY],
                                      created_client_initial_info[AffiliatePageConstants.THIRD_COUNTRY],
                                      created_client_initial_info[AffiliatePageConstants.FOURTH_COUNTRY],
                                      created_client_initial_info[AffiliatePageConstants.FIFTH_COUNTRY])

