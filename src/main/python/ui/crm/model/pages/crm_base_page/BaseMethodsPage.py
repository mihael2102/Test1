from time import sleep
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
import autoit
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.main.python.ui.crm.model.pages.crm_base_page.GlobalSearchPage import GlobalSearchPage
from src.main.python.ui.crm.model.pages.crm_base_page.ModuleSearchPage import ModuleSearchPage
from datetime import datetime
import os


class CRMBaseMethodsPage(CRMBasePage):

    def select_all_records(self):
        sleep(0.2)
        all_records_checkbox = super().wait_element_to_be_clickable("//*[@id='selectCurrentPageRec']")
        all_records_checkbox.click()
        Logging().reportDebugStep(self, "All records on the page were selected")
        return CRMBaseMethodsPage(self.driver)

    '''
        Check every line of table contain needed string:
    '''

    def global_data_checker(self, data):
        try:
            table = self.driver.find_element_by_xpath("//*[@id='listBody']")
            row_count = 0
            for tr in table.find_elements_by_tag_name("tr"):
                assert data.lower() in tr.text.lower()
                row_count += 1
            Logging().reportDebugStep(self, data + " is verified in " + str(row_count) + " rows")
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            super().wait_visible_of_element\
                ("//span[@class='genHeaderSmall message_title' and contains(text(),'There are no')]")
            Logging().reportDebugStep(self, "There are no documents that match the search criteria!")
        return CRMBaseMethodsPage(self.driver)

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
        return CRMBaseMethodsPage(self.driver)

    def open_tab_list_view(self, tab_title):
        tab = super().wait_element_to_be_clickable("//li[contains(text(),'%s')]" % tab_title)
        tab.click()
        self.wait_vtiger_loading_to_finish_custom(35)
        self.wait_crm_loading_to_finish_tasks(35)
        Logging().reportDebugStep(self, "Tab " + tab_title + " was opened")
        return CRMBaseMethodsPage(self.driver)

    def open_module(self, module_title):
        try:
            module = super().wait_load_element("//div[@class='content-menu']//span[contains(text(), '%s')]"
                                               % module_title)
            self.driver.execute_script("arguments[0].click();", module)
            self.wait_vtiger_loading_to_finish_custom(35)
            self.wait_crm_loading_to_finish_tasks(35)
            self.wait_loading_to_finish_new_ui(35)
            Logging().reportDebugStep(self, "Module " + module_title + " was opened")
            return CRMBaseMethodsPage(self.driver)
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Module " + module_title + " does not exist")

    def global_search_vtiger(self, item):
        search_field = super().wait_load_element("//input[@class='searchBox']")
        search_field.clear()
        search_field.send_keys(item)
        search_btn = super().wait_load_element("//button[@class='searchBtn']")
        self.driver.execute_script("arguments[0].click();", search_btn)
        Logging().reportDebugStep(self, "Global Search by data: " + item)
        return GlobalSearchPage(self.driver)

    def global_search_laravel(self, item):
        search_field = super().wait_load_element("//input[@class='form-control']")
        search_field.clear()
        search_field.send_keys(item)
        search_btn = super().wait_load_element("//button/i[@class='glyphicons search']")
        self.driver.execute_script("arguments[0].click();", search_btn)
        Logging().reportDebugStep(self, "Global Search by data: " + item)
        return GlobalSearchPage(self.driver)

    def comparator_string(self, item1, item2):
        try:
            assert item1 == item2
            Logging().reportDebugStep(self, item1 + " is equal to " + item2)
            return CRMBaseMethodsPage(self.driver)
        except AssertionError:
            Logging().reportDebugStep(self, item1 + " is not equal to " + item2)
            assert item1 == item2

    """
        Method returns current server date:
    """

    def get_current_date(self):
        date = datetime.today().strftime('%Y-%m-%d')
        Logging().reportDebugStep(self, "Get current date: " + date)
        return date

    """
        Method returns current server date and time:
    """

    def get_current_date_time(self):
        date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        Logging().reportDebugStep(self, "Get current date and time: " + date)
        return date

    """
        Method gets title of column and returns index (str) of column in list view:
    """
    def get_column_number_by_title_vtiger(self, title):
        sleep(0.1)
        try:
            table = self.driver.find_element_by_xpath("//*[@id='resizeble_cols']/tbody[1]/tr[1]")
            count = 0
            index = ""
            for td in table.find_elements_by_tag_name("td"):
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
    def get_data_from_list_view_vtiger(self, column, row):
        column_number = self.get_column_number_by_title_vtiger(column)
        if column_number:
            data = super().wait_load_element("//*[@id='listBody']/tr[%s]/td[%s]" % (row, column_number)).text
            Logging().reportDebugStep(self,
                                      "Get data from list view (column = " + column + ", row = " + row + "): " + data)
            return data
        else:
            Logging().reportDebugStep(self, "Column '" + column + "' or row '" + row + "' does not exist")
            return False

    """
        Click on 'Search in ... module' button (magnifying glass):
    """
    def click_magnifying_glass_btn(self):
        sleep(0.5)
        glass_btn = super().wait_element_to_be_clickable("//button[contains(@title,'Search in')]")
        glass_btn.click()
        Logging().reportDebugStep(self, "Click 'Search in...' button (magnifying glass)")
        return ModuleSearchPage(self.driver)

    """
        Method checks, that message in pop up contains 'Success' and returns full text of message:
    """

    def verify_success_message(self):
        message = super().wait_load_element("//div[contains(@class,'dialog-content-success mat-dialog-content')]").text
        assert "success" in message.lower()
        Logging().reportDebugStep(self, "Get message: " + message)
        return CRMBaseMethodsPage(self.driver)

    def click_ok(self):
        button = self.wait_load_element("//span[contains(text(),'OK')]")
        button.click()
        Logging().reportDebugStep(self, "Ok button was clicked")
        return CRMBaseMethodsPage(self.driver)
