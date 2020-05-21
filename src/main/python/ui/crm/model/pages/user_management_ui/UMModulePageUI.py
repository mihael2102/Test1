from time import sleep
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class UMModulePageUI(CRMBasePage):

    """ Get current logged in user name """
    def get_login_user_name(self):
        sleep(0.1)
        name = super().wait_load_element("//div[@class='user-name']").text
        Logging().reportDebugStep(self, "Get current user name: " + name)
        return name

    def click_login_as_sign_out(self):
        sleep(0.1)
        sing_out = super().wait_load_element("//div[@class='sign-out']")
        sing_out.click()
        sleep(0.5)
        self.wait_loading_to_finish_new_ui(35)
        Logging().reportDebugStep(self, "Click 'Sign Out' in Logged in mode")
        return UMModulePageUI(self.driver)
