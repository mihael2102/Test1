import re
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from _decimal import Decimal
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from selenium.webdriver.support.select import Select
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class ClientDetailsPageUI(CRMBasePage):

    def get_text_from_field(self, field):
        sleep(0.1)
        try:
            try:
                data = super().wait_load_element(
                    "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-txt-wrapper')]" % field,
                    timeout=5).text
            except(NoSuchElementException, TimeoutException):
                Logging().reportDebugStep(self, "Field " + field + " is not editable")
                data = super().wait_load_element(
                    "//div[label='%s']//following-sibling::div//div[@class='ng-star-inserted']" % field).text
            Logging().reportDebugStep(self, "Get data from field " + field + ": " + data)
            return data
        except:
            Logging().reportDebugStep(self, "Field " + field + " does not exist")
            return False

    def open_tab(self, title):
        try:
            Logging().reportDebugStep(self, "Open tab: " + title)
            tab = super().wait_load_element(
                "//mat-expansion-panel-header[@aria-expanded='false']//mat-panel-title/div[contains(text(),'%s')]"
                % title)
            self.driver.execute_script("arguments[0].click();", tab)
            sleep(1)
            self.wait_loading_to_finish_new_ui(5)
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Tab " + title + " already opened")
        return ClientDetailsPageUI(self.driver)

    def get_data_from_info_tag(self, tag_title):
        sleep(0.1)
        tag = super().wait_load_element(
            "(//div[contains(text(),'%s')]//following-sibling::div[contains(@class,'info-tags')])[1]" % tag_title).text
        Logging().reportDebugStep(self, "Get data from tag '" + tag_title + "': " + tag)
        return tag

    def open_mt4_module_newui(self, module):
        try:
            sleep(0.2)
            module_item = super().wait_load_element("//div[text()=' %s ']" % module)
            self.driver.execute_script("arguments[0].click();", module_item)
            Logging().reportDebugStep(self, module + " module is opened")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Module does not exist (NOT RUNNED)")
