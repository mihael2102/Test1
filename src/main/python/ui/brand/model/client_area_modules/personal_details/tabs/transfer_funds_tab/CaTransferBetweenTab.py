from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.utils.logs.Loging import Logging


class CaTransferBetweenTab(BrandBasePage):

    def __init__(self):
        super().__init__()

    def choose_transfer_from_account(self, transfer_to_from_account):
        drop_down_trading_account_drop_down = self.driver.find_element(By.XPATH,
                                                                       "//custom-select[@name='accountFrom']")
        drop_down_trading_account_drop_down.click()
        sleep(1)

        select = self.driver.find_element(By.XPATH, "//custom-select[@name='accountFrom']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % transfer_to_from_account)

        self.driver.execute_script("arguments[0].scrollIntoView();", select)
        select.click()
        Logging().reportDebugStep(self,
                                  "Select the first account that transfers the amount to the second account in the drop down: " + transfer_to_from_account)

        return CaTransferBetweenTab()

    def choose_transfer_to_account(self, transfer_to_account):
        drop_down_trading_account_drop_down = self.driver.find_element(By.XPATH,
                                                                       "//custom-select[@name='accountTo']")
        drop_down_trading_account_drop_down.click()
        sleep(1)

        select = self.driver.find_element(By.XPATH, "//custom-select[@name='accountTo']//"
                                                    "following-sibling::*[contains(text(),'%s')]" % transfer_to_account)

        self.driver.execute_script("arguments[0].scrollIntoView();", select)
        select.click()
        Logging().reportDebugStep(self,
                                  "Select the second account that receives the amount from  the first account in the drop down: " + transfer_to_account)
        return CaTransferBetweenTab()

    def set_amount(self, second_account, amount):
        amount_field = self.driver.find_element(By.XPATH, "//input[@type='text']")
        amount_field.clear()
        amount_field.send_keys(amount)
        Logging().reportDebugStep(self,
                                  "Set amount for  " + second_account + " = " + amount)
        return CaTransferBetweenTab()

    def confirm_check_box(self):
        check_box = self.driver.find_element(By.XPATH, "//label[@for='transferConfirm']")
        check_box.click()
        Logging().reportDebugStep(self,
                                  "Confirm checkbox")
        return CaTransferBetweenTab()

    def make_transfer_button(self):
        amount_field = self.driver.find_element(By.XPATH, "//button[contains(text(),'Make Transfer')]")
        amount_field.click()
        Logging().reportDebugStep(self,
                                  "Click the transfer_button")
        return CaTransferBetweenTab()

    def refreshing_wait(self):
        super().refreshing_wait()
