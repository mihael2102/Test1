from time import sleep

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.affiliates.CreateAffiliateModule import CreateAffiliateModule
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants


class AffiliatePage(CRMBasePage):
    def __init__(self):
        super().__init__()

    def open_create_affiliate_popup(self):
        """
        Open create new affiliate popup
        :return: AffiliateModule()
        """
        add_new_affiliate_button = super().wait_element_to_be_clickable(
            "//button[contains(text(), 'Add new affiliate')]")
        add_new_affiliate_button.click()
        Logging().reportDebugStep(self, "Open 'Add new affiliate' popup")
        return CreateAffiliateModule()

    def open_affiliate_details_page(self, existed_partner_name):
        sleep(2)
        partner_name_from_list = self.driver.find_element(By.XPATH, "//grid-cell/div/link-spa/a[contains(., '%s')]" % existed_partner_name)
        # if partner_name_from_list.text == AffiliateModuleConstants.PARTNER_NAME:
        #     partner_name_from_list.click()
        partner_name_from_list.click()
        Logging().reportDebugStep(self,
                                  "Open details page of required affiliate -> " + AffiliateModuleConstants.PARTNER_NAME)
    # else:
    #     Logging().reportDebugStep(self, "There is no required affiliate" + AffiliateModuleConstants.PARTNER_NAME)


    def perform_search_by_partner_name(self, partner_name_text):
        partner_name_input = self.driver.find_element(By.XPATH, "(//*[@id='host-element']/input)[2]")

        sleep(1)
        partner_name_input.clear()
        partner_name_input.send_keys(partner_name_text)

        Logging().reportDebugStep(self, "Searching by partner name: " + partner_name_text)
