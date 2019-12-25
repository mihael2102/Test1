from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException
import autoit
import os
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class CreateAffiliatesPageUI(CRMBasePage):

    def click_add_new_affiliate_btn(self):
        add_new_affiliate_btn = super().wait_element_to_be_clickable("//span[contains(text(),' Add new affiliate ')]")
        add_new_affiliate_btn.click()
        Logging().reportDebugStep(self, "Click 'Add new affiliate' button")
        return CreateAffiliatesPageUI(self.driver)

    def set_partner_name(self, name):
        sleep(0.5)
        partner_name_field = super().wait_load_element("//input[@formcontrolname='partnerName']")
        partner_name_field.clear()
        partner_name_field.send_keys(name)
        Logging().reportDebugStep(self, "Set Partner Name: " + name)
        return CreateAffiliatesPageUI(self.driver)

    """
        Select first item from pick list Brand name:
    """

    def select_brand(self):
        sleep(0.2)
        item = super().wait_load_element\
         ("//label[contains(text(),' Brand name: ')]//following-sibling::nice-select//ul[@class='options-list']//a[1]")
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select Brand name")
        return CreateAffiliatesPageUI(self.driver)
