from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class ChangeClientPassword(CRMBasePage):

    def set_password(self, password):
        time_element = self.wait_element_to_be_clickable("//*[@id='NewPassword']")
        time_element.clear()
        time_element.send_keys(password)
        Logging().reportDebugStep(self, "The new password is set to: %s" % password)
        return ChangeClientPassword(self.driver)

    def click_change(self):
        button = self.wait_load_element("//*[@id='resetpassform']/div[3]/button[2]")
        button.click()
        Logging().reportDebugStep(self, "The Change button was clicked")
