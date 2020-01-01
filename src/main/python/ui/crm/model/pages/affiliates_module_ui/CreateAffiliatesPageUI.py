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
        sleep(0.5)
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
         ("//label[contains(text(),' Brand name: ')]//following-sibling::nice-select//ul[@class='options-list']/li[1]")
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select Brand name")
        return CreateAffiliatesPageUI(self.driver)

    def set_allowed_ip(self, ip):
        sleep(0.1)
        ip_field = super().wait_load_element("//input[@formcontrolname='allowedIp']")
        ip_field.clear()
        ip_field.send_keys(ip)
        add_btn = super().wait_element_to_be_clickable("//span[text()='Add ']")
        add_btn.click()
        Logging().reportDebugStep(self, "Set Allowed IP: " + ip)
        return CreateAffiliatesPageUI(self.driver)

    def verify_allowed_ip_added(self, ip):
        sleep(0.1)
        ip_list = super().wait_load_element("//div[@class='ip-list']/div[1]/div[1]").text
        assert ip in ip_list
        Logging().reportDebugStep(self, "Allowed IP added successfully: " + ip)
        return CreateAffiliatesPageUI(self.driver)

    def select_allowed_methods(self, method):
        sleep(0.1)
        item = super().wait_load_element("(//span[contains(text(),'%s')])[1]" % method)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select Allowed Method: " + method)
        return CreateAffiliatesPageUI(self.driver)

    def select_blocked_countries(self, country):
        sleep(0.1)
        item = super().wait_load_element("(//span[contains(text(),'%s')])[1]" % country)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select Blocked Countries: " + country)
        return CreateAffiliatesPageUI(self.driver)

    def click_save(self):
        save_btn = super().wait_element_to_be_clickable("//button[span[contains(text(),'Save')]]")
        save_btn.click()
        Logging().reportDebugStep(self, "Click Save button")
        return CreateAffiliatesPageUI(self.driver)
