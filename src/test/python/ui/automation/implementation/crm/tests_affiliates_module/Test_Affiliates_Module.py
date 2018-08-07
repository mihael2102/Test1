from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.test.python.ui.automation.utils.postconditions.affiliates.Affiliates_Postcondition import \
    AffiliatesPostcondition
from src.test.python.ui.automation.utils.preconditions.affiliates.Affiliates_Precondition import AffiliatesPrecondition
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage


class AffiliateModule(BaseTest):

    def test_create_affiliate(self):

        AffiliatesPrecondition().create_affiliate()

        affiliate_list_view_page = AffiliateListViewPage()

        """ Perform search by Partner name """
        affiliate_list_view_page.perform_search_by_partner_name(AffiliateModuleConstants.PARTNER_NAME)

        """ Check values on List view page """

        assert Config.data.get_data_affliate_info(
            AffiliateModuleConstants.IS_ENABLED) == affiliate_list_view_page.get_is_enabled()
        assert Config.data.get_data_affliate_info(
            AffiliateModuleConstants.ALLOWED_IP) == affiliate_list_view_page.get_allowed_ip()

        """ Check blocked countries """

        assert AffiliateListViewPage().check_blocked_countries()

        """ Check allowed methods """
        assert AffiliateListViewPage().check_allowed_methods()

        """ Check brand name """
        assert Config.data.get_data_affliate_info(
            AffiliateModuleConstants.BRAND_NEW_FOREX) == affiliate_list_view_page.get_brand_name()

        """ Open affiliate details page and check values on Details view page """
        affiliate_details_page = affiliate_list_view_page.open_affiliate_details_page(AffiliateModuleConstants.PARTNER_NAME)

        partner_name_for_checking = affiliate_details_page.get_partner_name()

        assert AffiliateModuleConstants.PARTNER_NAME == partner_name_for_checking

        assert Config.data.get_data_affliate_info(
            AffiliateModuleConstants.BRAND_NEW_FOREX) == affiliate_details_page.get_brand()

        """Postcondition - Delete created affiliate"""
        AffiliatesPostcondition().delete_affiliate(AffiliateModuleConstants.PARTNER_NAME)


    def test_edit_affiliate(self):

        AffiliatesPrecondition().create_affiliate()

        """ Open 'Edit' popup and edit affiliate """
        affiliate_list_view_page = AffiliateListViewPage()

        affiliate_list_view_page.edit_affiliate(AffiliateModuleConstants.PARTNER_NAME)

        """ Perform search by Partner name """
        affiliate_list_view_page.perform_search_by_partner_name(AffiliateModuleConstants.PARTNER_NAME_EDITED)

        """ Check values on List view page """
        assert affiliate_list_view_page.edited_client_initial_info[AffiliateModuleConstants.IS_ENABLED] == affiliate_list_view_page.get_is_enabled()


        assert affiliate_list_view_page.edited_client_initial_info[AffiliateModuleConstants.ALLOWED_IP] == affiliate_list_view_page.get_allowed_ip()

        """ Check blocked countries """
        assert AffiliateListViewPage().check_editing_of_blocked_countries()

        """ Check allowed methods """
        assert AffiliateListViewPage().check_editing_of_allowed_methods(affiliate_list_view_page.edited_client_initial_info[AffiliateModuleConstants.EDITED_FIRST_ALLOWED_METHOD_NAME])

        """ Check brand name """
        assert affiliate_list_view_page.edited_client_initial_info[AffiliateModuleConstants.BRAND_NEW_FOREX] == affiliate_list_view_page.get_brand_name()

        """ Open affiliate details page and check values on Details view page """
        affiliate_details_page = affiliate_list_view_page.open_affiliate_details_page(
            AffiliateModuleConstants.PARTNER_NAME_EDITED)

        partner_name_for_checking = affiliate_details_page.get_partner_name()

        assert AffiliateModuleConstants.PARTNER_NAME_EDITED == partner_name_for_checking

        assert affiliate_list_view_page.edited_client_initial_info[AffiliateModuleConstants.BRAND_NEW_FOREX] == affiliate_details_page.get_brand()

        """Postcondition - Delete created affiliate"""
        AffiliatesPostcondition().delete_affiliate(AffiliateModuleConstants.PARTNER_NAME_EDITED)

    def test_delete_affiliate(self):
        AffiliatesPrecondition().create_affiliate()

        AffiliatesPostcondition().delete_affiliate(AffiliateModuleConstants.PARTNER_NAME)

        assert AffiliateListViewPage().is_affiliate_deleted(AffiliateModuleConstants.PARTNER_NAME)








