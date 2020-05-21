from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp


class CRMLoginPageUI(CRMBasePage):

    '''
        Login  to CRM 
        :parameter name pandaqa name
        :parameter password pandaqa password
        return Home Page instance    
    '''

    def crm_login(self, url=None, user_name=None, password=None, otp_secret=None):
        if url:
            self.open_first_tab_page(url)
        if user_name:
            self.set_user_name(user_name)
        if password:
            self.set_password(password)
        self.check_new_design()
        self.click_login_btn()
        sleep(1)
        if otp_secret:
            self.set_otp(otp_secret)
        sleep(1)
        self.close_news_popup()

    def crm_login_second_tab(self, url=None, user_name=None, password=None, otp_secret=None):
        if url:
            self.open_second_tab_page(url)
        if user_name:
            self.set_user_name(user_name)
        if password:
            self.set_password(password)
        self.check_new_design()
        self.click_login_btn()
        sleep(1)
        if otp_secret:
            self.set_otp(otp_secret)
        sleep(1)
        self.close_news_popup()

    def set_user_name(self, user_name):
        sleep(0.1)
        user_name_field = self.driver.find_element(By.XPATH, "//input[@id='user_name']")
        user_name_field.clear()
        user_name_field.send_keys(user_name)
        Logging().reportDebugStep(self, "Set User Name: " + user_name)
        return CRMLoginPageUI(self.driver)

    def set_password(self, password):
        sleep(0.1)
        password__field = self.driver.find_element(By.XPATH, "//input[@id='user_password']")
        password__field.clear()
        password__field.send_keys(password)
        Logging().reportDebugStep(self, "Set Password")
        return CRMLoginPageUI(self.driver)

    def check_new_design(self):
        sleep(0.1)
        check_box = self.driver.find_element(By.XPATH, "//label[@class='pure-material-checkbox']")
        flag = self.driver.find_element(By.XPATH, "//input[@id='new-ui-selected']").get_property("checked")
        if flag:
            Logging().reportDebugStep(self, "'LOGIN TO NEW CRM DESIGN' is already checked")
        else:
            check_box.click()
            Logging().reportDebugStep(self, "Check 'LOGIN TO NEW CRM DESIGN'")
        return CRMLoginPageUI(self.driver)

    def click_login_btn(self):
        login_button = self.driver.find_element(By.XPATH, "//input[@id='submitButton']")
        login_button.click()
        Logging().reportDebugStep(self, "Click the Login button")
        return CRMLoginPageUI(self.driver)

    def set_otp(self, otp_secret):
        try:
            otp_field = self.driver.find_element(By.XPATH, "//input[@id='otp']")
            submit_button = self.driver.find_element(By.XPATH, "//a[@id='submitButton2']")
            time_otp = pyotp.TOTP(otp_secret)
            otp = time_otp.now()
            otp_field.clear()
            otp_field.send_keys(otp)
            Logging().reportDebugStep(self, "Setting the otp token: " + otp + '\n')
            submit_button.click()
            Logging().reportDebugStep(self, "Click the submit button")
        except NoSuchElementException:
            Logging().reportDebugStep(self, "No OTP authentication is required")
        return CRMLoginPageUI(self.driver)

    def close_news_popup(self):
        try:
            do_not_show_again_checkbox = super().wait_element_to_be_clickable("//*[@id='do_not_show']", timeout=1)
            do_not_show_again_checkbox.click()
            close_window_button = super().wait_element_to_be_clickable(
                                        "//*[@id = 'whats_newcontent']//button[@aria-label = 'Close']", timeout=1)
            close_window_button.click()
            Logging().reportDebugStep(self, "'What's new' popup was closed")
        except (NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "'What's new' popup isn't displayed")
        return ClientsModulePageUI(self.driver)

    def open_second_tab_page(self, url):
        super().open_second_tab_page(url)
        Logging().reportDebugStep(self, "Open second tabs page: " + url + '\n')
        return CRMLoginPageUI(self.driver)

    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return CRMLoginPageUI(self.driver)

    '''
        Select the crm page again
        return Login Page instance 
    '''

    def switch_second_tab_page(self):
        super().switch_second_tab_page()
        Logging().reportDebugStep(self, "Switch the second page")
        return CRMLoginPageUI(self.driver)
