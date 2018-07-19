from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class MassEditLeadModule(CRMBasePage):
    def __init__(self):
        super().__init__()

    def perform_mass_edit(self, tittle, lead_source, lead_status, assign_to, language, source_name, referral, country,
                          description):
        self.set_checkbox()
        self.set_tittle(tittle)
        self.set_lead_source(lead_source)
        self.set_lead_status(lead_status)
        self.set_assign_to(assign_to)
        self.set_language(language)
        self.set_source_name(source_name)
        self.set_referral(referral)
        self.set_country(country)
        self.set_description(description)
        self.click_save()
        return MassEditLeadModule()

    def set_language(self, language):
        first_name_field = super().wait_load_element("//input[@name='cf_1092']")
        first_name_field.clear()
        first_name_field.send_keys(language)
        Logging().reportDebugStep(self, "The language  was set: " + language)
        return MassEditLeadModule()

    def set_referral(self, referral):
        referral_field = super().wait_load_element("//textarea[@name='refferal']")
        referral_field.clear()
        referral_field.send_keys(referral)
        Logging().reportDebugStep(self, "The referral was set: " + referral)
        return MassEditLeadModule()

    def set_country(self, country):
        country_list = Select(self.driver.find_element(By.XPATH, "//select[@name='country']"))
        country_list.select_by_visible_text(country)
        Logging().reportDebugStep(self, "The country was set: " + country)
        return MassEditLeadModule()

    def set_tittle(self, tittle):
        time_element = self.driver.find_element(By.XPATH, "//input[@id='designation']")
        time_element.clear()
        time_element.send_keys(tittle)
        Logging().reportDebugStep(self, "the tittle ws set" + tittle)
        return MassEditLeadModule()

    def set_event_type(self, type):
        type_element = self.driver.find_element(By.XPATH, "//select[@id='activitytype']")
        select = Select(type_element)
        select.select_by_visible_text(type)
        Logging().reportDebugStep(self, "The event type is set " + type)
        return MassEditLeadModule()

    def set_source_name(self, source_name):
        source_name_field = super().wait_load_element("//input[@name='sourcename']")
        source_name_field.clear()
        source_name_field.send_keys(source_name)
        Logging().reportDebugStep(self, "The source name was set: " + source_name)
        return MassEditLeadModule()

    def set_duration(self, duration):
        duration_element = self.driver.find_element(By.XPATH, "//select[@id='duration_minutes']")
        select = Select(duration_element)
        select.select_by_visible_text(duration)
        Logging().reportDebugStep(self, "The duration  is set " + duration)
        return MassEditLeadModule()

    def set_priority(self, priority):
        priority_element = super().wait_element_to_be_clickable("//select[@id='priority']")
        select = Select(priority_element)
        select.select_by_visible_text(priority)
        Logging().reportDebugStep(self, "The priority is set " + priority)
        return MassEditLeadModule()

    def set_assign_to(self, assign_to):
        assign_to_element = self.driver.find_element(By.XPATH, "//select[@name='assigned_user_id']")
        select = Select(assign_to_element)
        select.select_by_visible_text(assign_to)
        Logging().reportDebugStep(self, "The assign to is set " + assign_to)
        return MassEditLeadModule()

    def set_description(self, comments):
        description_element = self.driver.find_element(By.XPATH, "//textarea[@name='description']")
        description_element.clear()
        description_element.send_keys(comments)
        Logging().reportDebugStep(self, "The comments is set " + comments)
        return MassEditLeadModule()

    def set_lead_source(self, lead_source):
        lead_source_list = Select(self.driver.find_element(By.XPATH, "//select[@name='leadsource']"))
        lead_source_list.select_by_visible_text(lead_source)
        Logging().reportDebugStep(self, "The lead source was set: " + lead_source)
        return MassEditLeadModule()

    def set_lead_status(self, lead_status):
        lead_source_list = Select(self.driver.find_element(By.XPATH, "//select[@name='leadstatus']"))
        lead_source_list.select_by_visible_text(lead_status)
        Logging().reportDebugStep(self, "The lead status was set: " + lead_status)
        return MassEditLeadModule()

    def click_save(self):
        save_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        save_button.click()
        Logging().reportDebugStep(self, "Click the 'save' button ")
        return MassEditLeadModule()

    def set_checkbox(self):
        sleep(3)
        event_type_check_box = super().wait_load_element(
            "//label[contains(text(),'Title')]//preceding-sibling::div")
        event_type_check_box.click()

        time_date_check_box = self.driver.find_element(By.XPATH,
                                                       "//label[contains(text(),'Lead Source')]//preceding-sibling::div")
        time_date_check_box.click()

        duration_check_box = self.driver.find_element(By.XPATH,
                                                      "//label[contains(text(),'Assigned To')]//preceding-sibling::div")
        duration_check_box.click()

        lead_status_check_box = self.driver.find_element(By.XPATH,
                                                         "//label[contains(text(),'Lead Status')]//preceding-sibling::div")
        lead_status_check_box.click()

        priority_check_box = self.driver.find_element(By.XPATH,
                                                      "//label[contains(text(),'Language')]//preceding-sibling::div")
        priority_check_box.click()

        assign_to_check_box = self.driver.find_element(By.XPATH,
                                                       "//label[contains(text(),'Source Name')]//preceding-sibling::div")
        assign_to_check_box.click()

        comments_to_check_box = self.driver.find_element(By.XPATH,
                                                         "//label[contains(text(),'Refferal')]//preceding-sibling::div")
        comments_to_check_box.click()

        country_check_box = self.driver.find_element(By.XPATH,
                                                     "//label[contains(text(),'Country')]//preceding-sibling::div")
        country_check_box.click()

        country_check_box = self.driver.find_element(By.XPATH,
                                                     "//label[contains(text(),'Description')]//preceding-sibling::div")
        country_check_box.click()

        return MassEditLeadModule()
