from scr.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from scr.main.python.ui.brand.model.client_area_modules.account_details.tabs.change_password.CaChangePasswordTab import CaChangePasswordTab
from scr.main.python.ui.brand.model.client_area_modules.account_details.tabs.personal_information.CaPersonalInformationTab import \
    CaPersonalInformationTab
from scr.main.python.utils.logs.Loging import Logging


class CaAccountDetails(BrandBasePage):
    def __init__(self):
        super().__init__()

    def open_change_password_tab(self):
        change_password = super().wait_load_element("//a[contains(text(),'Change Password')]")
        change_password.click()
        Logging().reportDebugStep(self, "Change Password is opened " + '\n')
        return CaChangePasswordTab()

    def open_personal_information_tab(self):
        personal_detail_tab = super().wait_load_element("//a[contains(text(),'Personal Information')]")
        personal_detail_tab.click()
        Logging().reportDebugStep(self, "Change Password is opened " + '\n')
        return CaPersonalInformationTab()
