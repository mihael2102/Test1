from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.help_desk_ui.HelpDeskDetailsPageUI import HelpDeskDetailsPageUI
from src.main.python.utils.logs.Loging import Logging


class HelpDeskModulePageUI(CRMBasePage):

    def open_ticket(self):
        sleep(0.1)
        ticket_no = super().wait_element_to_be_clickable("//span[contains(text(),'TT')]")
        ticket_no.click()
        sleep(1)
        self.wait_loading_to_finish_new_ui(15)
        Logging().reportDebugStep(self, "Click Ticket number")
        return HelpDeskDetailsPageUI(self.driver)
