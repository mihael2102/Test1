from time import sleep

from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.affiliates_modules.CreateAffiliateModule import CreateAffiliateModule
from src.main.python.ui.crm.model.modules.document_module.CreateDocumentModule import CreateDocumentModule
from src.main.python.ui.crm.model.modules.filter.FilterModule import FilterModule
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.utils.logs.Loging import Logging

class AffiliateModule(CRMBasePage):
    def __init__(self):
        super().__init__()


    def open_create_affiliate_popup(self):
        """
        Open create new affiliate popup
        :return: AffiliateModule()
        """
        add_new_affiliate_button = super().wait_element_to_be_clickable("//button[contains(text(), 'Add new affiliate')]")
        Logging().reportDebugStep(self, "Open 'Add new affiliate' popup")
        return CreateAffiliateModule()