from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
#import allure
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class GlobalTablePageUI(CRMBasePage):

    def set_data_column_field(self, column, data):
        sleep(0.1)
        btn = super().wait_load_element("(//span[@class='placeholder']/span[text()='%s'])[1]" % column)
        self.driver.execute_script("arguments[0].click();", btn)
        field = super().wait_load_element(
            "//span[contains(text(),'%s')]//following-sibling::div[@class='select-wrap']//input[@placeholder='Search']"
            % column)
        field.clear()
        field.send_keys(data)
        sleep(1)
        try:
            done = super().wait_element_to_be_clickable("//button[contains(span,'Apply')]")
            self.driver.execute_script("arguments[0].click();", done)
        except:
            pass
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        Logging().reportDebugStep(self, "Search by column: " + column + " with data: " + data)
        return GlobalTablePageUI(self.driver)

    def select_data_column_field(self, column, data):
        sleep(0.1)
        field = super().wait_element_to_be_clickable("//span[@class='placeholder']/span[text()='%s']" % column)
        self.driver.execute_script("arguments[0].click();", field)
        sleep(0.5)
        item = super().wait_load_element("//span[contains(text(),'%s')]//following-sibling::ul//span[text()='%s']"
                                         % (column, data))
        self.driver.execute_script("arguments[0].click();", item)
        try:
            done = super().wait_element_to_be_clickable("//button/span[text()='Apply']")
            self.driver.execute_script("arguments[0].click();", done)
        except:
            pass
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        Logging().reportDebugStep(self, "Search by column: " + column + " with data: " + data)
        return GlobalTablePageUI(self.driver)

    """
        Method gets title of column and returns index (str) of column in list view:
    """

    def get_column_number_by_title_ui(self, title):
        sleep(0.1)
        try:
            table = self.driver.find_element_by_xpath("//table/thead[@role='rowgroup']/tr")
            count = 0
            index = ""
            for td in table.find_elements_by_xpath("//th[@role='columnheader']"):
                count += 1
                if title.lower() in td.text.lower():
                    index = str(count)
                    break
            assert len(index)
            Logging().reportDebugStep(self, "Number of column " + title + " is: " + index)
            return index
        except(NoSuchElementException, TimeoutException, AssertionError, AttributeError):
            Logging().reportDebugStep(self, "Column '" + title + "' does not exist")
            return False

    """
        Method return data from cell of table (list view) by column title and row number:
    """

    def get_data_from_list_view_ui(self, column, row):
        column_number = self.get_column_number_by_title_ui(column)
        if column_number:
            data = super().wait_load_element(
                "//table/tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))][%s]/td[%s]"
                % (row, column_number)).text
            Logging().reportDebugStep(self,
                                      "Get data from list view (column = " + column + ", row = " + row + "): " + data)
            return data
        else:
            Logging().reportDebugStep(self, "Column '" + column + "' or row '" + row + "' does not exist")
            return False

    """
        Check every line of table contain needed string:
    """

    def global_data_checker_new_ui(self, data):
        self.wait_loading_to_finish_new_ui(10)
        try:
            table = self.driver.find_element_by_xpath("//tbody[@role='rowgroup']")
            row_count = 0
            for tr in table.find_elements_by_xpath("//tbody[@role='rowgroup']/tr[not (contains(@style,'hidden'))]"):
                assert data.lower() in tr.text.lower()
                row_count += 1
            Logging().reportDebugStep(self, data + " is verified in " + str(row_count) + " rows")
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            sleep(0.1)
            super().wait_element_to_be_disappear("//tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))][1]",
                                                 timeout=5)
            Logging().reportDebugStep(self, "Data was not found")
        return GlobalTablePageUI(self.driver)

    def select_all_records_checkbox(self):
        sleep(0.2)
        all_records_checkbox = super().wait_element_to_be_clickable(
            "//th[@role='columnheader']//label[@class='mat-checkbox-layout']")
        all_records_checkbox.click()
        Logging().reportDebugStep(self, "All records on the page were selected")
        return GlobalTablePageUI(self.driver)

    def click_select_all_records_btn(self):
        sleep(0.2)
        Logging().reportDebugStep(self, "Click 'Select All records' button")
        all_records_btn = super().wait_element_to_be_clickable("//div[contains(text(),' Select all records ')]")
        all_records_btn.click()
        return GlobalTablePageUI(self.driver)

    """
        Execute click on one from Mass Action buttons
    """

    def click_mass_action_btn(self, btn_title):
        sleep(0.1)
        btn = super().wait_element_to_be_clickable(
            "//div[contains(@class,'mass-actions')]/button/span[contains(text(),'%s')]" % btn_title)
        self.driver.execute_script("arguments[0].click();", btn)
        Logging().reportDebugStep(self, "Click '" + btn_title + "' button")
        return GlobalTablePageUI(self.driver)

    """
        Verify successful message
    """

    def verify_success_message(self):
        message = super().wait_load_element("//div[contains(@class,'dialog-content-success mat-dialog-content')]").text
        Logging().reportDebugStep(self, "Get message: " + message)
        assert "success" in message.lower()
        return GlobalTablePageUI(self.driver)

    """
        Click OK button
    """

    def click_ok(self):
        sleep(0.1)
        button = super().wait_element_to_be_clickable("//*[text()=' OK ']")
        self.driver.execute_script("arguments[0].click();", button)
        Logging().reportDebugStep(self, "OK button was clicked")
        sleep(1)
        return GlobalTablePageUI(self.driver)

    def select_filter_new_ui(self, test_filter):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select filter: " + test_filter)
        filter_item = super().wait_load_element("//span[contains(text(),'%s')]" % test_filter)
        self.driver.execute_script("arguments[0].click();", filter_item)
        sleep(1)
        self.wait_crm_loading_to_finish()
        return GlobalTablePageUI(self.driver)

    """
        Delete Record
    """

    def click_delete_icon_list_view(self, row):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Delete' button")
        delete_icon = super().wait_element_to_be_clickable(
            "//tr[not(contains(@style,'hidden'))][%s]//button[@title='delete']" % row)
        self.driver.execute_script("arguments[0].click();", delete_icon)
        return GlobalTablePageUI(self.driver)

    def approve_deleting(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Delete' button in approve pop up")
        delete_btn = super().wait_element_to_be_clickable(
            "//div[@class='mat-dialog-actions']/button/span[text()=' Delete ']")
        delete_btn.click()
        return GlobalTablePageUI(self.driver)

    def verify_data_not_found(self):
        sleep(0.1)
        super().wait_element_to_be_disappear("//tbody[@role='rowgroup']/tr[not(contains(@style,'hidden'))][1]",
                                             timeout=5)
        Logging().reportDebugStep(self, "Data was not found")
        return GlobalTablePageUI(self.driver)

    def open_actions_list(self):
        hover_mouse = ActionChains(self.driver)
        more_list_element = super().wait_element_to_be_clickable(
            "//tr[not(contains(@style,'hidden'))][1]/td/button/span/mat-icon[text()='more_vert']")
        hover_mouse.move_to_element(more_list_element)
        hover_mouse.perform()
        return GlobalTablePageUI(self.driver)
