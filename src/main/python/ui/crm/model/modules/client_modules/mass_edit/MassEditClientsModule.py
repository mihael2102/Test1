from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class MassEditClientsModule(CRMBasePage):

    def perform_mass_edit(self, gender, assigned_to, client_source, compliance_agent, compliance_notes, client_status,
                          retention_status, description, referral):
        self.set_gender(gender)
        self.set_assigned_to(assigned_to)
        self.set_client_source(client_source)
        self.set_compliance_agent(compliance_agent)
        self.set_compliance_notes(compliance_notes)
        self.set_terms_conditions()
        self.set_client_status(client_status)
        self.set_retention_status(retention_status)
        self.set_description(description)
        self.set_referral(referral)
        return MassEditClientsModule()

    def set_gender(self, gender):
        sleep(3)
        check_box = super().wait_element_to_be_clickable("//div[@id='gender_mass_edit_check']//div[1]")
        check_box.click()
        gender_drop_drown = Select(self.driver.find_element(By.XPATH,"//select[@name='gender']"))
        gender_drop_drown.select_by_visible_text(gender)
        Logging().reportDebugStep(self, "The gender was set: " + gender)
        return MassEditClientsModule()

    def set_assigned_to(self, assigned_to):
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[@id='assigned_user_id_mass_edit_check']//div[1]")
        check_box.click()
        assigned_to_drown = Select(self.driver.find_element(By.XPATH, "//select[@name='assigned_user_id']"))
        assigned_to_drown.select_by_visible_text(assigned_to)
        return MassEditClientsModule()

    def set_client_source(self, client_source):
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[@id='client_source_mass_edit_check']//div[1]")
        check_box.click()
        client_source_field = self.driver.find_element(By.XPATH,
                                                       "//input[@id='client_source']")
        client_source_field.clear()
        client_source_field.send_keys(client_source)
        return MassEditClientsModule()

    def set_compliance_agent(self, compliance_agent):
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[@id='compliance_agent_mass_edit_check']//div[1]")
        check_box.click()
        compliance_agent_drop_down = Select(
            self.driver.find_element(By.XPATH, "//select[@name='compliance_agent_group_id']"))
        compliance_agent_drop_down.select_by_visible_text(compliance_agent)
        return MassEditClientsModule()

    def set_compliance_notes(self, compliance_notes):
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[@id='compliance_note_mass_edit_check']//div[1]")
        check_box.click()
        compliance_notes_field = self.driver.find_element(By.XPATH,
                                                          "//input[@id='compliance_note']")
        compliance_notes_field.clear()
        compliance_notes_field.send_keys(compliance_notes)
        return MassEditClientsModule()

    def set_terms_conditions(self):
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[@id='terms_and_conditions_mass_edit_check']//div[1]")
        check_box.click()
        check_box_confirm = self.driver.find_element(By.XPATH,
                                                     "//div[@name='terms_and_conditions']//div[1]")
        check_box_confirm.click()
        return MassEditClientsModule()

    def set_client_status(self, client_status):
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[@id='accountstatus_mass_edit_check']//div[1]")
        check_box.click()
        client_status_drop_down = Select(self.driver.find_element(By.XPATH, "//select[@name='accountstatus']"))
        client_status_drop_down.select_by_visible_text(client_status)
        Logging().reportDebugStep(self, "The client status was set: " + client_status)
        return MassEditClientsModule()

    def set_retention_status(self, retention_status):
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[@id='retention_status_mass_edit_check']//div[1]")
        check_box.click()
        retention_status_drop_down = Select(self.driver.find_element(By.XPATH, "//select[@name='retention_status']"))
        retention_status_drop_down.select_by_visible_text(retention_status)
        Logging().reportDebugStep(self, "The retention status was set: " + retention_status)
        return MassEditClientsModule()

    def set_description(self, description):
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[@id='client_description_mass_edit_check']//div[1]")
        check_box.click()
        description_field = self.driver.find_element(By.XPATH,
                                                     "//input[@id='client_description']")
        description_field.clear()
        description_field.send_keys(description)
        Logging().reportDebugStep(self, "The description was set: " + description)
        return MassEditClientsModule()

    def set_referral(self, referral):
        check_box = self.driver.find_element(By.XPATH,
                                             "//div[@id='referral_mass_edit_check']//div[1]")
        check_box.click()
        referral_field = self.driver.find_element(By.XPATH,
                                                  "//textarea[@name='referral']")
        referral_field.clear()
        referral_field.send_keys(referral)
        Logging().reportDebugStep(self, "The referral was set: " + referral)
        return MassEditClientsModule()

    def click_save(self):
        save_button = self.driver.find_element(By.XPATH,
                                               "//button[contains(text(),'Save')]")
        save_button.click()
        Logging().reportDebugStep(self, "Save was clicked")
        return MassEditClientsModule()
