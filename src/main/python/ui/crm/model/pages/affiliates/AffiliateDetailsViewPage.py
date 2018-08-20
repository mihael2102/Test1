from time import sleep

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.affiliates.CreateAffiliateModule import CreateAffiliateModule
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.constants.AffiliatePageConstants import AffiliatePageConstants


class AffiliateDetailsViewPage(CRMBasePage):

    def open_affiliate_list_view_page(self):
        """If URL contains digit in the end it means that we are at Details page and need to go to List view page via menu button. Else stay at current page"""
        if list(self.driver.current_url)[-2] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            """Click on Affiliate button in menu"""
            self.driver.find_element(By.XPATH, "//ul[1]/li[6]/a").click()
        return ""

    def get_partner_name(self):
        sleep(2)
        partner_name_text = self.driver.find_element(By.XPATH, "//div[1]/div/div[1]/h1").text
        return partner_name_text

    def get_partner_id(self):
        sleep(2)
        partner_id_text = self.driver.find_element(By.XPATH, "(//div/div[1]/div/div[1]/div)[2]").text
        return partner_id_text

    def get_brand(self):
        brand_text = self.driver.find_element(By.XPATH, "//tbody/tr/td[7]/div[2]").text
        return brand_text
