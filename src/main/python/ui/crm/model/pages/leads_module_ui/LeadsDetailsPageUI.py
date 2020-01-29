from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class LeadsDetailsPageUI(CRMBasePage):

    def get_text_from_field(self, field):
        sleep(0.1)
        data = super().wait_load_element(
            "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-txt-wrapper')]" % field).text
        Logging().reportDebugStep(self, "Get data from field " + field + ": " + data)
        return data

    def open_tab(self, title):
        try:
            tab = super().wait_load_element(
                "//mat-expansion-panel-header[@aria-expanded='false']//mat-panel-title/div[contains(text(),'%s')]"
                % title)
            self.driver.execute_script("arguments[0].click();", tab)
            Logging().reportDebugStep(self, "Open tab: " + title)
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Tab " + title + " already opened")
        return LeadsDetailsPageUI(self.driver)
