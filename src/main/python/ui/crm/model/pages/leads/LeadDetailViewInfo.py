import re

from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.leads_module.LeadViewInfo import LeadViewInfo
from src.main.python.ui.crm.model.pages.leads.EditLeadsProfilePage import EditLeadsProfilePage
from src.main.python.utils.logs.Loging import Logging


class LeadDetailViewInfo(CRMBasePage):



    def click_delete_button(self):
        task_module = super().wait_load_element("//input[@name='Delete']")
        task_module.click()
        Logging().reportDebugStep(self, "The delete pop-up is displayed")
        return LeadViewInfo()

    def open_edit_lead_profile(self):
        task_module = super().wait_load_element("//input[@name='Edit']")
        task_module.click()
        Logging().reportDebugStep(self, "The delete pop-up is displayed")
        return EditLeadsProfilePage(self.driver)

    '''
        Returns the first name
    '''

    def get_first_name_text(self):
        first_name = self.driver.find_element(By.XPATH, "//td[contains(text(),'First Name')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the first name: " + first_name.text)
        return first_name.text

    '''
        Returns the first name
    '''

    def get_last_name_text(self):
        last_name = self.driver.find_element(By.XPATH, "//td[contains(text(),'Last Name')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the last_name: " + last_name.text)
        return last_name.text

    '''
        Returns the mobile
    '''

    def get_mobile_text(self):
        phone = self.driver.find_element(By.XPATH, "//td[contains(text(),'Mobile')]//following-sibling::td[1]")
        parser_phone_text = re.sub('[+," "]', '', phone.text)
        Logging().reportDebugStep(self, "Returns the mobile text: " + parser_phone_text)
        return parser_phone_text

    '''
        Returns the fax
    '''

    def get_fax_text(self):
        fax_name = self.driver.find_element(By.XPATH, "//td[contains(text(),'Fax')]//following-sibling::td[1]")
        parser_fax_text = re.sub('[+," "]', '', fax_name.text)
        Logging().reportDebugStep(self, "Returns the fax text: " + parser_fax_text)
        return parser_fax_text

    '''
        Returns the email
    '''

    def get_email_text(self):
        fax_name = self.driver.find_element(By.XPATH, "//td[contains(text(),'Email')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the email text: " + fax_name.text)
        return fax_name.text

    '''
        Returns the secondary email
    '''

    def get_secondary_email_text(self):
        secondary_email = self.driver.find_element(By.XPATH,
                                                   "//td[contains(text(),'Secondary Email')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the secondary email: " + secondary_email.text)
        return secondary_email.text

    '''
        Returns the source name
    '''

    def get_source_name_text(self):
        source_name = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Source Name')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the source name_: " + source_name.text)
        return source_name.text

    '''
        Returns the panda_partner
    '''

    def get_panda_partner_id_text(self):
        panda_partner = self.driver.find_element(By.XPATH,
                                                 "//td[contains(text(),'Panda Partner ID')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the panda partner: " + panda_partner.text)
        return panda_partner.text

    '''
        Returns the referral text
    '''

    def get_referral_text(self):
        referral = self.driver.find_element(By.XPATH,
                                            "//td[contains(text(),'Referral')]//following-sibling::td[1]")

        parser_referral_text = re.sub('[" "]', '', referral.text, 2)

        Logging().reportDebugStep(self, "Returns the referral text: " + parser_referral_text)
        return parser_referral_text

    '''
        Returns the  street text
    '''

    def get_street_text(self):
        street_text = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Street')]//following-sibling::td[1]")
        parser_street_text = re.sub('[" "]', '', street_text.text, 1)
        Logging().reportDebugStep(self, "Returns the street text: " + parser_street_text)
        return parser_street_text

    '''
        Returns the street text
    '''

    def get_postal_code_text(self):
        postal_code = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Postal Code')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the postal code: " + postal_code.text)
        return postal_code.text

    '''
        Returns the country text
    '''

    def get_country_text(self):
        country = self.driver.find_element(By.XPATH,
                                           "//td[contains(text(),'Country')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the postal code: " + country.text)
        return country.text

    '''
        Returns the country text
    '''

    def get_description_text(self):
        description = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Description')]//following-sibling::td[1]")
        parser_description_text = re.sub('[" "]', '', description.text, 2)
        Logging().reportDebugStep(self, "Returns the description text: " + parser_description_text)
        return parser_description_text

    '''
        Returns the phone text
    '''

    def get_phone_text(self):
        phone = self.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'Phone')]//following-sibling::td[1]")
        parser_phone_text = re.sub('[+," "]', '', phone.text)
        Logging().reportDebugStep(self, "Returns the description text: " + parser_phone_text)
        return parser_phone_text

    '''
         Returns the title text
    '''

    def get_tittle_text(self):
        title = self.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'Title')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the description text: " + title.text)
        return title.text

    '''
         Returns the lead source text
    '''

    def get_lead_source_text(self):
        lead_source = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Lead Source')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the description text: " + lead_source.text)
        return lead_source.text

    '''
        Returns the lead source text
    '''

    def get_lead_status_text(self):
        lead_status = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Lead Status')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the lead status text: " + lead_status.text)
        return lead_status.text

    '''
        Returns the lead source text
    '''

    def get_assigned_to_text(self):
        assigned_to = self.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'Assigned To')]//following-sibling::td[1]")
        parser_assigned_to_text = re.sub('[" "]', '', assigned_to.text, 2)

        Logging().reportDebugStep(self, "Returns the assigned to text: " + parser_assigned_to_text)
        return parser_assigned_to_text

    '''
         Returns the language text
     '''

    def get_language_text(self):
        language = self.driver.find_element(By.XPATH,
                                            "//td[contains(text(),'Language')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the language text: " + language.text)
        return language.text

    '''
        Returns the language text
    '''

    def get_brand_text(self):
        brand = self.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'Brand')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the language text: " + brand.text)
        return brand.text

    '''
        Returns the language text
    '''

    def get_po_box_text(self):
        po_box = self.driver.find_element(By.XPATH,
                                          "//td[contains(text(),'PO Box')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the language text: " + po_box.text)
        return po_box.text

    '''
        Returns the language text
    '''

    def get_city_text(self):
        city = self.driver.find_element(By.XPATH,
                                        "//td[contains(text(),'City')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the language text: " + city.text)
        return city.text

    '''
         Returns the state text
     '''

    def get_state_text(self):
        state = self.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'State')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the language text: " + state.text)
        return state.text

    def get_exists_text(self):
        exists = self.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'Exists')]//following-sibling::td[1]")
        Logging().reportDebugStep(self, "Returns the exists text: " + exists.text)
        return exists.text
