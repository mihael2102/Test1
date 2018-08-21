from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class EditRuleModule(CRMBasePage):
    def __init__(self):
        super().__init__()

    def perform_edit_rule(self, rule_name, brand, user, rule_type, currency):
        self.set_lead_module_check_box()
        self.set_rule_name(rule_name)
        self.set_brand(brand)
        self.set_set_assign_to_user_checkbox()
        self.select_user(user)
        self.select_rule_type(rule_type)
        self.select_item(currency)
        self.perform_submit()

    def set_rule_name(self, rule_name):
        rule_name_field = super().wait_visible_of_element("//input[@name='rule_name']")
        rule_name_field.clear()
        rule_name_field.send_keys(rule_name)
        Logging().reportDebugStep(self, "The rule name field was entered: " + rule_name)
        return EditRuleModule()

    def set_set_assign_to_role_checkbox(self):
        rol_name_field = super().wait_visible_of_element(
            "//div[@class='col-md-12 p-l-0 p-r-0 text-center']//input[@value='2']")
        rol_name_field.click()
        Logging().reportDebugStep(self, "The role checkbox was set")
        return EditRuleModule()

    def set_set_assign_to_user_checkbox(self):
        rol_name_field = super().wait_visible_of_element(
            "//div[@class='col-md-12 p-l-0 p-r-0 text-center']//input[@value='1']")
        rol_name_field.click()
        Logging().reportDebugStep(self, "The user checkbox was set")
        return EditRuleModule()

    def set_brand(self, brand):
        campaign_name_link = Select(super().wait_visible_of_element("//select[@name='brand_id']"))
        campaign_name_link.select_by_visible_text(brand)
        Logging().reportDebugStep(self, "The brand was set: " + brand)
        return EditRuleModule()

    def set_lead_module_check_box(self):
        sleep(2)
        campaign_name_link = super().wait_element_to_be_clickable("//input[@name='leadrule']")
        campaign_name_link.click()
        Logging().reportDebugStep(self, "The lead module checkbox was set")
        return EditRuleModule()

    def set_clients_module_check_box(self):
        campaign_name_link = self.driver.find_element(By.XPATH, "//input[@name='clientrule']")
        campaign_name_link.click()
        Logging().reportDebugStep(self, "The clients module checkbox was set")
        return EditRuleModule()

    def set_assign_to_check_box(self):
        assign_to_check_box = self.driver.find_element(By.XPATH,
                                                       "//div[@class='col-md-12 p-l-0 p-r-0 text-center']//input[@value='1']")
        assign_to_check_box.click()
        Logging().reportDebugStep(self, "The assign to checkbox was set")
        return EditRuleModule()

    def perform_submit(self):
        submit_button = self.driver.find_element(By.XPATH,
                                                 "//button[contains(text(),'Submit')]")
        submit_button.click()
        Logging().reportDebugStep(self, "The submit button was set")
        return EditRuleModule()

    def select_rule_type(self, rule_type):
        rule_type_button = Select(super().wait_visible_of_element("//select[@name='ruletype']"))
        rule_type_button.select_by_visible_text(rule_type)
        Logging().reportDebugStep(self, "The rule_type was selected")
        return EditRuleModule()

    def select_item(self, campaign):
        campaign_drop_down = self.driver.find_element(By.XPATH,
                                                      "//div[@id='selection_select_multi_container']//span[1]")
        campaign_drop_down.click()
        campaign_field = self.driver.find_element(By.XPATH,
                                                  "//input[@placeholder='Search']")
        campaign_field.send_keys(campaign)
        item = super().wait_visible_of_element("//label[contains(text(),'%s')]" % campaign)
        item.click()
        campaign_drop_down.click()

        Logging().reportDebugStep(self, "The rule_type was selected")
        return EditRuleModule()

    def select_role(self, role):
        role_filed = self.driver.find_element(By.XPATH,
                                              "//div[@id='role_div']//input[1]")
        role_filed.send_keys(role)

        item = super().wait_visible_of_element(
            "//div[contains(text(),'%s')]/preceding-sibling::div[1]//div[1]//div[1]" % role)
        item.click()
        return EditRuleModule()

    def select_user(self, user):
        role_filed = self.driver.find_element(By.XPATH,
                                              "//div[@id='jqxTreeUsers']//input[1]")
        role_filed.send_keys(user)

        item = super().wait_visible_of_element(
            "//div[contains(text(),'%s')]/preceding-sibling::div[1]//div[1]//div[1]" % user)
        item.click()
        return EditRuleModule()
