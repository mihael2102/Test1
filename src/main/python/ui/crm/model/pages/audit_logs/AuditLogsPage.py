from time import sleep

#from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging
from datetime import *
#import allure


class AuditLogsPage(CRMBasePage):

    def get_all_tab_text(self):
        all_tab = super().wait_element_to_be_clickable("//button[contains(text(),'All')]")
        all_tab.click()
        tab_text = self.driver.find_element(By.XPATH, "//button[contains(text(),'All')]")
        Logging().reportDebugStep(self, "Returns the tab name " + tab_text.text)
        return tab_text.text

    def perform_screen_shot(self):
        sleep(3)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        file_name = 'D:/automation-newforexqa/screenshots/audit_logs/audit logs_module screenshot %s.png' % now
        self.driver.get_screenshot_as_file(file_name)
        #allure.MASTER_HELPER.attach('screenshot',  self.driver.get_screenshot_as_png(),
        #                            type=AttachmentType.PNG)
        Logging().reportDebugStep(self, "The screenshot was performed ")
        return AuditLogsPage()

    def open_calendar_view(self):
        all_tab = super().wait_element_to_be_clickable(
            "//div[@class='module-header-date-filter']//span[@id='basic-addon2']")
        all_tab.click()
        Logging().reportDebugStep(self, "The calendar view was opened ")
        return AuditLogsPage(self.driver)

    def get_today_tab_text(self):
        today_tab = super().wait_element_to_be_clickable("//button[contains(text(),'Today')]")
        today_tab.click()
        today_tab_text = self.driver.find_element(By.XPATH, "//button[contains(text(),'Today')]")
        Logging().reportDebugStep(self, "Returns the tab name " + today_tab_text.text)
        return today_tab_text.text

    def get_week_tab_text(self):
        week_tab = super().wait_element_to_be_clickable("//button[contains(text(),'Week')]")
        week_tab.click()
        week_tab_text = self.driver.find_element(By.XPATH, "//button[contains(text(),'Week')]")
        Logging().reportDebugStep(self, "Returns the tab name " + week_tab_text.text)
        return week_tab_text.text

    def get_month_tab_text(self):
        month_tab = super().wait_element_to_be_clickable("//button[contains(text(),'Month')]")
        month_tab.click()
        month_tab_text = self.driver.find_element(By.XPATH, "//button[contains(text(),'Month')]")
        Logging().reportDebugStep(self, "Returns the tab name " + month_tab_text.text)
        return month_tab_text.text

    def perform_searching(self, module, action, user, email, id_record, user_agent):
        self.select_module_audit_logs(module)
        self.select_action_audit_logs(action)
        self.select_user_audit_logs(user)
        self.enter_id_record(id_record)
        self.enter_email_audit_logs(email)
        self.select_user_agent(user_agent)
        return AuditLogsPage(self.driver)

    def searching_by_2_columns(self, module, action):
        self.select_module_audit_logs(module)
        self.select_action_audit_logs(action)
        return AuditLogsPage(self.driver)

    def select_module_audit_logs(self, module):
        module_drop_down = super().wait_element_to_be_clickable("(//button[text()='None selected'])[1]")
        module_drop_down.click()
        search_field = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        search_field.clear()
        search_field.send_keys(module)
        module_choice = self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % module)
        module_choice.click()
        ac = ActionChains(self.driver)
        ac.move_by_offset(250, 250).click().perform()
        self.wait_crm_loading_to_finish_tasks(35)
        Logging().reportDebugStep(self, "The Module was set: " + module)
        return AuditLogsPage(self.driver)

    def select_action_audit_logs(self, action):
        action_drop_down = super().wait_element_to_be_clickable("(//button[text()='None selected'])[1]")
        action_drop_down.click()
        search_field = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        search_field.clear()
        search_field.send_keys(action)
        action_choice = self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % action)
        action_choice.click()
        ac = ActionChains(self.driver)
        ac.move_by_offset(250, 250).click().perform()
        self.wait_crm_loading_to_finish_tasks(35)
        Logging().reportDebugStep(self, "The Action was set: " + action)
        return AuditLogsPage(self.driver)

    def select_user_audit_logs(self, user):
        user_drop_down = super().wait_element_to_be_clickable("//tr[@class='tableFilters']//td[3]")

        user_drop_down.click()
        search_field = self.driver.find_element(By.XPATH,
                                                "//div[@class='select-options options-enabled']//input")
        search_field.clear()
        search_field.send_keys(user)
        action_choice = self.driver.find_element(By.XPATH,
                                                 "//div[@class='select-options options-enabled']//"
                                                 "span[contains(text(),'%s')]" % user)
        action_choice.click()

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The user was entered : " + user)

        return AuditLogsPage()

    def enter_id_record(self, id_record):
        id_record_element = super().wait_element_to_be_clickable("//tr[@class='tableFilters']//td[4]//input")
        id_record_element.clear()
        id_record_element.send_keys(id_record)

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The id_record was entered : " + id_record)
        return AuditLogsPage()

    def select_user_agent(self, user_agent):
        super().wait_element_to_be_clickable("//tr[@class='tableFilters']//td[8]")

        search_field = Select(self.driver.find_element(By.XPATH,
                                                       "//tr[@class='tableFilters']//td[8]//select"))
        search_field.select_by_visible_text(user_agent)

        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        Logging().reportDebugStep(self, "The user_agent was entered : " + user_agent)
        return AuditLogsPage()

    def enter_email_audit_logs(self, email):
        search_field = self.driver.find_element(By.XPATH,
                                                "//tr[@class='tableFilters']//td[5]//input")
        search_field.clear()
        search_field.send_keys(email)
        ac = ActionChains(self.driver)

        ac.move_by_offset(250, 250).click().perform()
        return AuditLogsPage()

    def check_audit_logs_loaded(self):
        sleep(2)
        super().wait_load_element("(//tr[contains(@class,'tableRow')])[1]", timeout=35)
        Logging().reportDebugStep(self, "Audit Logs module is loaded")
        return AuditLogsPage(self.driver)

    def audit_logs_data_checker(self, data):
        sleep(2)
        try:
            table = self.driver.find_element_by_xpath("//div[@class='table-grid-container of-auto']/table/tbody")
            row_count = 0
            for tr in table.find_elements_by_xpath("//tr[@class='tableRow ng-star-inserted' and @data-loadtime]"):
                if tr.text:
                    data = data.replace(" ", "")
                    row_text = tr.text.replace(" ", "")
                    assert data.lower() in row_text.lower()
                    row_count += 1
            Logging().reportDebugStep(self, data + " is verified in " + str(row_count) + " rows")
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            super().wait_visible_of_element("//td[text()=' Data not found ']")
            Logging().reportDebugStep(self, "Data not found")
        return AuditLogsPage(self.driver)
