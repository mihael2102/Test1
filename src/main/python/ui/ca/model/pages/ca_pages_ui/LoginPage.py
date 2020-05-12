from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.ca_pages_ui.MainPage import MainPage
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class LoginPage(CRMBasePage):

    def login(self, email, password):
        self.click_login_btn()
        self.set_email(email)
        self.set_password(password)
        self.click_login()
        return MainPage(self.driver)

    def open_second_tab_page(self, url):
        super().open_second_tab_page(url)
        Logging().reportDebugStep(self, "Open second tab page: " + url)
        return LoginPage(self.driver)

    def click_login_btn(self):
        try:
            sleep(1)
            login_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                self.__class__.__name__)["login_btn"])
            self.driver.execute_script("arguments[0].click();", login_button)
            Logging().reportDebugStep(self, "Click 'Login' button")
        except:
            Logging().reportDebugStep(self, "There is no panda's plugin")
            Logging().reportDebugStep(self, "NOT RUNNED")
        return LoginPage(self.driver)

    def set_email(self, email):
        sleep(0.5)
        input_email = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["login_email_input"])
        self.driver.execute_script("arguments[0].click();", input_email)
        sleep(0.1)
        input_email.send_keys(email)
        Logging().reportDebugStep(self, "Enter Email: " + email)
        return LoginPage(self.driver)

    def set_password(self, password):
        sleep(0.1)
        input_password = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["login_password_input"])
        self.driver.execute_script("arguments[0].click();", input_password)
        sleep(0.1)
        input_password.send_keys(password)
        Logging().reportDebugStep(self, "Enter Password: " + password)
        return LoginPage(self.driver)

    def click_login(self):
        login_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
            self.__class__.__name__)["login_btn_2"])
        try:
            login_button.click()
        except:
            self.driver.execute_script("arguments[0].click();", login_button)
        Logging().reportDebugStep(self, "Click Login in pop up")
        return LoginPage(self.driver)
