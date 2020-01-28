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


class FilterPageUI(CRMBasePage):

    def create_filter_clients_ui(self, field1=None, view_name=None):
        self.click_create_filter_btn()
        if view_name:
            self.set_text_field(field1, view_name)

    def click_create_filter_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Create Filter' button")
        btn = super().wait_element_to_be_clickable("//button[@title='Create Filter']")
        btn.click()
        return FilterPageUI(self.driver)

    def set_text_field(self, title, text):
        sleep(0.1)
        field = super().wait_load_element(
            "//div[label[contains(text(),'%s')]]//following-sibling::mat-form-field//input" % title)
        field.clear()
        field.send_keys(text)
        Logging().reportDebugStep(self, "Set '" + text + "' to '" + title + "' field")
        return FilterPageUI(self.driver)

    def select_from_list(self, pick_list, item_title):
        sleep(0.1)
        item = super().wait_load_element(
            "//span[text()=' %s ']//following-sibling::ul//span[text()='%s']" % (pick_list, item_title))
        self.driver.execute_script("arguments[0].click();", item)
        Logging().reportDebugStep(self, "Select '" + item_title + "' from pick list " + pick_list)
        return FilterPageUI(self.driver)

    def click_assign_btn(self):
        sleep(0.1)
        assign_btn = super().wait_element_to_be_clickable("//button/span[text()=' Assign ']")
        self.driver.execute_script("arguments[0].click();", assign_btn)
        sleep(1)
        self.wait_loading_to_finish_new_ui(5)
        Logging().reportDebugStep(self, "Click 'Assign' button")
        return FilterPageUI(self.driver)
