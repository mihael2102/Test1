from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class CheckClientPassword(CRMBasePage):

    def set_password_to_check(self, password):
        time_element = self.wait_element_to_be_clickable("//*[@id='pwd_password']")
        time_element.clear()
        time_element.send_keys(password)
        Logging().reportDebugStep(self, "The password to check is set to: %s" % password)
        return CheckClientPassword(self.driver)

    def click_check(self):
        button = self.wait_load_element("//*[@id='mtpassword']/div[2]/button[2]")
        button.click()
        Logging().reportDebugStep(self, "The Check button was clicked")
