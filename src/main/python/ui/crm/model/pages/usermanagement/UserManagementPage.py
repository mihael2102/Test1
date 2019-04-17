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

class UserManagementPage(CRMBasePage):

    def refresh(self):
        self.driver.refresh()
        Logging().reportDebugStep(self, "Perform the refresh ")
        return UserManagementPage(self.driver)

    def check_user_management_tab(self):
        sleep(2)
        tab_name = super().wait_load_element("//*[@id='nav_tab_users']/a")
        Logging().reportDebugStep(self, "Check name tab User Management")
        return tab_name.text

    def check_table_loaded(self):
        sleep(5)
        table = super().wait_load_element("//div[@id='row5userManagement']/div[5]//a")
        Logging().reportDebugStep(self, "Check table loaded")
        return table.text

    def click_new_user_module(self):
        sleep(2)
        new_user_button = super().wait_element_to_be_clickable("//button[contains(text(),'New User')]")
        new_user_button.click()
        Logging().reportDebugStep(self, "The user profile was opened ")
        return UserManagementPage(self.driver)

    def set_user_name(self, user_name):
        user_name_field = super().wait_element_to_be_clickable("//input[@name='user_name']")
        user_name_field.clear()
        user_name_field.send_keys(user_name)
        Logging().reportDebugStep(self, "The user name was set " + user_name)
        return UserManagementPage(self.driver)

    def email(self, email):
        email_field = self.driver.find_element(By.XPATH, "//input[@name='email1']")
        email_field.clear()
        email_field.send_keys(email)
        Logging().reportDebugStep(self, "The email was set: " + email)
        return UserManagementPage(self.driver)

    def first_name(self, first_name):
        first_name_field = super().wait_element_to_be_clickable("//input[@name='first_name']")
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "The first name was set: " + first_name)
        return UserManagementPage(self.driver)

    def set_role(self, role):
        role_field = self.driver.find_element(By.XPATH, "//input[@name='role_name']")
        role_field.click()
        handle = self.driver.window_handles[1]
        self.driver.switch_to_window(handle)
        search_button = super().wait_element_to_be_clickable("//a[contains(text(),'%s')]" % role)
        search_button.click()
        Logging().reportDebugStep(self, "The role was set: " + role)
        return UserManagementPage(self.driver)

    def set_password(self, password):
        handle = self.driver.window_handles[0]
        self.driver.switch_to_window(handle)
        password_field = self.driver.find_element(By.XPATH, "//input[@name='user_password']")
        password_field.clear()
        password_field.send_keys(password)
        Logging().reportDebugStep(self, "The password was set: " + password)
        return UserManagementPage(self.driver)

    def set_confirm_password(self, confirm_password):
        confirm_password_field = super().wait_element_to_be_clickable("//input[@name='confirm_password']")
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)
        Logging().reportDebugStep(self, "The confirm password  was set: " + confirm_password)
        return UserManagementPage(self.driver)

    def last_name(self, last_name):
        last_name_field = super().wait_element_to_be_clickable("//input[@name='last_name']")
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "The last name was set: " + last_name)
        return UserManagementPage(self.driver)

    def click_save_button_user_module(self):
        save_button = super().wait_element_to_be_clickable("//button[contains(text(),'Save')]")
        save_button.click()
        Logging().reportDebugStep(self, "The save button was clicked")
        return UserManagementPage(self.driver)