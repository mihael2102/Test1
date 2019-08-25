from time import sleep
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.document.CreateDocumentModule import CreateDocumentModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.utils.logs.Loging import Logging
import autoit
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import os


class CRMBaseMethodsPage(CRMBasePage):

    def select_all_records(self):
        sleep(0.2)
        all_records_checkbox = super().wait_element_to_be_clickable("//*[@id='selectCurrentPageRec']")
        all_records_checkbox.click()
        Logging().reportDebugStep(self, "All records on the page were selected")
        return CRMBaseMethodsPage(self.driver)
