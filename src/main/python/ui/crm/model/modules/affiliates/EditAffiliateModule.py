from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from selenium.webdriver.support.ui import Select
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC


class EditAffiliateModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def perform_edit_affiliate(self, partner_name, brand, allowed_ip, is_enabled, added_allowed_method_1,
                               edited_country_1):

        self.edit_partner_name(partner_name)
        self.edit_brand(brand)
        self.edit_allowed_ip(allowed_ip)
        self.edit_is_enabled_radio_button(is_enabled)
        self.edit_allowed_methods(added_allowed_method_1)

        self.edit_countries(edited_country_1)
        self.click_submit()
        Logging().reportDebugStep(self, "Existed affiliate was edited")

    def edit_partner_name(self, partner_name):
        partner_name_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='partnerName']")))
        partner_name_field.clear()
        partner_name_field.send_keys(partner_name)
        Logging().reportDebugStep(self, "Partner name was edited: " + partner_name)
        return EditAffiliateModule()

    """Leave without the changes because second brand doesn't have allowed methods"""
    def edit_brand(self, brand):
    #     select = Select(self.driver.find_element(By.ID, "brand"))
    #     select.select_by_visible_text(brand)
    #     Logging().reportDebugStep(self, "The brand was selected: " + brand)
        return EditAffiliateModule()

    def edit_allowed_ip(self, ip_value):
        """Delete old IP"""
        allowed_ip_field = self.driver.find_element(By.XPATH, "//bs-modal-body/div/div[2]/div/button").click()

        """Set new IP"""
        allowed_ip_field = self.driver.find_element(By.XPATH, "//*[@id='allowedIps']")
        allowed_ip_field.clear()
        allowed_ip_field.send_keys(ip_value)
        add_ip_button = self.driver.find_element(By.XPATH, "//bs-modal-body/div/div[2]/button")
        add_ip_button.click()
        Logging().reportDebugStep(self, "The allowed ip was edited: " + ip_value)
        return EditAffiliateModule()

    def edit_is_enabled_radio_button(self, is_enabled):

        if is_enabled == "yes":
            is_enabled_element = self.driver.find_element(By.XPATH, "//div[@class='btn-group form-group']//label[1]")
            is_enabled_element.click()
            Logging().reportDebugStep(self, "The enabled  was edited" + is_enabled)
        else:
            is_enabled_element = self.driver.find_element(By.XPATH, "//div[@class='btn-group form-group']//label[2]")
            is_enabled_element.click()
        Logging().reportDebugStep(self, "The enabled was edited and value was set: " + is_enabled)
        return EditAffiliateModule()

    def edit_allowed_methods(self, added_allowed_method):
        """Open pick list"""
        allowed_pick_list = self.driver.find_element(By.XPATH,
                                                     "//div[@class='multi-select']//div[@class='multi-select-title']")
        allowed_pick_list.click()
        Logging().reportDebugStep(self, "The allowed pick list was clicked")

        """Add new allowed method"""
        added_allowed_element = self.driver.find_element(By.XPATH,
                                                         "(//filter-multi-select/div/div[2]/span[%s])[1]" % added_allowed_method)
        added_allowed_element.click()
        Logging().reportDebugStep(self, "The first_allowed_element was edited" + added_allowed_method)

        # """2nd method"""
        # second_allowed_element = self.driver.find_element(By.XPATH,
        #                                                   "//div[@class='multi-select']//span[@class='hovered-option'][%s]" % allowed_methods_2)
        # second_allowed_element.click()
        # Logging().reportDebugStep(self, "The second_allowed_element was edited" + allowed_methods_2)
        #
        # """3rd method"""
        # third_allowed_element = self.driver.find_element(By.XPATH,
        #                                                  "//div[@class='multi-select']//span[@class='hovered-option'][%s]" % allowed_methods_3)
        # third_allowed_element.click()
        # Logging().reportDebugStep(self, "The third_allowed_element was edited" + allowed_methods_3)
        #
        # """4th method"""
        # fourth_allowed_element = self.driver.find_element(By.XPATH,
        #                                                   "//div[@class='multi-select']//span[@class='hovered-option'][%s]" % allowed_methods_4)
        #
        # fourth_allowed_element.click()
        # Logging().reportDebugStep(self, "The fourth_allowed_element was edited" + allowed_methods_4)
        #
        # """5th method"""
        # fifth_allowed_element = self.driver.find_element(By.XPATH,
        #                                                  "//div[@class='multi-select']//span[@class='hovered-option'][%s]" % allowed_methods_5)
        #
        # fifth_allowed_element.click()
        # Logging().reportDebugStep(self, "The fifth_allowed_element was edited" + allowed_methods_5)
        return EditAffiliateModule()

    def edit_countries(self, edited_blocked_countries):
        """Remove country from list (deselect it) and other countries leave as is"""
        allowed_pick_list = self.driver.find_element(By.XPATH,
                                                     "//div[@class='multi-select margin-top-10']//div[@class='multi-select-title']")
        allowed_pick_list.click()

        search_element = self.driver.find_element(By.XPATH,
                                                  "//div[@class='select-options options-enabled']//input")
        search_element.clear()
        search_element.send_keys(edited_blocked_countries)

        find_country = self.driver.find_element(By.XPATH,
                                                "//div[@class='select-options options-enabled']//span[@class='active-option'][1]")

        find_country.click()

        Logging().reportDebugStep(self, "The country was edited: " + edited_blocked_countries)

        # '''
        #     second country
        # '''
        #
        # search_element = self.driver.find_element(By.XPATH,
        #                                           "//div[@class='select-options options-enabled']//input")
        # search_element.clear()
        # search_element.send_keys(blocked_countries_2)
        #
        # find_country = self.driver.find_element(By.XPATH,
        #                                         "//div[@class='select-options options-enabled']//span[@class='hovered-option'][1]")
        #
        # find_country.click()
        # '''
        #     third country
        # '''
        #
        # search_element = self.driver.find_element(By.XPATH,
        #                                           "//div[@class='select-options options-enabled']//input")
        # search_element.clear()
        # search_element.send_keys(blocked_countries_3)
        #
        # find_country = self.driver.find_element(By.XPATH,
        #                                         "//div[@class='select-options options-enabled']//span[@class='hovered-option'][1]")
        #
        # find_country.click()
        #
        # Logging().reportDebugStep(self, "The third country was edited")
        #
        # '''
        #     fourth country
        # '''
        #
        # search_element = self.driver.find_element(By.XPATH,
        #                                           "//div[@class='select-options options-enabled']//input")
        # search_element.clear()
        # search_element.send_keys(blocked_countries_4)
        #
        # find_country = self.driver.find_element(By.XPATH,
        #                                         "//div[@class='select-options options-enabled']//span[@class='hovered-option'][1]")
        #
        # find_country.click()
        #
        # Logging().reportDebugStep(self, "The fourth country was edited")
        #
        # '''
        #     fifth country
        # '''
        #
        # search_element = self.driver.find_element(By.XPATH,
        #                                           "//div[@class='select-options options-enabled']//input")
        # search_element.clear()
        # search_element.send_keys(blocked_countries_5)
        #
        # find_country = self.driver.find_element(By.XPATH,
        #                                         "//div[@class='select-options options-enabled']//span[@class='hovered-option'][1]")
        #
        # find_country.click()
        #
        # Logging().reportDebugStep(self, "The fifth country was edited")

        return EditAffiliateModule()

    def click_submit(self):
        submit_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
        submit_button.click()


