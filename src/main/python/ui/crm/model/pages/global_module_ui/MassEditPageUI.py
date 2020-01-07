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
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class MassEditPageUI(CRMBasePage):

    def select_field_to_edit(self, field):
        sleep(0.1)
        item = super().wait_element_to_be_clickable(
            "//div[h3=' Choose fields to edit: ']//span[contains(text(),'%s')]" % field)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select '" + field + "' check box")
        return MassEditPageUI(self.driver)

    def set_users_field(self, user):
        sleep(0.1)
        users_field = super().wait_element_to_be_clickable("//input[@placeholder='Search users']")
        users_field.clear()
        users_field.send_keys(user)
        Logging().reportDebugStep(self, "Set '" + user + "' to Users field")
        return MassAssignPageUI(self.driver)

    def select_user_by_title(self, user):
        sleep(0.1)
        user_item = super().wait_element_to_be_clickable(
            "//div[@class='options-wrap ng-star-inserted']//span[contains(text(),'%s')]" % user)
        self.driver.execute_script("arguments[0].click();", user_item)
        Logging().reportDebugStep(self, "Select '" + user + "' from list")
        return MassAssignPageUI(self.driver)

    def select_status(self, status):
        sleep(0.1)
        item = super().wait_load_element("//div[@class='row client-status-wrap']//span[text()='%s']" % status)
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select '" + status + "' status")
        return MassAssignPageUI(self.driver)

    def click_assign_btn(self):
        sleep(0.1)
        assign_btn = super().wait_element_to_be_clickable("//button/span[text()=' Assign ']")
        self.driver.execute_script("arguments[0].click();", assign_btn)
        Logging().reportDebugStep(self, "Click 'Assign' button")
        return MassAssignPageUI(self.driver)
