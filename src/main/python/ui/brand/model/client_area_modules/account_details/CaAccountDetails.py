from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.client_area_modules.account_details.tabs.change_password.CaChangePasswordTab import \
    CaChangePasswordTab
from src.main.python.ui.brand.model.client_area_modules.account_details.tabs.personal_information.CaPersonalInformationTab import \
    CaPersonalInformationTab
from src.main.python.utils.logs.Loging import Logging


class CaAccountDetails(BrandBasePage):
    def __init__(self):
        super().__init__()

    def open_change_password_tab(self):
        change_password = super().wait_load_element_present("//a[contains(text(),'Change Password')]")
        change_password.click()
        Logging().reportDebugStep(self, "Change Password module is opened ")
        return CaChangePasswordTab()

    def open_personal_information_tab(self):
        personal_detail_tab = super().wait_load_element_present("//a[contains(text(),'Personal Information')]")
        personal_detail_tab.click()
        Logging().reportDebugStep(self, "Personal Information module is opened ")
        return CaPersonalInformationTab()
