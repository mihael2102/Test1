from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import time
from selenium.webdriver.common.by import By

class MT4DropDown(CRMBasePage):

    def mt4_actions(self, module):
        time.sleep(5)
        selected_module = self.driver.find_element(By.XPATH,
                                                   "//a[@class='webMnu act_btn btn btn-primary'][%s]" % module)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", selected_module)
        time.sleep(1)
        # selected_module.click()
