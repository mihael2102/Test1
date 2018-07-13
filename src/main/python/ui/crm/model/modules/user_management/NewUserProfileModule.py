from selenium.webdriver.common.by import By

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.utils.logs.Loging import Logging


class NewUserProfileModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    def perform_create_user(self, user_name, email, first_name, role, password, confirm_password, last_name):
        self.set_user_name(user_name)
        self.email(email)
        self.first_name(first_name)
        self.set_role(role)
        self.set_password(password)
        self.set_confirm_password(confirm_password)
        self.last_name(last_name)
        return NewUserProfileModule()

    def set_user_name(self, user_name):
        user_name_field = super().wait_element_to_be_clickable("//input[@name='user_name']")
        user_name_field.clear()
        user_name_field.send_keys(user_name)
        Logging().reportDebugStep(self, "The event status is set ")
        return NewUserProfileModule()

    def email(self, email):
        email_field = self.driver.find_element(By.XPATH, "//input[@name='email1']")
        email_field.clear()
        email_field.send_keys(email)
        Logging().reportDebugStep(self, "The event status is set ")
        return NewUserProfileModule()

    def first_name(self, first_name):
        first_name_field = super().wait_element_to_be_clickable("//input[@name='first_name']")
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        Logging().reportDebugStep(self, "The event status is set ")
        return NewUserProfileModule()

    def set_role(self, role):
        role_field = self.driver.find_element(By.XPATH, "//input[@name='role_name']")
        role_field.click()
        handle = self.driver.window_handles[1]
        self.driver.switch_to_window(handle)
        search_button = super().wait_element_to_be_clickable("//a[contains(text(),'%s')]" % role)
        search_button.click()
        Logging().reportDebugStep(self, "The rol was set ")
        return NewUserProfileModule()

    def set_password(self, _password):
        handle = self.driver.window_handles[0]
        self.driver.switch_to_window(handle)
        password_field = self.driver.find_element(By.XPATH, "//input[@name='user_password']")
        password_field.clear()
        password_field.send_keys(_password)
        Logging().reportDebugStep(self, "The event status is set ")
        return NewUserProfileModule()

    def set_confirm_password(self, confirm_password):
        confirm_password_field = super().wait_element_to_be_clickable("//input[@name='confirm_password']")
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)
        Logging().reportDebugStep(self, "The event status is set ")
        return NewUserProfileModule()

    def last_name(self, last_name):
        last_name_field = super().wait_element_to_be_clickable("//input[@name='last_name']")
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        Logging().reportDebugStep(self, "The event status is set ")
        return NewUserProfileModule()

    def click_save_button_user_module(self):
        save_button = super().wait_element_to_be_clickable("//button[contains(text(),'Save')]")
        save_button.click()
        Logging().reportDebugStep(self, "The save button was clicked")
        return NewUserProfileModule()
