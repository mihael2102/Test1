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
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class ClientsModulePage(CRMBasePage):

    def get_client_crm_id_list_view(self, row):
        sleep(0.5)
        crm_id = super().wait_load_element("//tr[contains(@id,'row')][%s]//a[contains(@title,'ACC')]" % row).text
        Logging().reportDebugStep(self, "Get CRM ID from list view(row = " + row + "): " + crm_id)
        return crm_id

    def get_client_created_time_list_view(self, row):
        sleep(0.5)
        created_time = super().wait_load_element\
            ("//tr[contains(@id,'row')][%s]/td[contains(text(),'2019') or contains(text(),'2020')]" % row)\
            .get_attribute("innerText")
        Logging().reportDebugStep(self, "Get Created Time from list view(row = " + row + "): " + created_time)
        return created_time

    def get_client_status_list_view(self, row):
        sleep(0.5)
        client_status = super().wait_load_element \
            ("//tr[contains(@id,'row')][%s]/td[contains(text(),'2019') or contains(text(),'2020')]" % row) \
            .get_attribute("innerText")
        Logging().reportDebugStep(self, "Get Created Time from list view(row = " + row + "): " + client_status)
        return client_status

    def set_data_to_email_column_search_field(self, email):
        sleep(0.1)
        email_field = super().wait_load_element("//input[@id='tks_email1']")
        email_field.clear()
        email_field.send_keys(email)
        Logging().reportDebugStep(self, "Set data to Email field: " + email)
        return ClientsModulePage(self.driver)

    def click_search_btn(self):
        search_button = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        search_button.click()
        Logging().reportDebugStep(self, "Click Search button")
        sleep(1)
        self.wait_vtiger_loading_to_finish_custom(35)
        return ClientsModulePage(self.driver)

    def click_crm_id_list_view(self, row):
        sleep(0.5)
        crm_id = super().wait_load_element("//tr[contains(@id,'row')][%s]//a[contains(@title,'ACC')]" % row)
        self.driver.execute_script("arguments[0].click();", crm_id)
        Logging().reportDebugStep(self, "Open client's details page")
        return ClientsModulePage(self.driver)
