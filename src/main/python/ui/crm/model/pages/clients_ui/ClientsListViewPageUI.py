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


class ClientsListViewPageUI(CRMBasePage):

    def set_data_column_field(self, column, data):
        sleep(0.1)
        field = super().wait_load_element("(//input[@placeholder='%s'])[1]" % column)
        field.clear()
        field.send_keys(data)
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        Logging().reportDebugStep(self, "Search by column: " + column + " with data: " + data)
        return ClientsListViewPageUI(self.driver)

    def select_data_column_field(self, column, data):
        sleep(0.1)
        field = super().wait_element_to_be_clickable("//span[@class='placeholder']/span[text()='%s']" % column)
        field.click()
        sleep(0.5)
        item = super().wait_load_element("//span[text()='%s']" % data)
        self.driver.execute_script("arguments[0].click();", item)
        done = super().wait_element_to_be_clickable("//button[@class='btn-save']")
        self.driver.execute_script("arguments[0].click();", done)
        sleep(1)
        self.wait_loading_to_finish_new_ui(25)
        Logging().reportDebugStep(self, "Search by column: " + column + " with data: " + data)
        return ClientsListViewPageUI(self.driver)
