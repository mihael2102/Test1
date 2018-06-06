from selenium.webdriver.common.by import By
from src.main.python.ui.brand.model.ca_base_page.BrandBasePage import BrandBasePage
from src.main.python.ui.brand.model.client_area_modules.deposit.CASuccessDeposit import CASuccessDeposit


class CADeposit(BrandBasePage):

    def __init__(self):
        super().__init__()

    def click_depost(self):
        print("hello")

    def select_payment_method(self, payment_method):
        method = super().wait_load_element_present("//div[@class='pay-method-pandats'][%s]" % payment_method)
        method.click()
        return CADeposit()

    def set_amount_deposit(self, amount):
        amount_element = self.driver.find_element(By.XPATH, "//input[@name='amount']")
        amount_element.clear()
        amount_element.send_keys(amount)
        return CADeposit()

    def click_deposit_button(self):
        deposit_button = self.driver.find_element(By.XPATH, "//button[@class='forex-button-pandats']")
        deposit_button.click()
        return CADeposit()

    def set_card_number(self, card_number):
        card_number_element = self.driver.find_element(By.XPATH, "//input[@name='number']")
        card_number_element.clear()
        card_number_element.send_keys(card_number)
        return CADeposit()

    def set_expiry_date(self, expiry_date):
        expiry_date_element = self.driver.find_element(By.XPATH, "//input[@name='expiryMonth']")
        expiry_date_element.clear()
        expiry_date_element.send_keys(expiry_date)
        return CADeposit()

    def set_expiry_year(self, expiry_year):
        expiry_year_element = self.driver.find_element(By.XPATH, "//input[@name='expiryYear']")
        expiry_year_element.clear()
        expiry_year_element.send_keys(expiry_year)
        return CADeposit()

    def set_cvc(self, cvc_number):
        cvc_element = self.driver.find_element(By.XPATH, "//input[@name='cvv']")
        cvc_element.clear()
        cvc_element.send_keys(cvc_number)
        return CADeposit()

    def perform_deposit(self):
        deposit_button = self.driver.find_element(By.XPATH, "//button[@class='forex-button-pandats']")
        deposit_button.click()
        return CASuccessDeposit()
