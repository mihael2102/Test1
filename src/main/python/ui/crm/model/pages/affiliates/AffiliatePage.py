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
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage


class AffiliatePage(CRMBasePage):

    def click_submit(self):
        sleep(3)
        submit = self.driver.find_element(By.XPATH,
                                          "/html/body/bs-modal[3]/div/div/form/bs-modal-footer/div/button[3]")
        submit.click()
        Logging().reportDebugStep(self, "click submit")
        return AffiliatePage(self.driver)

    def add_none_selected_countries(self):
        sleep(3)
        methods = super().wait_element_to_be_clickable(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[5]/div[2]/filter-multi-select/div/div[1]/span")
        methods.click()
        sleep(2)
        all_methods = super().wait_element_to_be_clickable(
            "/html/body/bs-modal[3]/div/div/form/bs-modal-body/div/div[5]/div[2]/filter-multi-select/div/div[2]/span[2]")
        all_methods.click()
        # sleep(4)
        # all_methods.click()
        Logging().reportDebugStep(self, "None selected countries")
        return AffiliatePage(self.driver)

    def check_selected_countries(self):
        sleep(3)
        selected_number = super().wait_load_element(
            "(//div[@class='multi-select-title']/span[contains(text(),'elected')])[2]").text
        Logging().reportDebugStep(self, "Check selected blocked countries")
        return selected_number

    def click_cancel(self):
        cancel = super().wait_load_element("/html/body/bs-modal[3]/div/div/form/bs-modal-footer/div/button[2]")
        cancel.click()
        Logging().reportDebugStep(self, "Click cancel")
        return AffiliatePage(self.driver)

    def check_selected_methods(self):
        sleep(3)
        selected_number = super().wait_load_element(
            "(//div[@class='multi-select-title']/span[contains(text(),'elected')])[1]").text
        Logging().reportDebugStep(self, "Check selected methods")
        return selected_number

    def search_by_partner_id(self, partner_id):
        sleep(2)
        input = self.driver.find_element(By.XPATH, "//*[@id='host-element']/input")
        input.send_keys(partner_id)
        Logging().reportDebugStep(self, "Enter partner ID %s" % partner_id)
        return AffiliatePage(self.driver)

    def open_edit_affiliate(self):
        sleep(3)
        edit_button = self.driver.find_element(By.XPATH, "//span[contains(@class,'pencil')]")
        edit_button.click()
        Logging().reportDebugStep(self, "Click Edit affiliate")
        return AffiliatePage(self.driver)

    def add_all_methods(self):
        sleep(3)
        methods = super().wait_element_to_be_clickable(
            "(//div[@class='multi-select-title']/span[contains(text(),'elected')])[1]")
        methods.click()
        sleep(2)
        all_methods = super().wait_element_to_be_clickable(
            "(//span[contains(@class,'selectAll')]/i)[1]")
        all_methods.click()
        sleep(4)
        all_methods.click()
        Logging().reportDebugStep(self, "Select all methods")
        return AffiliatePage(self.driver)

    def copy_secret_key(self):
        sleep(5)
        copy_button = super().wait_element_to_be_clickable("//button[contains(text(), 'Copy')]")
        self.driver.execute_script("arguments[0].click();", copy_button)
        sleep(3)
        key = super().wait_load_element("//div[@class='modal-body']/span").text
        button_ok = super().wait_load_element("//div[@class='modal-footer']/button[text()='OK']")
        button_ok.click()
        Logging().reportDebugStep(self, "Copy key")
        return key

    def get_link_api(self):
        sleep(5)
        try:
            api_link = self.driver.find_element(By.XPATH, "//a[contains(@id,'api-link')]").text
        except NoSuchElementException:
            try:
                CRMBasePage(self.driver).refresh_page()
                sleep(1)
                api_link = self.driver.find_element(By.XPATH, "//a[contains(@id,'api-link')]").text
            except NoSuchElementException:
                CRMBasePage(self.driver).refresh_page()
                sleep(1)
                api_link = self.driver.find_element(By.XPATH, "//a[contains(@id,'api-link')]").text
        Logging().reportDebugStep(self, "Get link API")
        return api_link

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
        # select_drop_down_brand = Select(super().wait_element_to_be_clickable("//*[@id='brand']"))
        # select_drop_down_brand.select_by_visible_text()
        # Logging().reportDebugStep(self, "")

    def enter_allowed_ip(self, allowed_ip):
        input_ip = super().wait_load_element("//*[@id='allowedIps']")
        input_ip.send_keys(allowed_ip)
        Logging().reportDebugStep(self, "Enter allowed IP: " + allowed_ip)

    def click_plus_ip(self):
        sleep(5)
        button_plus = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element
                                                           (self.__class__.__name__)["button_plus"])
        sleep(1)
        button_plus.click()
        Logging().reportDebugStep(self, "Click plus ip")

    def select_allowed_methods(self, method):
        sleep(1)
        methods_drop_down = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                      (self.__class__.__name__)["methods_drop_down"])
        methods_drop_down.click()
        sleep(2)
        input_methods = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                  (self.__class__.__name__)["input_methods"])
        input_methods.send_keys(method)
        sleep(2)
        methods = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                            ["methods"] % method)
        methods.click()
        Logging().reportDebugStep(self, "Select allowed methods %s" % method)

    def select_blocked_country(self, country):
        country_drop_down = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                      (self.__class__.__name__)["blocked_country_drop_down"])
        country_drop_down.click()
        sleep(2)
        input_country = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                  (self.__class__.__name__)["input_country"])
        input_country.send_keys(country)
        sleep(5)
        countrys = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element
                                            (self.__class__.__name__)["countrys"] % country)
        sleep(2)
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
        Logging().reportDebugStep(self, "Search by Partner Name: " + name)

    def click_on_affiliate(self, name):
        sleep(2)
        affiliate_name = super().wait_load_element("//a[contains(text(), '%s')]" % name)
        affiliate_name.click()
        Logging().reportDebugStep(self, "Go to affiliate details page")

    def check_name_on_affiliate_details(self):
        sleep(2)
        title_details = super().wait_load_element("//h1[@class='affiliate-header-sign']").text
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

    def delete_affiliate(self):
        sleep(2)
        trash_button = super().wait_element_to_be_clickable(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)["trash_button"])
        sleep(1)
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
        # submit = super().wait_element_to_be_clickable("/html/body/bs-modal[3]/div/div/form/bs-modal-footer/div/button[3]")
        # submit.click()
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
        # sleep(4)
        # all_methods.click()
        Logging().reportDebugStep(self, "None selected countries")
        return AffiliatePage(self.driver)

    def copy_secret_key(self):
        sleep(5)
        copy_button = super().wait_element_to_be_clickable("//button[contains(text(), 'Copy')]")
        # copy_button.click()
        self.driver.execute_script("arguments[0].click();", copy_button)
        sleep(3)
        key = super().wait_load_element("/html/body/bs-modal[5]/div/div/bs-modal-body/div/span").text
        button_ok = super().wait_load_element("/html/body/bs-modal[5]/div/div/bs-modal-footer/div/button")
        button_ok.click()
        Logging().reportDebugStep(self, "Copy key")
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
        # api_link.click()
        Logging().reportDebugStep(self, "Get link API")
        return api_link



