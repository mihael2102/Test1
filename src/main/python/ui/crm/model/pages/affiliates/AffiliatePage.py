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
        button_plus = super().wait_element_to_be_clickable("/html/body/bs-modal[2]/div/div/form/bs-modal-body/div/div[2]/button")
        # button_plus.click()
        self.driver.execute_script("arguments[0].click();", button_plus)
        Logging().reportDebugStep(self, "Click plus ip")

    def select_allowed_methods(self, method):
        sleep(1)
        methods_drop_down = super().wait_element_to_be_clickable("/html/body/bs-modal[2]/div/div/form/bs-modal-body/div/div[4]/div[2]")
        sleep(1)
        methods_drop_down.click()
        sleep(1)
        input_methods = super().wait_load_element("/html/body/bs-modal[2]/div/div/form/bs-modal-body/div/div[4]/div[2]/filter-multi-select/div/div[2]/span[1]/input")
        sleep(1)
        input_methods.send_keys(method)
        sleep(1)
        methods = super().wait_load_element("//span[@class = 'hovered-option'][contains(text(),'%s')]" % method)
        sleep(1)
        methods.click()
        Logging().reportDebugStep(self, "Select allowed methods %s" % method)

    def select_blocked_country(self, country):
        # title = self.driver.find_element(By.XPATH, "/html/body/bs-modal[2]/div/div/form/bs-modal-header/div/h4")
        # title.click()
        sleep(1)
        country_drop_down = super().wait_element_to_be_clickable("/html/body/bs-modal[2]/div/div/form/bs-modal-body/div/div[5]/div[2]")
        country_drop_down.click()
        sleep(1)
        input_country = super().wait_load_element("/html/body/bs-modal[2]/div/div/form/bs-modal-body/div/div[5]/div[2]/filter-multi-select/div/div[2]/span[1]/input")
        sleep(1)
        input_country.send_keys(country)
        sleep(1)
        countrys = super().wait_load_element("//span[@class = 'hovered-option'][contains(text(),'%s')]" % country)
        sleep(1)
        countrys.click()
        Logging().reportDebugStep(self, "Select blocked country %s" % country)

    def click_submit(self):
        button_submit = super().wait_element_to_be_clickable("//button[@class = 'btn btn-success']")
        button_submit.click()
        Logging().reportDebugStep(self, "Click Submit")

    def get_success_message(self):
        success_message = super().wait_load_element("//div[contains(text(),'Success')]").text
        Logging().reportDebugStep(self, "Text from 'Update' popup has been got: " + success_message)
        return success_message

    def search_affiliate_by_name(self, name):
        input_partner_name = super().wait_load_element("//td[3]//input")
        input_partner_name.send_keys(name)
        sleep(2)
        affiliate_name = super().wait_load_element("//a[contains(text(),'testqa')]")
        self.driver.execute_script("arguments[0].click();", affiliate_name)
        Logging().reportDebugStep(self, "Search partner name and go to affiliate details page")

    def check_name_on_affiliate_details(self):
        title_details = super().wait_load_element("/html/body/app-root/affiliate-details/div/div[1]/div/div[1]/h1").text
        Logging().reportDebugStep(self, "Affiliate details page")
        return title_details