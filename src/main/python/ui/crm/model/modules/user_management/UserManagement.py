from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.user_management.NewUserProfileModule import NewUserProfileModule
from src.main.python.utils.logs.Loging import Logging


class UserManagement(CRMBasePage):
    def __init__(self) -> None:
        super().__init__()

    def click_new_user_module(self):
        new_user_button = super().wait_element_to_be_clickable("//button[contains(text(),'New User')]")
        new_user_button.click()
        Logging().reportDebugStep(self, "The user profile was opened ")
        return NewUserProfileModule()
