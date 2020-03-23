from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.client_modules.mass_sms.SendSMSClientsModule import SendSMSClientsModule
from src.main.python.ui.crm.model.modules.client_modules.send_email.SendEmailClientsModule import SendEmailClientsModule
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskPage import HelpDeskPage
from src.main.python.ui.crm.model.modules.client_modules.mass_assign.MassAssignClientsModule import \
    MassAssignClientsModule
from src.main.python.ui.crm.model.modules.client_modules.mass_edit.MassEditClientsModule import MassEditClientsModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.utils.logs.Loging import Logging
#import allure
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class GlobalDetailsPageUI(CRMBasePage):

    def open_tab_ui(self, tab):
        sleep(0.1)
        Logging().reportDebugStep(self, "Open " + tab + " tab")
        tab_name = super().wait_load_element("//mat-panel-title/div[contains(text(),'%s')]" % tab)
        self.driver.execute_script("arguments[0].click();", tab_name)
        self.wait_loading_to_finish_new_ui(8)
        return ClientProfilePage(self.driver)

    def get_text_from_field(self, field):
        sleep(0.1)
        try:
            data = super().wait_load_element(
                "//div[label='%s']//following-sibling::button/span[contains(@class,'btn-txt-wrapper')]" % field,
                timeout=5).text
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Field " + field + " is not editable")
            data = super().wait_load_element(
                "//div[label='%s']//following-sibling::div//div[@class='ng-star-inserted']" % field).text
        Logging().reportDebugStep(self, "Get data from field " + field + ": " + data)
        return data

    def click_edit_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click Edit button")
        edit_btn = super().wait_load_element(
            "//div[@class='wrap-navigation d-flex align-items-center']//button[span[i[contains(@class,'pencil')]]]")
        edit_btn.click()
        return GlobalDetailsPageUI(self.driver)
