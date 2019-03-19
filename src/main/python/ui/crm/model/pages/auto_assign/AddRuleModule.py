from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class AddRuleModule(CRMBasePage):
    # def __init__(self):
    #     super().__init__()

    def perform_add_rule(self, rule_name, brand, rule_type, campaign, role):
        self.set_rule_name(rule_name)
        self.set_brand(brand)
        self.set_lead_module_check_box()
        self.set_clients_module_check_box()
        self.set_set_assign_to_role_checkbox()
        self.select_role(role)
        self.select_rule_type(rule_type)
        self.select_item(campaign)
        self.perform_submit()

    def perform_second_add_rule(self, rule_name, brand, rule_type, item, role):
        self.set_rule_name(rule_name)
        self.set_brand(brand)
        self.set_lead_module_check_box()
        self.set_clients_module_check_box()
        self.set_set_assign_to_role_checkbox()
        self.select_role(role)
        self.select_rule_type(rule_type)
        self.select_item(item)
        self.perform_submit()

    def set_rule_name(self, rule_name):
        rule_name_field = super().wait_visible_of_element("//input[@name='rule_name']")
        rule_name_field.clear()
        rule_name_field.send_keys(rule_name)
        Logging().reportDebugStep(self, "The rule name field was entered: " + rule_name)
        return AddRuleModule(self.driver)

    def set_set_assign_to_role_checkbox(self):
        rol_name_field = super().wait_visible_of_element(
            "//div[@class='col-md-12 p-l-0 p-r-0 text-center']//input[@value='2']")
        rol_name_field.click()
        Logging().reportDebugStep(self, "The rol name field was set")
        return AddRuleModule()

    def set_brand(self, brand):
        try:
            campaign_name_link = Select(super().wait_visible_of_element("//select[@name='brand_id']"))
            campaign_name_link.select_by_visible_text(brand)
            Logging().reportDebugStep(self, "The brand was set: " + brand)
            return AddRuleModule(self.driver)
        except NoSuchElementException:
            pass
            Logging().reportDebugStep(self, "There is no Brand field")
            return AddRuleModule(self.driver)

    def select_brand_by_number(self):
        try:
            campaign_name_link = super().wait_visible_of_element("//select[@name='brand_id']")
            campaign_name_link.click()
            first_option = self.driver.find_element_by_xpath("//*[@id='brand_id']/option[2]")
            # self.driver.execute_script("arguments[0].click();", first_option)
            first_option.click()
            Logging().reportDebugStep(self, "The brand was set")
            return AddRuleModule(self.driver)
        except NoSuchElementException:
            pass
            Logging().reportDebugStep(self, "There is no Brand field")
            return AddRuleModule(self.driver)

    def set_lead_module_check_box(self):
        campaign_name_link = self.driver.find_element(By.XPATH, "//input[@name='leadrule']")
        campaign_name_link.click()
        Logging().reportDebugStep(self, "The lead module checkbox was set")
        return AddRuleModule(self.driver)

    def set_clients_module_check_box(self):
        campaign_name_link = self.driver.find_element(By.XPATH, "//input[@name='clientrule']")
        campaign_name_link.click()
        Logging().reportDebugStep(self, "The clients module checkbox was set")
        return AddRuleModule(self.driver)

    def set_assign_to_check_box(self):
        assign_to_check_box = self.driver.find_element(By.XPATH,
                                                "//div[@class='col-md-12 p-l-0 p-r-0 text-center']//input[@value='1']")
        assign_to_check_box.click()
        Logging().reportDebugStep(self, "The assign to checkbox was set")
        return AddRuleModule(self.driver)

    def perform_submit(self):
        submit_button = self.driver.find_element(By.XPATH,
                                                 "//button[contains(text(),'Submit')]")
        submit_button.click()
        Logging().reportDebugStep(self, "The submit button was set")
        return AddRuleModule(self.driver)

    def select_rule_type(self, rule_type):
        rule_type_button = Select(super().wait_visible_of_element("//select[@name='ruletype']"))
        rule_type_button.select_by_visible_text(rule_type)
        Logging().reportDebugStep(self, "The rule_type was selected")
        return AddRuleModule(self.driver)

    def select_item(self, item):
        campaign_drop_down = self.driver.find_element(By.XPATH,
                                                      "//div[@id='selection_select_multi_container']//span[1]")
        campaign_drop_down.click()
        campaign_field = self.driver.find_element(By.XPATH,
                                                  "//input[@placeholder='Search']")
        campaign_field.clear()
        campaign_field.send_keys(item)
        item = super().wait_visible_of_element("//label[contains(text(),'%s')]" % item)
        item.click()
        campaign_drop_down.click()

        Logging().reportDebugStep(self, "The rule_type was selected")
        return AddRuleModule(self.driver)

    def select_role(self, role):
        role_filed = self.driver.find_element(By.XPATH,
                                              "//div[@id='role_div']//input[1]")
        role_filed.send_keys(role)

        item = super().wait_visible_of_element(
            "//div[contains(text(),'%s')]/preceding-sibling::div[1]//div[1]//div[1]" % role)
        item.click()
        return AddRuleModule()

    def select_destination_user(self, user):
        search_user_field = super().wait_visible_of_element("//*[@id='jqxTreeUsers']/input[1]")
        search_user_field.clear()
        search_user_field.send_keys(user)
        sleep(1)
        user_item = self.driver.find_element_by_xpath("//li[@username='pandaqa pandaqa']/div/div/div")
        user_item.click()
        Logging().reportDebugStep(self, "User selected")
        return AddRuleModule(self.driver)

    def click_ok(self):
        sleep(1)
        super().click_ok()
        sleep(1)
        return AddRuleModule(self.driver)