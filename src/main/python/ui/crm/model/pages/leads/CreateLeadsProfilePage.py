from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class CreateLeadsProfilePage(CRMBasePage):

    def perform_create_lead(self, first_name, last_name, mobile, fax, email, secondary_email, language,
                            panda_partner_id, referral, street, postal_code, country, description, phone, tittle,
                            lead_source, lead_status, assigned_to, source_name, brand, po_box, city, state):
        sleep(2)
        if first_name:
            self.set_first_name(first_name)
        if last_name:
            self.set_last_name(last_name)
        if mobile:
            self.set_mobile(mobile)
        if fax:
            self.set_fax(fax)
        if email:
            self.set_email(email)
        if secondary_email:
            self.set_secondary_email(secondary_email)
        if language:
            self.set_language(language)
        if panda_partner_id:
            self.set_panda_partner_id(panda_partner_id)
        if referral:
            self.set_referral(referral)
        if street:
            self.set_street(street)
        if postal_code:
            self.set_postal_code(postal_code)
        if country:
            self.set_country(country)
        if description:
            self.set_description(description)
        if phone:
            self.set_phone(phone)
        if tittle:
            self.set_tittle(tittle)
        if lead_source:
            self.set_lead_source(lead_source)
        if lead_status:
            self.set_lead_status(lead_status)
        if assigned_to:
            self.set_assigned_to(assigned_to)
        if source_name:
            self.set_source_name(source_name)
        if brand:
            self.set_brand(brand)
        else:
            self.set_first_brand()
        if po_box:
            self.set_po_box(po_box)
        if city:
            self.set_city(city)
        if state:
            self.set_state(state)
        self.click_save()

    def perform_create_lead_new(self, first_name, last_name, mobile, fax, email, secondary_email, referral, street,
                                postal_code, country, description, phone, tittle, lead_source, lead_status, assigned_to,
                                po_box, city, state):
        sleep(2)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_mobile(mobile)
        self.set_fax(fax)
        self.set_email(email)
        self.set_secondary_email(secondary_email)
        if referral:
            self.set_referral(referral)
        self.set_street(street)
        self.set_postal_code(postal_code)
        self.set_country(country)
        self.set_description(description)
        self.set_phone(phone)
        self.set_tittle(tittle)
        self.set_lead_source(lead_source)
        self.set_lead_status(lead_status)
        self.set_assigned_to(assigned_to)
        self.set_po_box(po_box)
        self.set_city(city)
        self.set_state(state)
        self.click_save()

    def perform_create_lead_short(self, last_name, email, assigned_to, phone):
        sleep(2)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_phone(phone)
        self.set_assigned_to(assigned_to)
        self.click_save()

    def set_first_name(self, first_name):
        first_name_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                     (self.__class__.__name__)["first_name_field"])
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "First name was set: " + first_name)
        return CreateLeadsProfilePage(self.driver)

    def set_last_name(self, last_name):
        last_name_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["last_name_field"])
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "Last name was set: " + last_name)
        return CreateLeadsProfilePage(self.driver)

    def set_mobile(self, mobile):
        sleep(0.1)
        mobile_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                 ["mobile_field"])
        mobile_field.clear()
        mobile_field.send_keys(mobile)
        Logging().reportDebugStep(self, "Mobile was set: " + mobile)
        return CreateLeadsProfilePage(self.driver)

    def set_fax(self, fax):
        fax_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                              ["fax_field"])
        fax_field.clear()
        fax_field.send_keys(fax)
        Logging().reportDebugStep(self, "Fax was set: " + fax)
        return CreateLeadsProfilePage(self.driver)

    def set_email(self, email):
        email_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                ["email_field"])
        email_field.clear()
        email_field.send_keys(email)
        Logging().reportDebugStep(self, "The email was set: " + email)
        return CreateLeadsProfilePage(self.driver)

    def set_secondary_email(self, secondary_email):
        secondary_email_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                          (self.__class__.__name__)["secondary_email_field"])
        secondary_email_field.clear()
        secondary_email_field.send_keys(secondary_email)
        Logging().reportDebugStep(self, "The secondary email was set: " + secondary_email)
        return CreateLeadsProfilePage(self.driver)

    def set_language(self, language):
        language_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                   (self.__class__.__name__)["language_field"])
        language_field.clear()
        language_field.send_keys(language)
        Logging().reportDebugStep(self, "The language was set: " + language)
        return CreateLeadsProfilePage(self.driver)

    def set_panda_partner_id(self, partner_id):
        sleep(0.1)
        panda_partner_id_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                           (self.__class__.__name__)["panda_partner_id_field"])
        panda_partner_id_field.clear()
        panda_partner_id_field.send_keys(partner_id)
        Logging().reportDebugStep(self, "The panda partner id was set: " + partner_id)
        return CreateLeadsProfilePage(self.driver)

    def set_phone(self, phone):
        phone_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                ["phone_field"])
        phone_field.clear()
        phone_field.send_keys(phone)
        Logging().reportDebugStep(self, "The phone number was set: " + phone)
        return CreateLeadsProfilePage(self.driver)

    def set_tittle(self, tittle):
        tittle_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                 ["tittle_field"])
        tittle_field.clear()
        tittle_field.send_keys(tittle)
        Logging().reportDebugStep(self, "The tittle was set: " + tittle)
        return CreateLeadsProfilePage(self.driver)

    def set_lead_source(self, lead_source):
        try:
            lead_source_list = Select(self.driver.find_element(By.XPATH, "//select[@name='leadsource']"))
            lead_source_list.select_by_visible_text(lead_source)
        except:
            lead_source_item = super().wait_load_element("(//ul/li/a[@title='%s'])[1]" % lead_source)
            self.driver.execute_script("arguments[0].click();", lead_source_item)
        Logging().reportDebugStep(self, "The lead source was set: " + lead_source)
        return CreateLeadsProfilePage(self.driver)

    def set_lead_status(self, lead_status):
        try:
            lead_source_list = Select(self.driver.find_element(By.XPATH, "//select[@name='leadstatus']"))
            lead_source_list.select_by_visible_text(lead_status)
        except:
            lead_source_item = super().wait_load_element("//ul/li/a[@title='%s']" % lead_status)
            self.driver.execute_script("arguments[0].click();", lead_source_item)
        Logging().reportDebugStep(self, "The lead status was set: " + lead_status)
        return CreateLeadsProfilePage(self.driver)

    def set_assigned_to(self, assigned_to):
        try:
            assigned_to_list = Select(self.driver.find_element(By.XPATH, "//select[@name='assigned_user_id']"))
            assigned_to_list.select_by_visible_text(assigned_to)
        except:
            assigned_to_item = super().wait_load_element("(//ul/li/a[@title='%s'])[1]" % assigned_to)
            self.driver.execute_script("arguments[0].click();", assigned_to_item)
        Logging().reportDebugStep(self, "The assigned_to was set: " + assigned_to)
        return CreateLeadsProfilePage(self.driver)

    def set_source_name(self, source_name):
        source_name_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                      (self.__class__.__name__)["source_name_field"])
        source_name_field.clear()
        source_name_field.send_keys(source_name)
        Logging().reportDebugStep(self, "The source name was set: " + source_name)
        return CreateLeadsProfilePage(self.driver)

    def set_brand(self, brand):
        brand_list = Select(self.driver.find_element(By.XPATH, "//select[@name='brands']"))
        brand_list.select_by_visible_text(brand)
        Logging().reportDebugStep(self, "The brand was set: " + brand)
        return CreateLeadsProfilePage(self.driver)

    def set_first_brand(self):
        try:
            brand_list = Select(self.driver.find_element(By.XPATH, "//select[@name='brands']"))
            brand_list.select_by_index(1)
            Logging().reportDebugStep(self, "The lead status was set to the first brand")
        except NoSuchElementException:
            Logging().reportDebugStep(self, "Brand select box was not found")
        return CreateLeadsProfilePage(self.driver)

    def set_referral(self, referral):
        referral_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                   (self.__class__.__name__)["referral_field"])
        referral_field.clear()
        referral_field.send_keys(referral)
        Logging().reportDebugStep(self, "The referral was set: " + referral)
        return CreateLeadsProfilePage(self.driver)

    def set_street(self, street):
        street_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                                 ["street_field"])
        street_field.clear()
        street_field.send_keys(street)
        Logging().reportDebugStep(self, "The street name was set: " + street)
        return CreateLeadsProfilePage(self.driver)

    def set_po_box(self, pobox):
        pobox_field = super().wait_load_element("//input[@name='pobox']")
        pobox_field.clear()
        pobox_field.send_keys(pobox)
        Logging().reportDebugStep(self, "The po box was set: " + pobox)
        return CreateLeadsProfilePage(self.driver)

    def set_postal_code(self, postal_code):
        postal_code_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                      (self.__class__.__name__)["postal_code_field"])
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        Logging().reportDebugStep(self, "The postal code was set: " + postal_code)
        return CreateLeadsProfilePage(self.driver)

    def set_city(self, city):
        city_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element(self.__class__.__name__)
                                               ["city_field"])
        city_field.clear()
        city_field.send_keys(city)
        Logging().reportDebugStep(self, "The city was set: " + city)
        return CreateLeadsProfilePage(self.driver)

    def set_country(self, country):
        try:
            country_list = Select(self.driver.find_element(By.XPATH, "//select[@name='country']"))
            country_list.select_by_visible_text(country)
        except:
            country_item = super().wait_load_element("(//span[text()='%s'])[1]" % country)
            self.driver.execute_script("arguments[0].click();", country_item)
        Logging().reportDebugStep(self, "The country was set: " + country)
        return CreateLeadsProfilePage(self.driver)

    def set_description(self, description):
        description_field = super().wait_load_element(global_var.get_xpath_for_current_brand_element
                                                      (self.__class__.__name__)["description_field"])
        description_field.clear()
        description_field.send_keys(description)
        Logging().reportDebugStep(self, "The description was set: " + description)
        return CreateLeadsProfilePage(self.driver)

    def set_state(self, state):
        state_field = super().wait_load_element("//input[@name='state']")
        state_field.clear()
        state_field.send_keys(state)
        Logging().reportDebugStep(self, "The state was set: " + state)
        return CreateLeadsProfilePage(self.driver)

    def click_save(self):
        save_button = self.driver.find_element(By.XPATH, global_var.get_xpath_for_current_brand_element
                                                (self.__class__.__name__)["save_button"])
        self.perform_scroll_up()
        save_button.click()
        Logging().reportDebugStep(self, "The Save button was clicked")
        return CreateLeadsProfilePage(self.driver)

    def verify_success_message(self):
        message = super().wait_load_element("//div[@class='dialog-content-success mat-dialog-content']").text
        assert "success" in message.lower()
        Logging().reportDebugStep(self, "Get message: " + message)
        return CreateLeadsProfilePage(self.driver)
