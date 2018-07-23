from time import sleep
from datetime import *
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.modules.leads_module.MassAssignLeadModule import MassAssignLeadModule
from src.main.python.ui.crm.model.modules.leads_module.MassEditLeadModule import MassEditLeadModule
from src.main.python.ui.crm.model.pages.leads.CreateLeadsProfilePage import CreateLeadsProfilePage
from src.main.python.utils.config import Config
from selenium.webdriver.support.ui import Select
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants

class CreateAffiliateModule(CRMBasePage):
    """
    Methods which are related to "Create affiliate" popup
    """

    def __init__(self):
        super().__init__()

    def perform_create_affiliate(self, partner_name, brand, allowed_ip, is_enabled, allowed_methods, blocked_countries):
        """
        Fill fields of the "Add new affiliate" form
        """
        return None


    def set_partner_name(self, partner_name):
        partner_name_field = super().wait_load_element("//input[@name='partnerName']")
        partner_name_field.clear()
        partner_name_field.send_keys(partner_name)
        Logging.reportDebugStep(self, "Partner name was set: " + partner_name)
        return CreateAffiliateModule()

    def set_brand(self, brand=""):
        if brand == AffiliateModuleConstants.BRAND_NEW_FOREX:
            brand_drop_down = Select(self.driver.find_element(By.XPATH, "//*[@id='brand']"))
            brand_drop_down.select_by_value(AffiliateModuleConstants.BRAND_NEW_FOREX)
        elif brand == AffiliateModuleConstants.BRAND_NFX:
            brand_drop_down = Select(self.driver.find_element(By.XPATH, "//*[@id='brand']"))
            brand_drop_down.select_by_value(AffiliateModuleConstants.BRAND_NFX)
        else:
            """ 
            Brand is not selected
            Use it for negative test cases 
            """

    def set_allowed_ip(self, ip_value):
        allowed_ip_field = self.driver.find_element(By.XPATH, "//*[@id='allowedIps']")
        add_ip_button = self.driver.find_element(By.XPATH, "//bs-modal-body/div/div[3]/button")
        add_ip_button.click()










