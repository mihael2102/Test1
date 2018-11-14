from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging


class CaWithdrawHistory(BrandBasePage):
    def __init__(self):
        super().__init__()

    '''
        Returns the status request
    '''

    def get_status_request(self):
        #sleep(2)
        status_request = super().wait_load_element_present("//td[@class='td-20-pandats'][2]")
        Logging().reportDebugStep(self, "Returns the status request  " + status_request.text)
        return status_request.text

    '''
        Choice an account from withdraw pop-up history
    '''

    def select_account(self, account):
        account_drop_down = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//custom-select[@name='tradingAccounts']")))
        account_drop_down.click()
        #sleep(1)

        select = super().wait_element_to_be_clickable("//custom-select[@name='tradingAccounts']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % account)

        self.driver.execute_script("arguments[0].scrollIntoView();", select)
        select.click()
        Logging().reportDebugStep(self, "The account was selected  " + select.text)
        return CaWithdrawHistory()

    '''
        Click the cancel request from withdraw pop-up history
    '''

    def click_cancel(self):
        cancel_button = super().wait_load_element_present("//button[contains(text(),'Cancel')]")
        cancel_button.click()
        submit_cancel_button = super().wait_load_element_present("//button[contains(text(),'yes')]")
        submit_cancel_button.click()
        Logging().reportDebugStep(self, "The account was canceled  ")
        return CaWithdrawHistory()
