from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class MassAssignPageUI(CRMBasePage):

    def select_department(self, department):
        sleep(0.1)
        item = super().wait_element_to_be_clickable("//span[contains(text(),'%s')]" % department)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select '" + department + "' check box")
        return MassAssignPageUI(self.driver)

    def set_users_field(self, user):
        sleep(0.1)
        users_field = super().wait_element_to_be_clickable("//input[@placeholder='Search users']")
        users_field.clear()
        users_field.send_keys(user)
        Logging().reportDebugStep(self, "Set '" + user + "' to Users field")
        return MassAssignPageUI(self.driver)

    def select_user_by_title(self, user):
        sleep(0.1)
        user_item = super().wait_element_to_be_clickable(
            "//div[@class='options-wrap ng-star-inserted']//span[contains(text(),'%s')]" % user)
        self.driver.execute_script("arguments[0].click();", user_item)
        Logging().reportDebugStep(self, "Select '" + user + "' from list")
        return MassAssignPageUI(self.driver)

    def select_status(self, status):
        sleep(0.1)
        item = super().wait_load_element("//div[@class='row client-status-wrap']//span[text()='%s']" % status)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select '" + status + "' status")
        return MassAssignPageUI(self.driver)

    def click_assign_btn(self):
        sleep(0.1)
        assign_btn = super().wait_element_to_be_clickable("//button/span[text()=' Assign ']")
        self.driver.execute_script("arguments[0].click();", assign_btn)
        sleep(1)
        self.wait_loading_to_finish_new_ui(5)
        Logging().reportDebugStep(self, "Click 'Assign' button")
        return MassAssignPageUI(self.driver)
