from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.withdraw_module.tabs.CaWithdrawSecondStepRequest import \
    CaWithdrawSecondStepRequest


class CaWithdrawFirstStepRequest(BrandBasePage):
    def __init__(self):
        super().__init__()

    def perform_withdraw_first_step_request(self, account_number):
        self.choose_account(account_number)
        self.set_amount(CaConstants.AMOUNT_WITHDRAW)
        self.click_withdraw_funds_button()
        return CaWithdrawSecondStepRequest()

    def choose_account(self, account):
        drop_down_trading_account_drop_down = self.driver.find_element(By.XPATH,
                                                                       "//custom-select[@name='activeTradingAccount']")
        drop_down_trading_account_drop_down.click()
        sleep(2)

        select = self.driver.find_element(By.XPATH, "//custom-select[@name='activeTradingAccount']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % account)

        self.driver.execute_script("arguments[0].scrollIntoView();", select)
        select.click()

        return CaWithdrawFirstStepRequest()

    def set_amount(self, amount):
        amount_field = self.driver.find_element(By.XPATH,
                                                "//div[@class='amount-curr-input-pandats']//input[@name='value']")
        amount_field.clear()
        amount_field.send_keys(amount)
        return CaWithdrawFirstStepRequest()

    def click_withdraw_funds_button(self):
        withdraw_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Withdraw Funds')]")
        withdraw_button.click()
        return CaWithdrawSecondStepRequest()
