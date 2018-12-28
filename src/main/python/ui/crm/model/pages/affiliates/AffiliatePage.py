from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.document.CreateDocumentModule import CreateDocumentModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.document.DocumentDetailViewPage import DocumentDetailViewPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException
import autoit
import os
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class AffiliatePage(CRMBasePage):

    def add_new_affiliate(self):
        add_new_affiliate_button = super().wait_element_to_be_clickable(
            "//button[contains(text(), 'Add new affiliate')]")
        add_new_affiliate_button.click()
        Logging().reportDebugStep(self, "Open 'Add new affiliate' popup")

    def add_partner_name(self, name):
        sleep(1)
        input_partner_name = super().wait_load_element("//*[@id='partnerName']")
        sleep(1)
        input_partner_name.send_keys(name)
        sleep(1)
        Logging().reportDebugStep(self, "Enter partner name")

    def choose_brand(self):
        try:
            brand_list = Select(self.driver.find_element(By.XPATH, "//*[@id='brand']"))
            brand_list.select_by_index(1)
            Logging().reportDebugStep(self, "Choose brand")
        except NoSuchElementException:
            Logging().reportDebugStep(self, "Brand select box was not found")
        # select_drop_down_brand = Select(super().wait_element_to_be_clickable("//*[@id='brand']"))
        # select_drop_down_brand.select_by_visible_text()
        # Logging().reportDebugStep(self, "")

    def enter_allowed_ip(self, allowed_ip):
        input_ip = super().wait_load_element("//*[@id='allowedIps']")
        input_ip.send_keys(allowed_ip)
        Logging().reportDebugStep(self, "Enter allowed IP")

    def click_plus_ip(self):
        sleep(5)
        button_plus = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["button_plus"])
        button_plus.click()
        Logging().reportDebugStep(self, "Click plus ip")

    def select_allowed_methods(self, method):
        methods_drop_down = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["methods_drop_down"])
        methods_drop_down.click()
        input_methods = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["input_methods"])
        input_methods.send_keys(method)
        methods = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["methods"]
            % method)
        methods.click()
        Logging().reportDebugStep(self, "Select allowed methods %s" % method)

    def select_blocked_country(self, country):
        country_drop_down = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["blocked_country_drop_down"])
        country_drop_down.click()
        sleep(1)
        input_country = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["input_country"])
        input_country.send_keys(country)
        sleep(5)
        countrys = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["countrys"]
            % country)
        countrys.click()

        Logging().reportDebugStep(self, "Select blocked country %s" % country)

    def click_submit(self):
        button_submit = super().wait_element_to_be_clickable("//button[@class = 'btn btn-success']")
        # button_submit.click()
        sleep(1)
        self.driver.execute_script("arguments[0].click();", button_submit)
        Logging().reportDebugStep(self, "Click Submit")

    def get_success_message(self):
        success_message = super().wait_load_element("//div[contains(text(),'Success')]").text
        Logging().reportDebugStep(self, "Text from 'Update' popup has been got: " + success_message)
        return success_message

    def search_affiliate_by_name(self, name):
        input_partner_name = super().wait_load_element("//td[3]//input")
        input_partner_name.send_keys(name)
        sleep(2)
        affiliate_name = super().wait_load_element("/html/body/app-root/affiliate-list/div[2]/div[2]/grid/div/div/div[1]/table/tbody/tr[2]/td[3]")
        affiliate_name.click()
        Logging().reportDebugStep(self, "Search partner name and go to affiliate details page")

    def check_name_on_affiliate_details(self):
        title_details = super().wait_load_element("/html/body/app-root/affiliate-details/div/div[1]/div/div[1]/h1").text
        Logging().reportDebugStep(self, "Affiliate details page")
        return title_details

    def Sign_Out(self):
        CRMBasePage(self.driver).refresh_page()
        sleep(2)
        user = super().wait_element_to_be_clickable("//*[@id='bs-example-navbar-collapse-1']/ul[2]/li[3]/a/img")
        # self.driver.execute_script("arguments[0].click();", user)
        user.click()
        sleep(2)
        sign_out = super().wait_element_to_be_clickable("//a[contains(text(), 'Sign Out')]")
        self.driver.execute_script("arguments[0].click();", sign_out)
        Logging().reportDebugStep(self, "Sign Out")
        return AffiliatePage(self.driver)