from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import autoit
import os
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class AffiliatesListViewPageUI(CRMBasePage):

    """
        Method get column title and data for searching:
    """
    def set_data_column_field(self, column, data):
        sleep(0.1)
        field = super().wait_load_element("(//input[@placeholder='%s'])[1]" % column)
        field.clear()
        field.send_keys(data)
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        Logging().reportDebugStep(self, "Search by column: " + column + " with data: " + data)
        return AffiliatesListViewPageUI(self.driver)

    def click_on_partner_name(self, name):
        sleep(0.1)
        partner_name = super().wait_element_to_be_clickable("//span[@class='td-link' and contains(text(),'%s')]" % name)
        partner_name.click()
        Logging().reportDebugStep(self, "Open details of affiliate: " + name)
        return AffiliatesListViewPageUI(self.driver)

    def verify_name_on_affiliate_details(self, name):
        sleep(0.1)
        super().wait_load_element("//div[@class='user-name' and text()='%s']" % name)
        Logging().reportDebugStep(self, "Partner name is verified on affiliate's details page: " + name)
        return AffiliatesListViewPageUI(self.driver)

    def click_more_icon(self):
        sleep(2)
        more_btn = super().wait_load_element("//mat-icon[text()='more_vert'][1]", timeout=35)
        self.driver.execute_script("arguments[0].scrollIntoView();", more_btn)
        self.driver.execute_script("arguments[0].click();", more_btn)
        Logging().reportDebugStep(self, "The More button was clicked")
        return AffiliatesListViewPageUI(self.driver)

    def click_delete_icon(self):
        sleep(0.1)
        try:
            delete_btn = self.driver.find_element_by_xpath("//mat-icon[text()='delete'][1]")
            self.driver.execute_script("arguments[0].click();", delete_btn)
            Logging().reportDebugStep(self, "The Delete Affiliates button was clicked")
        except (NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "The Delete Affiliates button does not exist (NOT RUNNED)")
        return AffiliatesListViewPageUI(self.driver)

    def click_delete_btn(self):
        sleep(0.1)
        btn = super().wait_element_to_be_clickable("//span[contains(text(),'Delete')]")
        btn.click()
        sleep(1)
        self.wait_loading_to_finish_new_ui(15)
        Logging().reportDebugStep(self, "Delete Confirmation button was clicked")
        return AffiliatesListViewPageUI(self.driver)

    def verify_data_not_found(self):
        sleep(0.1)
        super().wait_load_element("//span[contains(text(),'No results')]")
        Logging().reportDebugStep(self, "Affiliate was not found")
        return AffiliatesListViewPageUI(self.driver)
