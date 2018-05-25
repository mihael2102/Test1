from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from src.main.python.ui.crm.model.crm_base_page.CRMBasePage import CRMBasePage
from selenium.webdriver.support import expected_conditions as EC

from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage


class MT4Withdraw(CRMBasePage):
    def __init__(self):
        super().__init__()

    def make_withdraw(self, account_number, amount):
        self.select_payment_method()
        self.select_status()
        self.select_account(account_number)
        self.set_amount(amount)
        self.set_description()
        self.create_deposit()
        return CRMClientProfilePage()

    def select_payment_method(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='payment_method']")))
        select = Select(self.driver.find_element(By.XPATH, "//select[@name='payment_method']"))
        select.select_by_visible_text("Credit card")
        return MT4Withdraw()

    def select_status(self):
        select = Select(self.driver.find_element(By.XPATH, "//select[@id='transaction_status_id']"))
        select.select_by_visible_text("Approved")
        return MT4Withdraw()

    def select_account(self, account):
        drop_down = self.driver.find_element(By.XPATH, "//select[@name='loginserver']")

        drop_down.click()

        select_account = self.driver.find_element(By.XPATH, "//select[@name='loginserver']//"
                                                            "following-sibling::*[contains(text(),'%s')]" % account)
        select_account.click()
        return MT4Withdraw()

    def set_amount(self, amount):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='amount']")
        amount_filed.clear()
        amount_filed.send_keys(amount)
        return MT4Withdraw()

    def set_description(self):
        amount_filed = self.driver.find_element(By.XPATH, "//input[@id='transaction_comment']")
        amount_filed.clear()
        amount_filed.send_keys("Test")
        return MT4Withdraw()

    def create_deposit(self):
        create_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Create')]")
        create_button.click()
        return CRMClientProfilePage()
