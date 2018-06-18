from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage


class MT4CheckPasswordModule(CRMBasePage):

    def __init__(self):
        super().__init__()

    '''
        Choice an account from the pick-list
        :parameter account the live account of the client
        :returns MT4 Check PasswordModule instance
    '''

    def select_account(self, account):
        drop_down = super().wait_element_to_be_clickable("//select[@name='pwd_loginSel']")
        drop_down.click()
        select_account = self.driver.find_element(By.XPATH, "//select[@name='pwd_loginSel']//"
                                                            "following-sibling::*[contains(text(),'%s')]" % account)
        select_account.click()
        return MT4CheckPasswordModule()

    '''
         Enter the password 
         :parameter password the password of the  live account
         :returns MT4 Check PasswordModule instance
    '''

    def enter_password(self, password):
        field_password = self.driver.find_element(By.XPATH, "//input[@type='password']")
        field_password.clear()
        field_password.send_keys(password)
        return MT4CheckPasswordModule()

    '''
        Enter the check button 
        :returns MT4 Check PasswordModule instance
    '''

    def click_check_button(self):
        check_button = self.driver.find_element(By.XPATH, "//span[@id='MTPasswordSubmitButton']")
        check_button.click()
        return MT4CheckPasswordModule()

    def refresh_page(self):
        super().refresh_page()
        return MT4CheckPasswordModule()


