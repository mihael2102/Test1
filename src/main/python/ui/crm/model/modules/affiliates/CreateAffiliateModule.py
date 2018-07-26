from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from selenium.webdriver.support.ui import Select
from src.main.python.utils.logs.Loging import Logging
from selenium.webdriver.support import expected_conditions as EC

class CreateAffiliateModule(CRMBasePage):
    """
    Methods which are related to "Create affiliate" popup
    """

    def __init__(self):
        super().__init__()

    def perform_create_affiliate(self, partner_name, brand, allowed_ip, is_enabled, allowed_methods_1,
                                 allowed_methods_2, allowed_methods_3, allowed_methods_4, allowed_methods_5,
                                 blocked_countries_1, blocked_countries_2, blocked_countries_3, blocked_countries_4,
                                 blocked_countries_5):

        self.set_partner_name(partner_name)
        self.set_brand(brand)
        self.set_allowed_ip(allowed_ip)
        self.set_is_enabled_radio_button(is_enabled)
        self.set_allowed_methods(allowed_methods_1, allowed_methods_2, allowed_methods_3,
                                 allowed_methods_4, allowed_methods_5)

        self.set_countries(blocked_countries_1, blocked_countries_2, blocked_countries_3,
                           blocked_countries_4,blocked_countries_5)
        self.click_submit()

    def set_partner_name(self, partner_name):
        partner_name_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='partnerName']")))
        partner_name_field.clear()
        partner_name_field.send_keys(partner_name)
        Logging().reportDebugStep(self, "Partner name was set: " + partner_name)
        return CreateAffiliateModule()

    def set_brand(self, brand):
        select = Select(self.driver.find_element(By.ID, "brand"))
        select.select_by_visible_text(brand)
        Logging().reportDebugStep(self, "The brand was selected: " + brand)
        return CreateAffiliateModule()

    def set_allowed_ip(self, ip_value):
        allowed_ip_field = self.driver.find_element(By.XPATH, "//*[@id='allowedIps']")
        allowed_ip_field.clear()
        allowed_ip_field.send_keys(ip_value)
        add_ip_button = self.driver.find_element(By.XPATH, "//bs-modal-body/div/div[3]/button")
        add_ip_button.click()
        Logging().reportDebugStep(self, "The allowed ip was set: " + ip_value)
        return CreateAffiliateModule()

    def set_is_enabled_radio_button(self, is_enabled):

        if is_enabled == "yes":
            is_enabled_element = self.driver.find_element(By.XPATH, "//div[@class='btn-group form-group']//label[1]")
            is_enabled_element.click()
            Logging().reportDebugStep(self, "The enabled  was set" + is_enabled)
        else:
            is_enabled_element = self.driver.find_element(By.XPATH, "//div[@class='btn-group form-group']//label[2]")
            is_enabled_element.click()
        Logging().reportDebugStep(self, "The enabled was set" + is_enabled)
        return CreateAffiliateModule()

    def set_allowed_methods(self, allowed_methods_1, allowed_methods_2, allowed_methods_3, allowed_methods_4,
                            allowed_methods_5):
        allowed_pick_list = self.driver.find_element(By.XPATH,
                                                     "//div[@class='multi-select']//div[@class='multi-select-title']")
        allowed_pick_list.click()
        Logging().reportDebugStep(self, "The allowed pick list was clicked")

        first_allowed_element = self.driver.find_element(By.XPATH,
                                                         "//div[@class='multi-select']//span[@class='hovered-option'][%s]" % allowed_methods_1)
        first_allowed_element.click()
        Logging().reportDebugStep(self, "The first_allowed_element was set" + allowed_methods_1)

        second_allowed_element = self.driver.find_element(By.XPATH,
                                                          "//div[@class='multi-select']//span[@class='hovered-option'][%s]" % allowed_methods_2)
        second_allowed_element.click()
        Logging().reportDebugStep(self, "The second_allowed_element was set" + allowed_methods_2)
        third_allowed_element = self.driver.find_element(By.XPATH,
                                                         "//div[@class='multi-select']//span[@class='hovered-option'][%s]" % allowed_methods_3)
        third_allowed_element.click()
        Logging().reportDebugStep(self, "The third_allowed_element was set" + allowed_methods_3)
        fourth_allowed_element = self.driver.find_element(By.XPATH,
                                                          "//div[@class='multi-select']//span[@class='hovered-option'][%s]" % allowed_methods_4)

        fourth_allowed_element.click()
        Logging().reportDebugStep(self, "The fourth_allowed_element was set" + allowed_methods_4)
        fifth_allowed_element = self.driver.find_element(By.XPATH,
                                                         "//div[@class='multi-select']//span[@class='hovered-option'][%s]" % allowed_methods_5)

        fifth_allowed_element.click()
        Logging().reportDebugStep(self, "The fifth_allowed_element was set" + allowed_methods_5)
        return CreateAffiliateModule()

    def set_countries(self, blocked_countries_1, blocked_countries_2, blocked_countries_3, blocked_countries_4,
                      blocked_countries_5):
        allowed_pick_list = self.driver.find_element(By.XPATH,
                                                     "//div[@class='multi-select margin-top-10']//div[@class='multi-select-title']")
        allowed_pick_list.click()

        search_element = self.driver.find_element(By.XPATH,
                                                  "//div[@class='select-options options-enabled']//input")
        search_element.clear()
        search_element.send_keys(blocked_countries_1)

        find_country = self.driver.find_element(By.XPATH,
                                                "//div[@class='select-options options-enabled']//span[@class='hovered-option'][1]")

        find_country.click()

        Logging().reportDebugStep(self, "The first country was set")

        '''
            second country
        '''

        search_element = self.driver.find_element(By.XPATH,
                                                  "//div[@class='select-options options-enabled']//input")
        search_element.clear()
        search_element.send_keys(blocked_countries_2)

        find_country = self.driver.find_element(By.XPATH,
                                                "//div[@class='select-options options-enabled']//span[@class='hovered-option'][1]")

        find_country.click()
        '''
            third country
        '''

        search_element = self.driver.find_element(By.XPATH,
                                                  "//div[@class='select-options options-enabled']//input")
        search_element.clear()
        search_element.send_keys(blocked_countries_3)

        find_country = self.driver.find_element(By.XPATH,
                                                "//div[@class='select-options options-enabled']//span[@class='hovered-option'][1]")

        find_country.click()

        Logging().reportDebugStep(self, "The third country was set")

        '''
            fourth country
        '''

        search_element = self.driver.find_element(By.XPATH,
                                                  "//div[@class='select-options options-enabled']//input")
        search_element.clear()
        search_element.send_keys(blocked_countries_4)

        find_country = self.driver.find_element(By.XPATH,
                                                "//div[@class='select-options options-enabled']//span[@class='hovered-option'][1]")

        find_country.click()

        Logging().reportDebugStep(self, "The fourth country was set")

        '''
            fifth country
        '''

        search_element = self.driver.find_element(By.XPATH,
                                                  "//div[@class='select-options options-enabled']//input")
        search_element.clear()
        search_element.send_keys(blocked_countries_5)

        find_country = self.driver.find_element(By.XPATH,
                                                "//div[@class='select-options options-enabled']//span[@class='hovered-option'][1]")

        find_country.click()

        Logging().reportDebugStep(self, "The fifth country was set")

    def click_submit(self):
        submit_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
        submit_button.click()
