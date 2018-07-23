from time import sleep
from _pytest.config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.client_area_modules.withdraw_module.tabs.CaWithdrawHistory import CaWithdrawHistory
from src.main.python.utils.logs.Loging import Logging
from src.main.python.utils.config import Config
from src.test.python.utils.TestDataConstants import TestDataConstants


class CaWithdrawSecondStepRequest(BrandBasePage):
    def __init__(self):
        super().__init__()

    def perform_withdraw_second_step_request(self):
        self.set_card_number_field(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CREDIT_CARD))
        self.set_expiry_date(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.EXPIRY_DATE))
        self.set_year_field(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.EXPIRY_YEAR))
        self.set_cvc_field(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CVC))
        self.select_withdraw_reason(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.WITHDRAWAL_REASON))
        self.submit_button()
        return CaWithdrawSecondStepRequest()

    def set_card_number_field(self, card_number):
        super().wait_load_element_present("//input[@name='number']")
        card_number_field = self.driver.find_element(By.XPATH,
                                                     "//input[@name='number']")
        card_number_field.clear()
        card_number_field.send_keys(card_number)
        Logging().reportDebugStep(self, "Set a card number_field")
        return CaWithdrawSecondStepRequest()

    def set_expiry_date(self, expiry_date):
        card_number_field = self.driver.find_element(By.XPATH,
                                                     "//input[@name='expiryMonth']")
        card_number_field.clear()
        card_number_field.send_keys(expiry_date)
        Logging().reportDebugStep(self, "Set a expiry date field")
        return CaWithdrawSecondStepRequest()

    def set_year_field(self, year):
        card_number_field = self.driver.find_element(By.XPATH,
                                                     "//input[@name='expiryYear']")
        card_number_field.clear()
        card_number_field.send_keys(year)
        Logging().reportDebugStep(self, "Set a year field field")
        return CaWithdrawSecondStepRequest()

    def set_cvc_field(self, cvc):
        card_number_field = self.driver.find_element(By.XPATH,
                                                     "//input[@name='cvv']")
        card_number_field.clear()
        card_number_field.send_keys(cvc)
        Logging().reportDebugStep(self, "Set a  cvc field")
        return CaWithdrawSecondStepRequest()

    def select_withdraw_reason(self, reason):
        drop_down_reason = self.driver.find_element(By.XPATH, "//custom-select[@name='withdrawalReasonsList']")
        drop_down_reason.click()
        Logging().reportDebugStep(self, "Click  the drop down reason")
        select_reason = self.driver.find_element(By.XPATH, "//custom-select[@name='withdrawalReasonsList']//"
                                                           "following-sibling::span[contains(text(),'%s')]" % reason)
        select_reason.click()
        Logging().reportDebugStep(self, "Select the withdraw_ca reason")
        return CaWithdrawSecondStepRequest()

    def submit_button(self):
        submit_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]")))
        submit_button.click()
        Logging().reportDebugStep(self, "Click the submit button")
        return CaWithdrawSecondStepRequest()

    def click_withdraw_history_tab(self):
        sleep(3)
        withdraw_history_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='section-top-menu-pandats']//li[2]")))
        withdraw_history_button.click()
        Logging().reportDebugStep(self, "Click the withdraw_ca history tabs")
        return CaWithdrawHistory()
