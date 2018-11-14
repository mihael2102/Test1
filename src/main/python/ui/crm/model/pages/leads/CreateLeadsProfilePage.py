from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class CreateLeadsProfilePage(CRMBasePage):

    def perform_create_lead(self, first_name, last_name, mobile, email,  country,
                            phone, lead_status, assigned_to,  brand):
        # sleep(2)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_mobile(mobile)

        self.set_email(email)

        self.set_country(country)

        self.set_phone(phone)

        self.set_lead_status(lead_status)
        self.set_assigned_to(assigned_to)

        if brand:
            self.set_brand(brand)
        else:
            self.set_first_brand()
        self.click_save()


    def perform_create_lead_new(self, first_name, last_name, mobile, email, country,
                            phone, lead_status, assigned_to):
        # sleep(2)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_mobile(mobile)
        self.set_email(email)
        self.set_country(country)
        self.set_phone(phone)
        self.set_lead_status(lead_status)
        self.set_assigned_to(assigned_to)
        self.click_save()

    def set_first_name(self, first_name):
        first_name_field = super().wait_load_element("//input[@name='firstname']")
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "First name was set: " + first_name)
        return CreateLeadsProfilePage(self.driver)

    def set_last_name(self, last_name):
        last_name_field = super().wait_load_element("//input[@name='lastname']")
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "last name was set: " + last_name)
        return CreateLeadsProfilePage(self.driver)

    def set_mobile(self, mobile):
        mobile_field = super().wait_load_element("//input[@name='mobile']")
        mobile_field.clear()
        mobile_field.send_keys(mobile)
        Logging().reportDebugStep(self, "Mobile was set: " + mobile)
        return CreateLeadsProfilePage(self.driver)

    def set_fax(self, fax):
        first_name_field = super().wait_load_element("//input[@name='fax']")
        first_name_field.clear()
        first_name_field.send_keys(fax)
        Logging().reportDebugStep(self, "fax was set: " + fax)
        return CreateLeadsProfilePage(self.driver)

    def set_email(self, email):
        email_field = super().wait_load_element("//input[@name='email']")
        email_field.clear()
        email_field.send_keys(email)
        Logging().reportDebugStep(self, "The first name was set: " + email)
        return CreateLeadsProfilePage(self.driver)

    def set_secondary_email(self, secondary_email):
        secondary_email_field = super().wait_load_element("//input[@name='secondaryemail']")
        secondary_email_field.clear()
        secondary_email_field.send_keys(secondary_email)
        Logging().reportDebugStep(self, "The secondary email was set: " + secondary_email)
        return CreateLeadsProfilePage(self.driver)

    def set_language(self, language):
        first_name_field = super().wait_load_element("//input[@name='cf_1092']")
        first_name_field.clear()
        first_name_field.send_keys(language)
        Logging().reportDebugStep(self, "The language  was set: " + language)
        return CreateLeadsProfilePage(self.driver)

    def set_panda_partner_id(self, partner_id):
        panda_partner_id_field = super().wait_load_element("//input[@name='pandapartnerid']")
        panda_partner_id_field.clear()
        panda_partner_id_field.send_keys(partner_id)
        Logging().reportDebugStep(self, "The panda partner id was set: " + partner_id)
        return CreateLeadsProfilePage(self.driver)

    def set_phone(self, phone):
        phone_field = super().wait_load_element("//input[@name='phone']")
        phone_field.clear()
        phone_field.send_keys(phone)
        Logging().reportDebugStep(self, "The phone number was set: " + phone)
        return CreateLeadsProfilePage(self.driver)

    def set_tittle(self, tittle):
        tittle_field = super().wait_load_element("//input[@name='designation']")
        tittle_field.clear()
        tittle_field.send_keys(tittle)
        Logging().reportDebugStep(self, "The tittle was set: " + tittle)
        return CreateLeadsProfilePage(self.driver)

    def set_lead_source(self, lead_source):
        lead_source_list = Select(self.driver.find_element(By.XPATH, "//select[@name='leadsource']"))
        lead_source_list.select_by_visible_text(lead_source)
        Logging().reportDebugStep(self, "The lead source was set: " + lead_source)
        return CreateLeadsProfilePage(self.driver)

    def set_lead_status(self, lead_status):
        lead_source_list = Select(self.driver.find_element(By.XPATH, "//select[@name='leadstatus']"))
        lead_source_list.select_by_visible_text(lead_status)
        Logging().reportDebugStep(self, "The lead status was set: " + lead_status)
        return CreateLeadsProfilePage(self.driver)

    def set_assigned_to(self, assigned_to):
        assigned_to_list = Select(self.driver.find_element(By.XPATH, "//select[@name='assigned_user_id']"))
        assigned_to_list.select_by_visible_text(assigned_to)
        Logging().reportDebugStep(self, "The lead status was set: " + assigned_to)
        return CreateLeadsProfilePage(self.driver)

    def set_source_name(self, source_name):
        source_name_field = super().wait_load_element("//input[@name='sourcename']")
        source_name_field.clear()
        source_name_field.send_keys(source_name)
        Logging().reportDebugStep(self, "The source name was set: " + source_name)
        return CreateLeadsProfilePage(self.driver)

    def set_brand(self, brand):
        brand_list = Select(self.driver.find_element(By.XPATH, "//select[@name='brands']"))
        brand_list.select_by_visible_text(brand)
        Logging().reportDebugStep(self, "The lead status was set: " + brand)
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
        referral_field = super().wait_load_element("//textarea[@name='refferal']")
        referral_field.clear()
        referral_field.send_keys(referral)
        Logging().reportDebugStep(self, "The referral was set: " + referral)
        return CreateLeadsProfilePage(self.driver)

    def set_street(self, street):
        street_field = super().wait_load_element("//textarea[@name='lane']")
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
        first_name_field = super().wait_load_element("//input[@name='code']")
        first_name_field.clear()
        first_name_field.send_keys(postal_code)
        Logging().reportDebugStep(self, "The postal code was set: " + postal_code)
        return CreateLeadsProfilePage(self.driver)

    def set_city(self, city):
        first_name_field = super().wait_load_element("//input[@name='city']")
        first_name_field.clear()
        first_name_field.send_keys(city)
        Logging().reportDebugStep(self, "The city was set: " + city)
        return CreateLeadsProfilePage(self.driver)

    def set_country(self, country):
        country_list = Select(self.driver.find_element(By.XPATH, "//select[@name='country']"))
        country_list.select_by_visible_text(country)
        Logging().reportDebugStep(self, "The country was set: " + country)
        return CreateLeadsProfilePage(self.driver)

    def set_description(self, description):
        description_field = super().wait_load_element("//textarea[@name='description']")
        description_field.clear()
        description_field.send_keys(description)
        Logging().reportDebugStep(self, "The description was set: " + description)
        return CreateLeadsProfilePage(self.driver)

    def set_state(self, state):
        description_field = super().wait_load_element("//input[@name='state']")
        description_field.clear()
        description_field.send_keys(state)
        Logging().reportDebugStep(self, "The state was set: " + state)
        return CreateLeadsProfilePage(self.driver)

    def click_save(self):
        save_button = super().wait_load_element("//input[@title='Save [Alt+S]']")
        self.perform_scroll_up()
        save_button.click()
        Logging().reportDebugStep(self, "The save button was clicked: ")
        Logging().reportDebugStep(self, "The lead was created: ")
        return CreateLeadsProfilePage(self.driver)
