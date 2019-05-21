from time import sleep

from selenium.webdriver.common.by import By
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.auto_assign.AddRuleModule import AddRuleModule
from src.main.python.ui.crm.model.pages.auto_assign.EditRuleModule import EditRuleModule
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class AutoAssignPage(CRMBasePage):
    # def __init__(self) -> None:
    #     super().__init__()

    def open_add_rule_module(self):
        add_rule_button = super().wait_element_to_be_clickable("//button[contains(text(),'Add Rule')]")
        add_rule_button.click()
        Logging().reportDebugStep(self, "The Add rule module was opened")
        return AddRuleModule(self.driver)

    def get_successfull_message(self):
        message = super().wait_visible_of_element("//div[@class='bootstrap-dialog-message']")
        Logging().reportDebugStep(self, "The Add rule module was opened")
        return message.text

    def click_ok(self):
        super().click_ok()
        return AutoAssignPage(self.driver)

    def perform_searching_auto_assign_module_by_name(self, rule_name):
        sleep(1)
        add_campaign_button = super().wait_visible_of_element(
            "//div[@id='filterrow.ListGrid0']//div[3]/preceding-sibling::div[1]//input")
        add_campaign_button.clear()
        add_campaign_button.send_keys(rule_name)
        Logging().reportDebugStep(self, "The campaign name was entered: " + rule_name)
        return AutoAssignPage(self.driver)

    def make_delete_rule(self):
        sleep(2)
        delete_button = super().wait_visible_of_element("//div[@title='Delete']")
        delete_button.click()
        Logging().reportDebugStep(self, "The Delete button was clicked")
        return AutoAssignPage(self.driver)

    def confirm_delete_rule(self):
        confirm_delete_button = super().wait_visible_of_element("//button[contains(text(),'OK')]")
        confirm_delete_button.click()
        Logging().reportDebugStep(self, "Confirm delete button was clicked")
        return AutoAssignPage(self.driver)

    def check_delete_message(self):
        sleep(1)
        message = super().wait_visible_of_element("//div[@class='bootstrap-dialog-message']").text
        if message == "Record deleted successfully.":
            self.click_ok()
            Logging().reportDebugStep(self, "Record deleted successfully")
            return AutoAssignPage(self.driver)
        elif message == "You are not permitted to perform this action":
            self.click_ok()
            Logging().reportDebugStep(self, "You are not permitted to perform this action")
            return self

    def click_edit_by_pencil(self):
        sleep(2)
        pencil_link = super().wait_visible_of_element("//div[@title='Edit']")
        pencil_link.click()
        Logging().reportDebugStep(self, "The edit pencil was clicked")
        return EditRuleModule()

    def get_rule_name_status(self, rule_name):
        sleep(2)
        rule_name_list = []
        modules_element = self.driver.find_element(By.XPATH, "//div[@role='row'][1]//div[2]/div").text
        Logging().reportDebugStep(self, "The modules_element is displayed: " + modules_element)
        rule_name_list.append(modules_element)
        for name in rule_name_list:
            if rule_name in name:
                return True
            else:
                return False

    def get_modules_status(self, first_module, second_module):
        rule_name_list = []
        modules_element = self.driver.find_element(By.XPATH, "//div[@role='row'][1]//div[3]/div").text
        Logging().reportDebugStep(self, "The modules_element is displayed: " + modules_element)
        rule_name_list.append(modules_element)
        for name in rule_name_list:
            if first_module in name:
                return True
            if second_module in name:
                return True
            else:
                return False

    def get_assign_to_status(self, assign_to):
        rule_name_list = []
        modules_element = self.driver.find_element(By.XPATH, "//div[@role='row'][1]//div[4]/div").text
        Logging().reportDebugStep(self, "The modules_element is displayed: " + modules_element)
        rule_name_list.append(modules_element)
        for name in rule_name_list:
            if assign_to in name:
                return True
            else:
                return False

    def get_assigned_details_status(self, assigned_details):
        rule_name_list = []
        modules_element = self.driver.find_element(By.XPATH, "//div[@role='row'][1]//div[5]/div").text
        Logging().reportDebugStep(self, "The modules_element is displayed: " + modules_element)
        rule_name_list.append(modules_element)
        for name in rule_name_list:
            if assigned_details in name:
                return True
            else:
                return False

    def get_rule_type_status(self, rule_tpe):
        rule_name_list = []
        modules_element = self.driver.find_element(By.XPATH, "//div[@role='row'][1]//div[6]/div").text
        Logging().reportDebugStep(self, "The modules_element is displayed: " + modules_element)
        rule_name_list.append(modules_element)
        for name in rule_name_list:
            if rule_tpe in name:
                return True
            else:
                return False

    def get_status(self, status):
        rule_name_list = []
        modules_element = self.driver.find_element(By.XPATH, "//div[@role='row'][1]//div[8]/div").text
        Logging().reportDebugStep(self, "The modules_element is displayed: " + modules_element)
        rule_name_list.append(modules_element)
        for name in rule_name_list:
            if status in name:
                return True
            else:
                return False

    def get_brand_status(self, brand):
        rule_name_list = []
        modules_element = self.driver.find_element(By.XPATH, "//div[@role='row'][1]//div[9]/div").text
        Logging().reportDebugStep(self, "The modules_element is displayed: " + modules_element)
        rule_name_list.append(modules_element)
        for name in rule_name_list:
            if brand in name:
                return True
            else:
                return False

    def get_created_by_status(self, status):
        rule_name_list = []
        modules_element = self.driver.find_element(By.XPATH, "//div[@role='row'][1]//div[10]/div").text
        Logging().reportDebugStep(self, "The modules_element is displayed: " + modules_element)
        rule_name_list.append(modules_element)
        for name in rule_name_list:
            if status in name:
                return True
            else:
                return False

    def get_date_created_status(self, date_created):
        rule_name_list = []
        modules_element = self.driver.find_element(By.XPATH, "//div[@role='row'][1]//div[11]/div").text
        Logging().reportDebugStep(self, "The modules_element is displayed: " + modules_element)
        rule_name_list.append(modules_element)
        for name in rule_name_list:
            if date_created in name:
                return True
            else:
                return False

    def get_no_data_text(self):
        no_data_text = super().wait_visible_of_element("//span[contains(text(),'No data to display')]")
        Logging().reportDebugStep(self, "The rule was delete, the message was displayed on grid: " + no_data_text.text)
        return no_data_text.text
