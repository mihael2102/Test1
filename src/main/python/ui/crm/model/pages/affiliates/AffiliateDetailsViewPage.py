from time import sleep

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.affiliates.CreateAffiliateModule import CreateAffiliateModule
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants


class AffiliateDetailsViewPage(CRMBasePage):

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
