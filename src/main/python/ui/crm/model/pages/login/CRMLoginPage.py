from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp


class CRMLoginPage(CRMBasePage):

    '''
        Open the second tabs of crm page
        :parameter url crm page url  
    '''

    def open_second_tab_page(self, url):
        super().open_second_tab_page(url)
        Logging().reportDebugStep(self, "Open second tabs page: " + url + '\n')
        return CRMLoginPage(self.driver)

    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return CRMLoginPage(self.driver)

    '''
        Login  to CRM 
        :parameter name pandaqa name
        :parameter password pandaqa password
        return Home Page instance    
    '''

    def crm_login(self, user_name, password, otp_secret=None):
        user_name_field = self.driver.find_element(By.XPATH, "//input[@id='user_name']")
        password__field = self.driver.find_element(By.XPATH, "//input[@id='user_password']")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='submitButton']")
        user_name_field.clear()
        user_name_field.send_keys(user_name)
        Logging().reportDebugStep(self, "Setting the user name: " + user_name)
        password__field.clear()
        password__field.send_keys(password)
        Logging().reportDebugStep(self, "Setting the password")
        login_button.click()
        Logging().reportDebugStep(self, "Click the Login button")
        sleep(1)
        try:
            otp_field = self.driver.find_element(By.XPATH, "//input[@id='otp']")
            submit_button = self.driver.find_element(By.XPATH, "//a[@id='submitButton2']")
            time_otp = pyotp.TOTP(otp_secret)
            otp = time_otp.now()
            otp_field.clear()
            otp_field.send_keys(otp)
            Logging().reportDebugStep(self, "Setting the otp token: " + otp)
            submit_button.click()
            Logging().reportDebugStep(self, "Click the submit button")
        except NoSuchElementException:
            Logging().reportDebugStep(self, "No OTP authentication is required")

        # Wait for News popup at Old forex and close popup if it is shown
        try:
            # if ("uminvestments" or "ogtrade") in super().get_current_url():
            sleep(8)
            do_not_show_again_checkbox = super().wait_element_to_be_clickable("//*[@id='do_not_show']", timeout=4)
            do_not_show_again_checkbox.click()

            close_window_button = super().wait_element_to_be_clickable(
                                        "//*[@id = 'whats_newcontent']//button[@aria-label = 'Close']", timeout=4)
            close_window_button.click()
            Logging().reportDebugStep(self, "'What's new' popup was closed")
        except (NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "'What's new' popup isn't displayed ")
        return ClientsPage(self.driver)

    '''
        Select the crm page again
        return Login Page instance 
    '''

    def switch_second_tab_page(self):
        super().switch_second_tab_page()
        Logging().reportDebugStep(self, "Switch the second page")
        return CRMLoginPage(self.driver)




