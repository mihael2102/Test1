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
        Logging().reportDebugStep(self, "Enter partner name: " + name)

    def choose_brand(self):
        try:
            brand_list = Select(self.driver.find_element(By.XPATH, "//*[@id='brand']"))
            brand_list.select_by_index(1)
            Logging().reportDebugStep(self, "Choose brand")
        except NoSuchElementException:
            Logging().reportDebugStep(self, "Brand select box was not found")

    def enter_allowed_ip(self, allowed_ip):
        input_ip = super().wait_load_element("//*[@id='allowedIps']")
        input_ip.send_keys(allowed_ip)
        Logging().reportDebugStep(self, "Enter allowed IP: " + allowed_ip)

    def click_plus_ip(self):
        sleep(0.5)
        button_plus = super().wait_load_element("//button[text()=' +']")
        self.driver.execute_script("arguments[0].click();", button_plus)
        Logging().reportDebugStep(self, "Click plus ip")

    def select_allowed_methods(self, method):
        sleep(1)
        methods_drop_down = super().wait_element_to_be_clickable(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[4]/div[2]")
        sleep(1)
        methods_drop_down.click()
        sleep(1)
        input_methods = super().wait_load_element(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[4]/div[2]/filter-multi-select/div/div[2]/span[1]/input")
        sleep(1)
        input_methods.send_keys(method)
        sleep(1)
        methods = super().wait_load_element(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[4]/div[2]/filter-multi-select/div/div[2]/span[contains(text(),'%s')]" % method)
        sleep(1)
        methods.click()
        Logging().reportDebugStep(self, "Select allowed methods %s" % method)

    def select_blocked_country(self, country):
        sleep(1)
        country_drop_down = super().wait_element_to_be_clickable(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[5]/div[2]")
        country_drop_down.click()
        sleep(1)
        input_country = super().wait_load_element(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[5]/div[2]/filter-multi-select/div/div[2]/span[1]/input")
        sleep(1)
        input_country.send_keys(country)
        sleep(1)
        countrys = super().wait_load_element(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[5]/div[2]/filter-multi-select/div/div[2]/span[contains(text(),'%s')]" % country)
        sleep(1)
        countrys.click()
        Logging().reportDebugStep(self, "Select blocked country %s" % country)

    def click_submit(self):
        button_submit = super().wait_element_to_be_clickable("//button[@class = 'btn btn-success']")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", button_submit)
        Logging().reportDebugStep(self, "Click Submit")

    def get_success_message(self):
        success_message = super().wait_load_element("//div[contains(text(),'Success')]").text
        Logging().reportDebugStep(self, "Text from 'Update' popup has been got: " + success_message)
        return success_message

    def search_affiliate_by_name(self, name):
        sleep(1)
        self.wait_crm_loading_to_finish_tasks(55)
        input_partner_name = super().wait_load_element("//td[3]//input")
        input_partner_name.send_keys(name)
        Logging().reportDebugStep(self, "Search partner name: " + name)

    def click_on_affiliate(self, name):
        affiliate_name = super().wait_load_element("//a[contains(text(), '%s')]" % name)
        self.driver.execute_script("arguments[0].click();", affiliate_name)
        Logging().reportDebugStep(self, "Go to affiliate details page")

    def check_name_on_affiliate_details(self):
        title_details = super().wait_load_element("/html/body/app-root/affiliate-details/div/div[1]/div/div[1]/h1").text
        Logging().reportDebugStep(self, "Affiliate name is verified: " + title_details)
        return title_details

    def delete_affiliate(self):
        sleep(3)
        trash_button = super().wait_load_element(
            "//span[@class = 'glyphicon glyphicon-trash cursor-pointer ng-star-inserted']")
        trash_button.click()
        Logging().reportDebugStep(self, "Delete button was clicked")
        return AffiliatePage(self.driver)

    def confirm_delete_affiliate(self):
        sleep(2)
        confirm_button = super().wait_element_to_be_clickable("//button[contains (text(), 'Confirm')]")
        confirm_button.click()
        Logging().reportDebugStep(self, "Confirm delete button was clicked")
        return AffiliatePage(self.driver)

    def check_data_not_found(self):
        super().wait_visible_of_element("//td[contains (text(), 'Data not found')]")
        Logging().reportDebugStep(self, "Data not found")
        return AffiliatePage(self.driver)

    def search_by_partner_id(self, partner_id):
        sleep(2)
        input = self.driver.find_element(By.XPATH, "//*[@id='host-element']/input")
        input.send_keys(partner_id)
        Logging().reportDebugStep(self, "Enter partner ID %s" % partner_id)
        return AffiliatePage(self.driver)

    def open_edit_affiliate(self):
        sleep(3)
        edit_button = self.driver.find_element(By.XPATH,
                                        "//span[@class='glyphicon glyphicon-pencil cursor-pointer ng-star-inserted']")
        edit_button.click()
        Logging().reportDebugStep(self, "Click edit affiliate")
        return AffiliatePage(self.driver)

    def check_selected_methods(self):
        sleep(3)
        selected_number = super().wait_load_element(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[4]/div[2]/filter-multi-select/div/div[1]").text
        Logging().reportDebugStep(self, "Check selected methods")
        return selected_number

    def add_all_methods(self):
        sleep(3)
        methods = super().wait_element_to_be_clickable(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[4]/div[2]")
        methods.click()
        sleep(2)
        all_methods = super().wait_element_to_be_clickable(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[4]/div[2]/filter-multi-select/div/div[2]/span[2]/i")
        all_methods.click()
        sleep(4)
        all_methods.click()
        Logging().reportDebugStep(self, "Select all methods")
        return AffiliatePage(self.driver)

    def check_selected_countries(self):
        sleep(3)
        selected_number = super().wait_load_element(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[5]/div[2]/filter-multi-select/div/div[1]/span").text
        Logging().reportDebugStep(self, "Check selected blocked countries")
        return selected_number

    def add_none_selected_countries(self):
        sleep(3)
        methods = super().wait_element_to_be_clickable(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[5]/div[2]/filter-multi-select/div/div[1]/span")
        methods.click()
        sleep(2)
        all_methods = super().wait_element_to_be_clickable(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[5]/div[2]/filter-multi-select/div/div[2]/span[2]")
        all_methods.click()
        Logging().reportDebugStep(self, "None selected countries")
        return AffiliatePage(self.driver)

    def copy_secret_key(self):
        sleep(5)
        copy_button = super().wait_element_to_be_clickable("//button[contains(text(), 'Copy')]")
        self.driver.execute_script("arguments[0].click();", copy_button)
        sleep(3)
        key = super().wait_load_element("/html/body/bs-modal[5]/div/div/bs-modal-body/div/span").text
        button_ok = super().wait_load_element("/html/body/bs-modal[5]/div/div/bs-modal-footer/div/button")
        button_ok.click()
        Logging().reportDebugStep(self, "Copy secret key")
        return key

    def get_link_api(self):
        sleep(5)
        try:
            api_link = self.driver.find_element(By.XPATH, "//a[@class = 'api-link']").text
        except NoSuchElementException:
            try:
                CRMBasePage(self.driver).refresh_page()
                sleep(1)
                api_link = self.driver.find_element(By.XPATH, "//a[@class = 'api-link']").text
            except NoSuchElementException:
                CRMBasePage(self.driver).refresh_page()
                sleep(1)
                api_link = self.driver.find_element(By.XPATH, "//a[@class = 'api-link']").text
        Logging().reportDebugStep(self, "Get link API")
        return api_link
