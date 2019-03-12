from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
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
import allure
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config

class LeaderboardPage(CRMBasePage):

    def refresh(self):
        self.driver.refresh()
        Logging().reportDebugStep(self, "Perform the refresh ")
        return LeaderboardPage(self.driver)

    def choose_group(self):
        sleep(3)
        select_btn = super().wait_element_to_be_clickable("//span[@id='select2-groupid-container']")
        select_btn.click()
        Logging().reportDebugStep(self, "Click select all")
        return LeaderboardPage(self.driver)

    def enter_name_group(self, group):
        input_group = super().wait_load_element("//input[@class='select2-search__field']")
        input_group.send_keys(group)
        Logging().reportDebugStep(self, "Enter name group")
        return LeaderboardPage(self.driver)

    def click_button_go(self):
        element = super().wait_load_element("//input[@class='btn btn-primary']")
        element.click()
        Logging().reportDebugStep(self, "Click Go")
        return LeaderboardPage(self.driver)

