from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsDetailsPageUI import LeadsDetailsPageUI
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class LeadsModulePageUI(CRMBasePage):

    def open_lead(self, row):
        sleep(0.5)
        lead_no = super().wait_element_to_be_clickable(
            "(//span[@class='td-link' and contains(text(),'LEA')])[%s]" % row)
        lead_no.click()
        sleep(1)
        self.wait_loading_to_finish_new_ui(15)
        Logging().reportDebugStep(self, "Click on Lead No")
        return LeadsDetailsPageUI(self.driver)
