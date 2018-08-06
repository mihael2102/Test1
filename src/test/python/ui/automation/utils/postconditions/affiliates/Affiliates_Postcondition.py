from time import sleep

from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.affiliates.AffiliateDetailsViewPage import AffiliateDetailsViewPage
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.utils.logs.Loging import Logging
from src.test.python.ui.automation.BaseTest import BaseTest


class AffiliatesPostcondition(BaseTest):

    def delete_affiliate(self, partner_name):
        affiliate_details_page = AffiliateDetailsViewPage()
        affiliate_details_page.open_affiliate_list_view_page()

        """Find needed affiliate"""
        affiliate_list_view_page = AffiliateListViewPage()
        affiliate_list_view_page.perform_search_by_partner_name(partner_name)

        """Click delete button and Confirm deletion"""
        affiliate_list_view_page.click_delete_icon_and_confirm_deletion()

        return AffiliateListViewPage()


