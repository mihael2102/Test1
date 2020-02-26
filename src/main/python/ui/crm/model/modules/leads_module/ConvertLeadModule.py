from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from time import sleep


class ConvertLeadModule(CRMBasePage):

    def perform_convert_lead(self, first_name, last_name, email, phone, birthday, citizenship,
                             address, postal_code, city, country, password, currency, referral,
                             brand, source_name, phone_area_code=None):
        sleep(2)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_phone(phone)
        self.set_birthday(birthday)
        self.set_citizenship(citizenship)
        self.set_address(address)
        self.set_postal_code(postal_code)
        self.set_city(city)
        self.set_country(country)
        self.set_password(password)
        self.set_currency(currency)
        self.set_source_name(source_name)
        if referral:
            self.set_referral(referral)
        if brand:
            self.set_brand(brand)
        if phone_area_code:
            self.set_area_code(phone_area_code)
        sleep(1)
        self.click_submit()

    def perform_convert_lead_short(self, first_name, birthday, address, postal_code, city, country):
        sleep(2)
        self.set_first_name(first_name)
        self.set_birthday(birthday)
        self.set_address(address)
        self.set_postal_code(postal_code)
        self.set_city(city)
        self.set_country(country)
        self.click_submit()

    def set_first_name(self, first_name):
        first_name_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                     (self.__class__.__name__)["first_name_field"])
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "First name was set: " + first_name)
        return ConvertLeadModule(self.driver)

    def set_last_name(self, last_name):
        last_name_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                    (self.__class__.__name__)["last_name_field"])
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "last name was set: " + last_name)
        return ConvertLeadModule(self.driver)

    def set_mobile(self, mobile):
        mobile_field = super().wait_load_element("//input[@name='mobile']")
        mobile_field.clear()
        mobile_field.send_keys(mobile)
        Logging().reportDebugStep(self, "Mobile was set: " + mobile)
        return ConvertLeadModule(self.driver)

    def set_email(self, email):
        email_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                ["email_field"])
        try:
            email_field.clear()
            email_field.send_keys(email)
            ConvertLeadConstantsUI.EMAIL_EDITABLE = True
            Logging().reportDebugStep(self, "The email was set to: " + email)
        except:
            ConvertLeadConstantsUI.EMAIL_EDITABLE = False
            Logging().reportDebugStep(self, "The email field is not editable")
        return ConvertLeadModule(self.driver)

    def set_phone(self, phone):
        phone_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                ["phone_field"])
        phone_field.clear()
        phone_field.send_keys(phone)
        Logging().reportDebugStep(self, "The phone number was set: " + phone)
        return ConvertLeadModule(self.driver)

    def set_area_code(self, area_code):
        try:
            area_code_field = super().wait_load_element("//input[@name='account[PhoneAreaCode]']", 1)
            area_code_field.clear()
            area_code_field.send_keys(area_code)
            Logging().reportDebugStep(self, "The phone area code was set: %d" % area_code)
        except (NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Area code input was not found")
        return ConvertLeadModule(self.driver)

    def set_brand(self, brand):
        try:
            brand_list = Select(self.driver.find_element(By.XPATH, "//select[@name='brands']"))
            brand_list.select_by_visible_text(brand)
            Logging().reportDebugStep(self, "The Brand was set: " + brand)
        except:
            first_item = super().wait_load_element(
                "(/html/body/app-root/mat-sidenav-container/mat-sidenav[1]/div/convert-leads/div[2]/form/div[9]/div[1]/nice-select/div/div/ul/li/a/span)[1]")
            self.driver.execute_script("arguments[0].click();", first_item)
            Logging().reportDebugStep(self, "The Brand was set")
        return ConvertLeadModule(self.driver)

    def set_referral(self, referral):
        referral_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                   (self.__class__.__name__)["referral_field"])
        referral_field.clear()
        referral_field.send_keys(referral)
        Logging().reportDebugStep(self, "The referral was set: " + referral)
        return ConvertLeadModule(self.driver)

    def set_postal_code(self, postal_code):
        postal_code_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                      (self.__class__.__name__)["postal_code_field"])
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        Logging().reportDebugStep(self, "The postal code was set: " + postal_code)
        return ConvertLeadModule(self.driver)

    def set_city(self, city):
        city_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                               ["city_field"])
        city_field.clear()
        city_field.send_keys(city)
        Logging().reportDebugStep(self, "The city was set: " + city)
        return ConvertLeadModule(self.driver)

    def set_country(self, country):
        try:
            country_list = Select(self.driver.find_element(By.XPATH, "//select[@name='account[Country]']"))
            country_list.select_by_visible_text(country)
        except:
            country_item = super().wait_load_element("//a[@title='%s']" % country)
            self.driver.execute_script("arguments[0].click();", country_item)
        Logging().reportDebugStep(self, "The country was set: " + country)
        return ConvertLeadModule(self.driver)

    def set_source_name(self, source_name):
        try:
            source_name_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                          (self.__class__.__name__)["source_name_field"])
            source_name_field.clear()
            source_name_field.send_keys(source_name)
            Logging().reportDebugStep(self, "The state was set: " + source_name)
        except (NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Source input was not found")
        return ConvertLeadModule(self.driver)

    def set_birthday(self, birthday):
        try:
            birthday_field = super().wait_load_element("//input[@name='account[Birthday]']", 1)
            birthday_field.clear()
            birthday_field.send_keys(birthday)
            hoverer = ActionChains(self.driver).move_to_element_with_offset(birthday_field, 0, -80).click()
            hoverer.perform()
            Logging().reportDebugStep(self, "The birthday was set: " + birthday)
        except (NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Birthday input was not found")
        return ConvertLeadModule(self.driver)

    def set_address(self, address):
        address_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                  (self.__class__.__name__)["address_field"])
        address_field.clear()
        address_field.send_keys(address)
        Logging().reportDebugStep(self, "The address was set: " + address)
        return ConvertLeadModule(self.driver)

    def set_password(self, password):
        password_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                   (self.__class__.__name__)["password_field"])
        password_field.clear()
        password_field.send_keys(password)
        Logging().reportDebugStep(self, "The password was set: " + password)
        return ConvertLeadModule(self.driver)

    def set_currency(self, currency):
        try:
            currency_list = Select(self.driver.find_element(By.XPATH, "//select[@name='account[Currency]']"))
            currency_list.select_by_visible_text(currency)
        except:
            currency_item = super().wait_load_element("//span[text()='%s']" % currency)
            self.driver.execute_script("arguments[0].click();", currency_item)
        Logging().reportDebugStep(self, "The currency was set: " + currency)
        return ConvertLeadModule(self.driver)

    def click_submit(self):
        convert_lead_btn = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                     (self.__class__.__name__)["convert_lead_btn"])
        try:
            convert_lead_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", convert_lead_btn)
        Logging().reportDebugStep(self, "Click Submit")
        return ConvertLeadModule(self.driver)

    def set_citizenship(self, citizenship):
        try:
            country_list = Select(self.driver.find_element(By.XPATH, "//select[@name='account[Citizenship]']"))
            country_list.select_by_visible_text(citizenship)
            Logging().reportDebugStep(self, "The citizenship was set: " + citizenship)
        except NoSuchElementException:
            Logging().reportDebugStep(self, "Citizenship input was not found")
        return ConvertLeadModule(self.driver)
