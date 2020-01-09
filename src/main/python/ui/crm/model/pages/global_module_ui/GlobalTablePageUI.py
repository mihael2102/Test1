from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.client_modules.mass_sms.SendSMSClientsModule import SendSMSClientsModule
from src.main.python.ui.crm.model.modules.client_modules.send_email.SendEmailClientsModule import SendEmailClientsModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.modules.client_modules.mass_assign.MassAssignClientsModule import \
    MassAssignClientsModule
from src.main.python.ui.crm.model.modules.client_modules.mass_edit.MassEditClientsModule import MassEditClientsModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
#import allure
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class GlobalTablePageUI(CRMBasePage):

    def set_data_column_field(self, column, data):
        sleep(0.1)
        field = super().wait_load_element("(//input[@placeholder='%s'])[1]" % column)
        field.clear()
        field.send_keys(data)
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        Logging().reportDebugStep(self, "Search by column: " + column + " with data: " + data)
        return GlobalTablePageUI(self.driver)

    def select_data_column_field(self, column, data):
        sleep(0.1)
        field = super().wait_element_to_be_clickable("//span[@class='placeholder']/span[text()='%s']" % column)
        field.click()
        sleep(0.5)
        item = super().wait_load_element("//span[text()='%s']" % data)
        self.driver.execute_script("arguments[0].click();", item)
        try:
            done = super().wait_element_to_be_clickable("//button[@class='btn-save']")
            self.driver.execute_script("arguments[0].click();", done)
        except:
            pass
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        Logging().reportDebugStep(self, "Search by column: " + column + " with data: " + data)
        return GlobalTablePageUI(self.driver)

    """
        Check every line of table contain needed string:
    """

    def global_data_checker_new_ui(self, data):
        try:
            table = self.driver.find_element_by_xpath("//tbody[@role='rowgroup']")
            row_count = 0
            for tr in table.find_elements_by_xpath("//tbody[@role='rowgroup']/tr[not (contains(@style,'hidden'))]"):
                assert data.lower() in tr.text.lower()
                row_count += 1
            Logging().reportDebugStep(self, data + " is verified in " + str(row_count) + " rows")
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            super().wait_visible_of_element\
                ("//span[@class='genHeaderSmall message_title' and contains(text(),'There are no')]")
            Logging().reportDebugStep(self, "There are no documents that match the search criteria!")
        return GlobalTablePageUI(self.driver)

    def select_all_records(self):
        sleep(0.2)
        all_records_checkbox = super().wait_element_to_be_clickable(
            "//th[@role='columnheader']//label[@class='mat-checkbox-layout']")
        all_records_checkbox.click()
        Logging().reportDebugStep(self, "All records on the page were selected")
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
        message = super().wait_load_element("//div[@class='dialog-content-success mat-dialog-content']").text
        assert "success" in message.lower()
        Logging().reportDebugStep(self, "Get message: " + message)
        return GlobalTablePageUI(self.driver)

    """
        Click OK button
    """

    def click_ok(self):
        sleep(0.1)
        button = super().wait_element_to_be_clickable("//*[text()=' OK ']")
        self.driver.execute_script("arguments[0].click();", button)
        Logging().reportDebugStep(self, "OK button was clicked")
        return GlobalTablePageUI(self.driver)

    def select_filter_new_ui(self, test_filter):
        sleep(0.1)
        filter_item = super().wait_load_element("//span[contains(text(),'%s')]" % test_filter)
        self.driver.execute_script("arguments[0].click();", filter_item)
        Logging().reportDebugStep(self, "Select filter: " + test_filter)
        sleep(1)
        self.wait_crm_loading_to_finish()
        return GlobalTablePageUI(self.driver)
