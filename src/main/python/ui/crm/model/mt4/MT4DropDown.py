from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class MT4DropDown(CRMBasePage):

    def mt4_actions(self, module):
        time.sleep(5)
        try:
            selected_module = self.driver.find_element(By.XPATH,
                                                       "//a[@class='webMnu act_btn btn btn-primary'][%s]" % module)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", selected_module)
            Logging().reportDebugStep(self, module + " module is opened")
        except (TimeoutException, NoSuchElementException):
            pass
            Logging().reportDebugStep(self, "Module does not exist (NOT RUNNED)")
        time.sleep(1)

    def open_mt4_module(self, module):
        mt4_button = super().wait_load_element("//div[@class='mt4_act_box']", timeout=35)
        sleep(1)
        try:
            mt4_button.click()
        except:
            self.driver.execute_script("arguments[0].click();", mt4_button)
        Logging().reportDebugStep(self, "Open MT4 Actions")
        try:
            selected_module = self.driver.find_element_by_xpath("//a[text()='%s']" % module)
            sleep(1)
            self.driver.execute_script("arguments[0].click();", selected_module)
            Logging().reportDebugStep(self, module + " module is opened")
        except (TimeoutException, NoSuchElementException):
            pass
            Logging().reportDebugStep(self, "Module does not exist (NOT RUNNED)")

    def open_mt4_module_newui(self, module):
        try:
            sleep(0.2)
            module_item = super().wait_load_element("//div[text()=' %s ']" % module)
            self.driver.execute_script("arguments[0].click();", module_item)
            Logging().reportDebugStep(self, module + " module is opened")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Module does not exist (NOT RUNNED)")
