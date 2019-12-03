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


class GlobalSearchPage(CRMBasePage):

    def get_module_title_from_result_vtiger(self):
        module_title = super().wait_load_element("//div[@class='row unified_search_module_title']")\
            .get_attribute("innerText")
        Logging().reportDebugStep(self, "Get module title: " + item)
        return GlobalSearchPage(self.driver)
