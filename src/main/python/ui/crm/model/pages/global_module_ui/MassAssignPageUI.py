from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI


class MassAssignPageUI(CRMBasePage):

    def mass_assign(self, department=None, user=None, status=None, final_btn=None):
        if department:
            self.select_department(department)
        if user:
            self.set_users_field(user)
            self.select_user_by_title(user)
        if status:
            self.select_status(status)
        self.click_assign_btn(final_btn)
        return MassAssignPageUI(self.driver)

    def select_department(self, department):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select '" + department + "' check box")
        item = super().wait_element_to_be_clickable("//span[contains(text(),'%s')]" % department, timeout=50)
        self.driver.execute_script("arguments[0].click();", item)
        return MassAssignPageUI(self.driver)

    def set_users_field(self, user):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set '" + user + "' to Users field")
        users_field = super().wait_element_to_be_clickable("//input[@placeholder='Search users']")
        users_field.clear()
        users_field.send_keys(user)
        return MassAssignPageUI(self.driver)

    def select_user_by_title(self, user):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select '" + user + "' from list")
        user_item = super().wait_element_to_be_clickable(
            "//div[@class='options-wrap ng-star-inserted']//span[contains(text(),'%s')]" % user)
        self.driver.execute_script("arguments[0].click();", user_item)
        return MassAssignPageUI(self.driver)

    def select_status(self, status):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select '" + status + "' status")
        item = super().wait_load_element("//div[@class='row client-status-wrap']//span[text()='%s']" % status)
        self.driver.execute_script("arguments[0].click();", item)
        return MassAssignPageUI(self.driver)

    def get_item_from_list_by_number(self, pick_list, number):
        item = GlobalPopupPageUI(self.driver)\
            .get_item_from_list_by_number(pick_list, number)
        return item

    def select_pick_list_item_by_number(self, pick_list, number):
        GlobalPopupPageUI(self.driver)\
            .select_pick_list_item_by_number(pick_list, number)
        return MassAssignPageUI(self.driver)

    def click_assign_btn(self, final_btn):
        GlobalPopupPageUI(self.driver) \
            .click_final_btn(final_btn)
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
        return MassAssignPageUI(self.driver)
