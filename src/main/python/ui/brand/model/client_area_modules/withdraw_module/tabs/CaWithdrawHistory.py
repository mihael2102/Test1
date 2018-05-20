from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage


class CaWithdrawHistory(BrandBasePage):
    def __init__(self):
        super().__init__()

    def get_status_request(self):
        sleep(2)
        status_request = super().wait_load_element("//td[@class='td-20-pandats'][2]")
        return status_request.text

    def select_account(self, account):
        account_drop_down = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//custom-select[@name='tradingAccounts']")))
        account_drop_down.click()
        sleep(1)

        select = self.driver.find_element(By.XPATH, "//custom-select[@name='tradingAccounts']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % account)

        self.driver.execute_script("arguments[0].scrollIntoView();", select)
        select.click()
        return CaWithdrawHistory()

    def click_cancel(self):
        cancel_button = super().wait_load_element("//button[contains(text(),'Cancel')]")
        cancel_button.click()
        submit_cancel_button = super().wait_load_element("//button[contains(text(),'yes')]")
        submit_cancel_button.click()
        return CaWithdrawHistory()
