from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI


class FilterPageUI(CRMBasePage):

    def create_filter_ui(self, field1=None, view_name=None, list1=None, based_filter=None, column1=None,
                         column2=None, column3=None, column4=None, column5=None, column6=None, column7=None,
                         column8=None, column9=None, column10=None, column11=None):
        self.click_add_filter_btn()
        if view_name:
            self.set_text_field(field1, view_name)
        if based_filter:
            self.select_from_list(list1, based_filter)
        if column1:
            self.select_column(column1)
        if column2:
            self.select_column(column2)
        if column3:
            self.select_column(column3)
        if column4:
            self.select_column(column4)
        if column5:
            self.select_column(column5)
        if column6:
            self.select_column(column6)
        if column7:
            self.select_column(column7)
        if column8:
            self.select_column(column8)
        if column9:
            self.select_column(column9)
        if column10:
            self.select_column(column10)
        if column11:
            self.select_column(column11)
        self.click_create_filter_btn()

    def click_add_filter_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Add Filter' button")
        btn = super().wait_element_to_be_clickable("//button[@title='Create Filter']")
        btn.click()
        return FilterPageUI(self.driver)

    def set_text_field(self, title, text):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set '" + text + "' to '" + title + "' field")
        field = super().wait_load_element(
            "//div[label[contains(text(),'%s')]]//following-sibling::mat-form-field//input" % title)
        field.clear()
        field.send_keys(text)
        return FilterPageUI(self.driver)

    def select_from_list(self, pick_list, item_title):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select '" + item_title + "' from pick list " + pick_list)
        item = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[text()='%s']" % (pick_list, item_title))
        self.driver.execute_script("arguments[0].click();", item)
        return FilterPageUI(self.driver)

    def select_column(self, item_title):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select '" + item_title + "' from 'Table columns and order'")
        item = super().wait_load_element(
            "//section[h3='Table columns and order']//following-sibling::ul//span[text()='%s']" % item_title)
        self.driver.execute_script("arguments[0].click();", item)
        return FilterPageUI(self.driver)

    def click_create_filter_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Create filter' button")
        btn = super().wait_element_to_be_clickable("//span[text()='Create filter']")
        self.driver.execute_script("arguments[0].click();", btn)
        sleep(1)
        self.wait_loading_to_finish_new_ui(5)
        return FilterPageUI(self.driver)

    def get_current_filter(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Get current filter title")
        current_filter = super().wait_load_element("//nice-select[@searchplaceholder='Search filter']"
                                                   "//div[@class='select-wrap']//span[@class='ng-star-inserted']").text
        Logging().reportDebugStep(self, "Current filter title: " + current_filter)
        return current_filter

    def delete_filter(self, title):
        sleep(1)
        Logging().reportDebugStep(self, "Click Delete filter button")
        delete_btn = super().wait_load_element(
            "(//a[@title='%s']//following-sibling::div[@class='actions-wrap ng-star-inserted']"
            "/ul[@class='actions-menu']//button[@title='Delete'])[1]" % title)
        self.driver.execute_script("arguments[0].click();", delete_btn)
        Logging().reportDebugStep(self, "Delete filter button was clicked")
        return GlobalModulePageUI(self.driver)

    def verify_filter_in_list(self, title):
        sleep(0.1)
        Logging().reportDebugStep(self, "Check filter " + title + " in filter pick-list")
        pick_list = super().wait_load_element(
            "//nice-select[@searchplaceholder='Search filter']//div[@class='select-wrap']//following-sibling::ul")\
            .get_attribute("innerText")
        try:
            assert title in pick_list
            Logging().reportDebugStep(self, "Filter " + title + " exist in pick-list")
            return True
        except AssertionError:
            Logging().reportDebugStep(self, "Filter " + title + " is not existing in pick-list")
            return False
