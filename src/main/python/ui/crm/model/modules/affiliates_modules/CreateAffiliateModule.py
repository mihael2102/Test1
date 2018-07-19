from time import sleep

from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.document_module.CreateDocumentModule import CreateDocumentModule
from src.main.python.ui.crm.model.modules.filter.FilterModule import FilterModule
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging

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
        partner_name_field.







