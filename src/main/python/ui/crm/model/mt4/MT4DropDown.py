from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.utils.logs.Loging import Logging

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
            Logging().reportDebugStep(self, "Module does not exist")
        time.sleep(1)

