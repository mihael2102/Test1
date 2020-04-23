from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalPopupPageUI import GlobalPopupPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.utils.logs.Loging import Logging


class HelpDeskDetailsPageUI(CRMBasePage):

    def get_text_from_field(self, field):
        data = GlobalDetailsPageUI(self.driver)\
            .get_text_from_field(field)
        return data

    def open_tab(self, title):
        GlobalDetailsPageUI(self.driver)\
            .open_tab(title)
        return HelpDeskDetailsPageUI(self.driver)
