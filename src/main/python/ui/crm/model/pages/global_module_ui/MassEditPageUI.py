from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class MassEditPageUI(CRMBasePage):

    def select_field_to_edit(self, field):
        sleep(0.1)
        item = super().wait_element_to_be_clickable(
            "//div[h3=' Choose fields to edit: ']//span[contains(text(),'%s')]" % field)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select '" + field + "' check box")
        return MassEditPageUI(self.driver)

    def set_text_field(self, title, text):
        sleep(0.1)
        field = super().wait_load_element("//div[label=' %s ']//following-sibling::mat-form-field//input" % title)
        field.clear()
        field.send_keys(text)
        Logging().reportDebugStep(self, "Set '" + text + "' to '" + title + "' field")
        return MassEditPageUI(self.driver)

    def select_from_list(self, pick_list, item_title):
        sleep(0.1)
        item = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[text()='%s']" % (pick_list, item_title))
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select '" + item_title + "' from pick list " + pick_list)
        return MassEditPageUI(self.driver)

    def click_save_changes_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Save changes' button")
        save_btn = super().wait_element_to_be_clickable("//button/span[text()=' Save changes ']")
        self.driver.execute_script("arguments[0].click();", save_btn)
        sleep(0.5)
        self.wait_loading_to_finish_new_ui(120)
        sleep(0.5)
        return MassEditPageUI(self.driver)
