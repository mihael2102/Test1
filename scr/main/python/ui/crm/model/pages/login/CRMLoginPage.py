from selenium.webdriver.common.by import By

from scr.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from scr.main.python.ui.crm.model.pages.main.CRMHomePage import CRMHomePage
from scr.main.python.utils.logs.Loging import Logging


class CRMLoginPage(CRMBasePage):

    def __init__(self):
        super().__init__()

    '''
        Open the second tabs of crm page
        :parameter url crm page url  
    '''

    def open_second_tab_page(self, url):
        super().open_second_tab_page(url)
        Logging().reportDebugStep(self, "Open second tabs page: " + url + '\n')
        return CRMLoginPage()

    def open_first_tab_page(self, url):
        super().open_first_tab_page(url)
        Logging().reportDebugStep(self, "Open first tabs page: " + url)
        return CRMLoginPage()

    '''
        Login  to CRM 
        :parameter name pandaqa name
        :parameter password pandaqa password
        return Home Page instance    
    '''

    def crm_login(self, user_name, password):
        self.log = Logging()
        user_name_field = self.driver.find_element(By.XPATH, "//input[@id='user_name']")
        password__field = self.driver.find_element(By.XPATH, "//input[@id='user_password']")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='submitButton']")
        user_name_field.clear()
        user_name_field.send_keys(user_name)
        Logging().reportDebugStep(self, "Setting the user name in the field : " + user_name + '\n')
        password__field.clear()
        password__field.send_keys(password)
        Logging().reportDebugStep(self, "Setting the user name in the password: " + password + '\n')
        login_button.click()
        Logging().reportDebugStep(self, "Click the login button" + '\n')
        return CRMHomePage()

    '''
        Select the crm page again
        return Login Page instance 
    '''

    def switch_second_tab_page(self):
        super().switch_second_tab_page()
        Logging().reportDebugStep(self, "Switch  the second page")
        return CRMLoginPage()
