from time import sleep

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.affiliates.CreateAffiliateModule import CreateAffiliateModule
from src.main.python.ui.crm.model.pages.affiliates.AffiliateDetailsViewPage import AffiliateDetailsViewPage
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants


class AffiliateListViewPage(CRMBasePage):
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
        sleep(1)
        partner_name_from_list = self.driver.find_element(By.XPATH, "//grid-cell/div/link-spa/a[contains(., '%s')]" % existed_partner_name)
        partner_name_from_list.click()
        Logging().reportDebugStep(self,
                                  "Open details page of required affiliate -> " + AffiliateModuleConstants.PARTNER_NAME)
        return AffiliateDetailsViewPage()


    def perform_search_by_partner_name(self, partner_name_text):
        partner_name_input = self.driver.find_element(By.XPATH, "(//*[@id='host-element']/input)[2]")

        sleep(1)
        partner_name_input.clear()
        partner_name_input.send_keys(partner_name_text)

        Logging().reportDebugStep(self, "Searching by partner name: " + partner_name_text)
        return  AffiliateListViewPage()

    def get_partner_id(self):
        partner_id_text = self.driver.find_element(By.XPATH, "//td[2]/grid-cell/div/span[2]").text
        return partner_id_text

    def get_is_enabled(self):
        is_enabled_text = self.driver.find_element(By.XPATH, "//td[5]/grid-cell/div/span[2]").text
        return is_enabled_text

    def get_allowed_ip(self):
        allowed_ip_text = self.driver.find_element(By.XPATH, "//td[6]/grid-cell/div/span[2]").text
        return allowed_ip_text

    def get_blocked_countries(self):
        blocked_countries_text = self.driver.find_element(By.XPATH, "//td[7]/grid-cell/div/span[2]").text
        return blocked_countries_text

    def get_allowed_methods(self):
        allowed_methods_text = self.driver.find_element(By.XPATH, "//td[8]/grid-cell/div/span[2]").text
        return allowed_methods_text

    def get_brand_name(self):
        brand_name_text = self.driver.find_element(By.XPATH, "//td[9]/grid-cell/div/span[2]").text
        return brand_name_text




